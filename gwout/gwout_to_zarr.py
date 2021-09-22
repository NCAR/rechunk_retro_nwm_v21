import sys
sys.path.append("..")

import dask
from dask.distributed import Client, progress, LocalCluster, performance_report
from dask_jobqueue import PBSCluster
from math import ceil
import numpy as np
import numcodecs
import os
import pandas as pd
import pathlib
from pprint import pprint
from read_yaml_config import read_yaml_config
from rechunker import rechunk
import shutil
import socket
import subprocess
import time
import xarray as xr
import zarr

config_file = (
    '/glade/u/home/jamesmcc/WRF_Hydro/rechunk_retro_nwm_v21/'
    'gwout/gwout_chunk_sizes.yaml')

config = read_yaml_config(config_file)

dirs_cfg = config['dirs']
output_path = pathlib.Path(dirs_cfg['output'])
input_dir = pathlib.Path(dirs_cfg['input'])

files_cfg = config['files']
file_chunked = pathlib.Path(files_cfg['chunked'])
file_step = pathlib.Path(files_cfg['step'])
file_last_step = pathlib.Path(files_cfg['last_step'])
file_temp = pathlib.Path(files_cfg['temp'])
file_log_loop_time = pathlib.Path(files_cfg['loop_time_log'])
input_fstring = files_cfg['input_fstring']

chunks_cfg = config['chunk_sizes']
time_chunk_size = chunks_cfg['time']
var_chunk_sizes = chunks_cfg['variables']
global_chunk_sizes = config['chunk_sizes']
_ = global_chunk_sizes.pop('variables')


dask_cfg = config['dask']
n_workers = dask_cfg['n_workers']
n_cores = dask_cfg['n_cores']
queue = dask_cfg['queue']
cluster_mem_gb = dask_cfg['cluster_mem_gb']

n_chunks_job = config['job']['n_chunks_process']

datetime_cfg = config['datetime']
end_date = datetime_cfg['end']
start_date = datetime_cfg['start']
freq = datetime_cfg['freq']

if not output_path.exists():
    output_path.mkdir()
os.chdir(output_path)


def del_zarr_file(the_file: pathlib.Path):
    if the_file.exists():
        try:
            shutil.rmtree(the_file)
            while os.path.exists(the_file):  # check if it still exists
                time.sleep(0.1)
                pass
        except:
            pass
    return None


def preprocess_gwout(ds):
    ds = ds.drop(["reference_time", "feature_id"])
    return ds.reset_coords(drop=True)


def eval_fstring(template, **kwargs):
    return eval(f"f'{template}'", kwargs)            


def main():
    print(f"Generate files list for all chunks in this job")
    if file_chunked.exists():
        print(f"\n ** Warning appending to existing output file: {file_chunked}")
        ds = xr.open_zarr(file_chunked)
        last_time = pd.Timestamp(ds.time.values[-1])
        ds.close()
        del ds
        dates = pd.date_range(
            start=last_time, periods=n_chunks_job * time_chunk_size + 1, freq=freq
        )[1:]
    else:
        dates = pd.date_range(
            start=start_date, periods=n_chunks_job * time_chunk_size, freq=freq
        )

    dates = dates[dates <= end_date]
    files = [
        pathlib.Path(
            eval_fstring(input_fstring, date=date)
            # f"{input_dir}/"
            # f'{date.strftime("%Y")}/'
            # f'{date.strftime("%Y%m%d%H%M")}.GWOUT_DOMAIN1.comp'
        )
        for date in dates
    ]

    n_chunks_job_actual = ceil(len(files) / time_chunk_size)

    print(f"Get single file data and metadata")
    dset = xr.open_dataset(files[0])

    print("Set cluster")
    cluster = PBSCluster(
        cores=n_cores,
        memory=f"{cluster_mem_gb}GB",
        queue=queue,
        project="NRAL0017",
        walltime="02:00:00",
        death_timeout=75,
    )
    dask.config.set({"distributed.dashboard.link": "/{port}/status"})

    print("Scale cluster")
    # cluster.adapt(maximum=n_workers, minimum=n_workers)
    cluster.scale(n_workers)

    print(f"Set client")
    client = Client(cluster)
    # print(client)
    dash_link = client.dashboard_link
    port = dash_link.split("/")[1]
    hostname = socket.gethostname()
    user = os.environ["USER"]
    print(f"Tunnel to compute node from local machine:")
    print(f"ssh -NL {port}: {hostname}:{port}{user}@cheyenne.ucar.edu")
    print(f"in local browser: ")
    print(f"http://localhost:{port}/status")
    numcodecs.blosc.use_threads = False
    # fraction of worker memory for each chunk (seems to be the max possible)
    chunk_mem_factor = 0.9
    # print(cluster.worker_spec[0]['options']['memory_limit'])
    max_mem = f"{format(chunk_mem_factor * cluster_mem_gb / n_workers, '.2f')}GB"

    indt = "    "
    for ii in range(n_chunks_job_actual):
        start_timer = time.time()

        print("\n-----------")
        print(f"ith chunk (of {n_chunks_job_actual} for this job): {ii+1}")

        istart = ii * time_chunk_size
        istop = int(np.min([(ii + 1) * time_chunk_size, len(files)]))
        files_chunk = files[istart:istop]
        print(f"{indt}First file: {files_chunk[0].name}")
        print(f"{indt}Last file: {files_chunk[-1].name}")

        ds = xr.open_mfdataset(
            files_chunk,
            parallel=True,
            preprocess=preprocess_gwout,
            combine="by_coords",
            concat_dim="time",
            join="override",
        )
        # print(ds)

        # add back in the 'feature_id' coordinate removed by preprocessing
        ds.coords["feature_id"] = dset.coords["feature_id"]

        # remove the temp and step zarr datasets
        # moving these and deleting asynchornously might help speed?
        print(f"{indt}Clean up any existing temp files")
        start_del_timer = time.time()
        _ = del_zarr_file(file_temp)
        _ = del_zarr_file(file_step)
        end_del_timer = time.time()

        # the last chunk will not have a full time_chunk_size
        # handle it separately
        if len(files_chunk) == time_chunk_size:
            chunk_plan = {}
            for var in ds.data_vars:
                if var in var_chunk_sizes.keys():
                    var_chunk = var_chunk_sizes[var]
                    chunk_plan[var] = var_chunk

            print(f"{indt}chunk_plan: {chunk_plan}")

            print(f"{indt}Set rechunk_obj")
            rechunk_obj = rechunk(
                ds,
                chunk_plan,
                max_mem,
                str(file_step),
                temp_store=str(file_temp),
                executor="dask",
            )

            print(f"{indt}Execute rechunk_obj")
            with performance_report(filename="dask-report.html"):
                result = rechunk_obj.execute(retries=10)

            print(f"{indt}After rechunk_obj.execute()")

            # read back in the zarr chunk rechunker wrote
            print(f"{indt}Open zarr step file")
            ds = xr.open_zarr(str(file_step), consolidated=False)

            print(f"{indt}Write/append step to zarr chunked file")
            if not file_chunked.exists():
                ds.to_zarr(str(file_chunked), consolidated=True, mode="w")
            else:
                ds.to_zarr(str(file_chunked), consolidated=True, append_dim="time")

            print(f"{indt}Close zarr chunked file")
            ds.close()

        else:
            print(f"{indt}Processing the final time chunk!")

            print(f"{indt}Clean up any existing temp files")
            start_del_timer = time.time()
            _ = del_zarr_file(file_temp)
            _ = del_zarr_file(file_step)
            _ = del_zarr_file(file_last_step)
            end_del_timer = time.time()

            print(f"{indt}Rehunking final chunk")
            ds1 = ds.chunk(global_chunk_sizes)
            _ = ds1.to_zarr(str(file_last_step), consolidated=True, mode="w")
            ds2 = xr.open_zarr(str(file_last_step), consolidated=True)
            ds2.to_zarr(file_chunked, consolidated=True, append_dim="time")

            print(f"{indt}Final file clean up")
            _ = del_zarr_file(file_temp)
            _ = del_zarr_file(file_step)
            _ = del_zarr_file(file_last_step)

        # end of loop timing and logging
        end_timer = time.time()
        time_taken = end_timer - start_timer
        del_time_taken = end_del_timer - start_del_timer
        print(f"{indt}time_taken: {time_taken}")
        print(f"{indt}del_time_take: {del_time_taken}")
        cmd = (
            f"echo completed core: {n_workers*n_cores} "
            # f"variable chunk sizes: {pprint(var_chunk_sizes)} "
            f"first_file: {files_chunk[0].name} "
            f"last_file: {files_chunk[-1].name} "
            f"loop_time_taken: {time_taken} "
            # f'del_time_taken: {del_time_taken} '
            f">> {file_log_loop_time}"
        )
        subprocess.run(cmd, shell=True)

    return 0


if __name__ == "__main__":
    result = main()
    sys.exit(result)
