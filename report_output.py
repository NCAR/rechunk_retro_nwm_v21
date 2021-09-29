#!/usr/bin/env python3
import warnings

with warnings.catch_warnings():
    import numpy as np
    import pathlib
    import subprocess
    import sys
    import xarray as xr
    import zarr as zr

nl = "\n"


def main(file_rechunked):

    print("\n-------------------------------------------------------")
    print(f"Output file report: {file_rechunked}")

    result = subprocess.run(
        f"du -shc {file_rechunked}", stdout=subprocess.PIPE, shell=True
    )
    file_size = result.stdout.decode("utf-8").split("\t")[0]
    print(f"Total file size: {file_size}")

    ds = xr.open_zarr(file_rechunked)
    dz = zr.open(file_rechunked)

    print("Dataset overviews:")
    print(f"zarr ds.info:\n{dz.info}")
    print(f"\nxarray ds.info:\n{ds}")

    print("\n-----------------------------------")
    print("Variable comparison xarray and zarr")
    for vv in ds.variables:
        print(f"\n--------\n")
        print(f"{vv}\n")
        print(f"xarray ds[{vv}]:{nl}{ds[vv]}")
        print(f"")
        info = dz[vv].info
        print(f"zarr dz[{vv}].info:{nl}{info}")
        chunk_bytes = np.prod(info.obj.chunks) * info.obj.dtype.itemsize
        storage_ratio = float(str(info.obj._info_reporter).split(':')[-2].split('\n')[0].split(' ')[1])
        print(f"Un-Compressed Chunk size in MB: {chunk_bytes / 1048576}")
        print(f"   Compressed Chunk size in MB: {chunk_bytes / 1048576 / storage_ratio}")        

    return 0


if __name__ == "__main__":
    args = sys.argv
    # print(args)
    if len(args) != 2:
        raise ValueError("output_report.py takes a single arg for a valid file")
    file_rechunked = pathlib.Path(args[1])
    if not file_rechunked.exists():
        raise FileExistsError(f"File does not exist: {str(file_rechunked)}")

    result = main(file_rechunked)

    sys.exit(result)
