import dask
from dask.distributed import Client, progress, LocalCluster, performance_report
from dask_jobqueue import PBSCluster
from math import ceil
import numpy as np
import numcodecs
import os
import pandas as pd
import pathlib
from rechunker import rechunk
import shutil
import socket
import subprocess
import sys
import time
import xarray as xr
import zarr

# User config
output_path = pathlib.Path("/glade/p/cisl/nwc/ishitas/zarr_new/chrtout")

# Chunk config
time_chunk_size = 672
feature_chunk_size = 30000

n_workers = 18
n_cores = 1
queue = "casper"
cluster_mem_gb = 15

n_chunks_job = 12  # how many to do before exiting, 12 is approx yearly
# end_date = '2018-12-31 23:00' # full time
end_date = "1981-04-30 23:00"  # pilot 2 years
# this end_date tests all parts of the execution for
# chunk size 672 and n_chunks_job=1
# end_date = "1979-04-17 00:00"

# files
## output_path is a global, user-defined variable defined above.
os.chdir(output_path)
file_chunked = output_path / "chrtout.zarr"
file_step = output_path / "step.zarr"
file_last_step = output_path / "last_step.zarr"
file_temp = output_path / "temp.zarr"
file_log_loop_time = output_path / "chrtout_loop_time.txt"

# static information
# todo JLM: centralize this info?
input_dir = "/glade/scratch/zhangyx/WRF-Hydro/model.data.v2.1"
start_date = "1979-02-10 00:00"
freq = "1h"


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


def preprocess_chrtout(ds):
    ds = ds.drop(["reference_time", "feature_id", "crs"])
    return ds.reset_coords(drop=True)

def process_chrtout(ds):
    rl_file = ('/glade/work/jamesmcc/domains/private/CONUS_v2.1_final/NWM/DOMAIN/RouteLink_NWMv2.1.nc')
    rl = xr.open_dataset(rl_file)
    for vv in rl.variables:
        if vv in ['link', 'gages']:
            continue
        rl = rl.drop(vv)
    rl = rl.set_coords('link')
    rl = rl.rename({'link':'feature_id', 'gages': 'gage_id'})
    rl = rl.sortby('feature_id')
    print("Resetting coordinates")
    ds = ds.reset_coords(['longitude', 'latitude'])
    print("Asserting")
    assert rl.feature_id.equals(ds.feature_id)
    print("Merging")
    ds2 = ds.merge(rl)
    # check the join
    print("Checking join")
    gages_unique = np.unique(ds2.gage_id.values)
    gage_random = gages_unique[1]
    wh_random_ds = np.where(ds2.gage_id.isin([gage_random]).values)
    feature_random_ds = ds2.feature_id[wh_random_ds]
    wh_random_rl = np.where(rl.gage_id.isin([gage_random]).values)
    feature_random_rl = rl.feature_id[wh_random_rl]
    assert feature_random_rl.equals(feature_random_ds)
    # global meta data
    print("global meta data")
    attrs_keep = ['code_version', 'featureType', 'model_configuration', 'proj4']
    attrs_new = {key: value for key, value in ds2.attrs.items() if key in attrs_keep}
    ds2.attrs = attrs_new
    ds2['elevation'] = ds2.elevation[0,:]
    ds2['order'] = ds2.order[0,:]
    print("dropping vars")
    drop_vars = ['qBtmVertRunoff', 'qBucket', 'qSfcLatRunoff', 'q_lateral']
    ds2 = ds2.drop_vars(drop_vars)
    ds2 = ds2.set_coords(['longitude', 'latitude', 'elevation'])
    ds2.elevation.attrs['long_name'] = 'feature elevation'
    del ds2.elevation.attrs['standard_name']
    ds2.latitude.attrs['long_name'] = 'feature latitude'
    ds2.longitude.attrs['long_name'] = 'feature longitude'
    ds2.order.attrs['long_name'] = 'stream order'
    del ds2.order.attrs['standard_name']
    del ds2.time.attrs['valid_max']
    del ds2.time.attrs['valid_min']
    return ds2


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
            f"{input_dir}/"
            f'{date.strftime("%Y")}/'
            f'{date.strftime("%Y%m%d%H%M")}.CHRTOUT_DOMAIN1.comp'
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
            preprocess=preprocess_chrtout,
            combine="by_coords",
            concat_dim="time",
            join="override",
        )
        # print(ds)

        # add back in the 'feature_id' coordinate removed by preprocessing
        ds.coords["feature_id"] = dset.coords["feature_id"]
        ds = process_chrtout(ds)

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
                if len(ds[var].dims) == 2:
                    var_chunk = (time_chunk_size, feature_chunk_size)
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
                drop_vars = ['gage_id', 'order']
                ds = ds.drop_vars(drop_vars)
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
            ds1 = ds.chunk({"feature_id": feature_chunk_size, "time": time_chunk_size})
            _ = ds1.to_zarr(str(file_last_step), consolidated=True, mode="w")
            ds2 = xr.open_zarr(str(file_last_step), consolidated=True)
            drop_vars = ['gage_id', 'order']
            ds2 = ds2.drop_vars(drop_vars)
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
            f"time_chunk_size: {time_chunk_size} "
            f"feature_chunk_size: {feature_chunk_size} "
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
