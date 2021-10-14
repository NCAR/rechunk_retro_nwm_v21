#!/usr/bin/env python3
###!/glade/work/jamesmcc/python_envs/379zr/bin/ipython --pdb
import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    import numpy as np
    import os
    import pandas as pd
    import pathlib
    import random
    import socket
    import sys
    import time
    import xarray as xr

    import dask
    from dask.distributed import Client, progress, LocalCluster, performance_report
    from dask_jobqueue import PBSCluster

# using dask speeds this up.    
n_workers = 6
n_cores = 1
queue = "casper"
cluster_mem_gb = 5
wall_time = "09:00:00"

type_pattern_dict = {
    "chrtout.zarr": "CHRTOUT_DOMAIN1.comp",
    "gwout.zarr": "GWOUT_DOMAIN1.comp",
    "lakeout.zarr": "LAKEOUT_DOMAIN1.comp",
    "rtout.zarr": "RTOUT_DOMAIN1.comp",
    "ldasout.zarr" : "LDASOUT_DOMAIN1.comp",
    "precip.zarr": "LDASIN_DOMAIN1",
}


def main(file_rechunked, start_chunk, end_chunk):
    pattern = type_pattern_dict[file_rechunked.name]

    print("Set cluster")
    cluster = PBSCluster(
        cores=n_cores,
        memory=f"{cluster_mem_gb}GB",
        queue=queue,
        project="NRAL0017",
        walltime=wall_time,
        death_timeout=75,
    )
    dask.config.set({"distributed.dashboard.link": "/{port}/status"})
    print("Scale cluster")
    cluster.adapt(maximum=n_workers, minimum=n_workers)
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
    # numcodecs.blosc.use_threads = False
    # fraction of worker memory for each chunk (seems to be the max possible)
    chunk_mem_factor = 0.9
    # print(cluster.worker_spec[0]['options']['memory_limit'])
    max_mem = f"{format(chunk_mem_factor * cluster_mem_gb / n_workers, '.2f')}GB"

    orig_dir = pathlib.Path("/glade/scratch/zhangyx/WRF-Hydro/model.data.v2.1")
    if file_rechunked.name == 'precip.zarr':
        orig_dir = pathlib.Path(
            '/glade/scratch/jamesmcc/aorc_forcing_symlinks')

    # Open the rechunked zarr output
    ds = xr.open_zarr(file_rechunked)
    print(f"Checking {file_rechunked.name} against its source files")
    print(ds)

    # Check one time in every time chunk
    data_vars = list(set(list(ds.data_vars)).difference(set(['crs'])))
    dv0 = ds[data_vars[0]]
    time_ind = dv0.dims.index('time')
    time_chunks = dv0.chunks[time_ind]

    check_static_variables = True

    if start_chunk is None or end_chunk is None:
        n_time_chunks = len(time_chunks)
        chunk_list = list(reversed(range(n_time_chunks)))
    else:
        n_time_chunks = end_chunk - start_chunk + 1
        chunk_list = (
            list(reversed(range(start_chunk, end_chunk + 1))))

    for cc in chunk_list:
        timer_start = time.perf_counter()
        if start_chunk is None or end_chunk is None:
            print(f'\nChecking a random time in chunk #{cc+1} (of {n_time_chunks})...', flush=True)
        else:
            print(
                f'\nChecking a random time in chunk {cc} '
                f'(in reversed(range({start_chunk}, {end_chunk} + 1)))',
                flush=True)

        ind_chunk_first_time = sum(time_chunks[0:cc])
        n_samples = 1
        random_samp = random.sample(range(time_chunks[cc]), n_samples)[0]
        rr = ind_chunk_first_time + random_samp

        time_random = pd.to_datetime(str(ds.time[rr].values))
        file_random = orig_dir / (
            time_random.strftime("%Y/") + time_random.strftime(f"%Y%m%d%H%M.{pattern}")
        )
        assert file_random.exists()
        ds_random = xr.open_dataset(file_random)

        # Static variables check
        if check_static_variables:
            print(f"\nCheck (non-time) static variables once")
            for vv in ds.variables:
                if 'time' in ds[vv].dims:
                    continue
                if vv == "time":
                    continue
                if file_rechunked.name == 'chrtout.zarr':
                    if vv in ['gage_id']:
                        print(f'Not checking gage_id')
                        continue

                print(f"Checking variable: {vv}")
                if vv == "crs":
                    if file_rechunked.name == 'precip.zarr':
                        assert ds_random[vv].values == ds[vv].values
                        for key, val in ds[vv].attrs.items():
                            assert np.all(val == ds_random[vv].attrs[key])
                    else:
                        assert ds_random[vv].equals(ds[vv])
                elif not "time" in ds[vv].dims:
                    diffs = ds_random[vv].values - ds[vv].values
                    assert np.nanmin(np.abs(diffs)) < 1e-8

            check_static_variables = False

        # Check at this time
        print(f"Checking time: {ds.time[rr].values}")
        for vv in ds.variables:
            if vv == "time":
                continue
            if "time" in ds[vv].dims:
                print(f"Checking variable: {vv}", flush=True)
                diffs = ds_random[vv].values - ds[vv].isel(time=rr).values
                if np.isnan(diffs).any():
                    n_nans_diff = np.isnan(diffs).sum()
                    print(f"{n_nans_diff} nans present")
                    assert n_nans_diff == np.isnan(ds_random[vv].values).sum()
                    assert n_nans_diff == np.isnan(ds[vv].isel(time=rr).values).sum()
                    assert np.nanmin(np.abs(diffs)) < 1e-8
                else:
                    assert np.min(np.abs(diffs)) < 1e-8

        timer_end = time.perf_counter()
        print(f"Time for this file: {timer_end - timer_start:0.4f} seconds")        


if __name__ == "__main__":
    args = sys.argv
    # print(args)
    if len(args) != 2 and len(args) != 4:
        raise ValueError("verify_output.py takes a single arg for a valid file")
    file_rechunked = pathlib.Path(args[1])
    if len(args) == 4:
        start_chunk = int(args[2])
        end_chunk = int(args[3])
    else:
        start_chunk = None
        end_chunk = None
        
    if not file_rechunked.exists():
        raise FileExistsError(f"File does not exist: {str(file_rechunked)}")

    result = main(file_rechunked, start_chunk=start_chunk, end_chunk=end_chunk)

    sys.exit(result)
