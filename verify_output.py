#!/usr/bin/env python3
import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    import numpy as np
    import pandas as pd
    import pathlib
    import random
    import sys
    import xarray as xr

orig_dir = pathlib.Path("/glade/scratch/zhangyx/WRF-Hydro/model.data.v2.1")

type_pattern_dict = {
    "chrtout.zarr": "CHRTOUT_DOMAIN1.comp",
    "gwout.zarr": "GWOUT_DOMAIN1.comp",
    "lakeout.zarr": "LAKEOUT_DOMAIN1.comp",
    "precip.zarr": "LDASIN_DOMAIN1",
}


def main(file_rechunked):
    if file_rechunked.name == 'precip.zarr':
        orig_dir = pathlib.Path(
            "/glade/campaign/ral/hap/zhangyx/AORC.Forcing")

    pattern = type_pattern_dict[file_rechunked.name]

    # Open the rechunked zarr output
    ds = xr.open_zarr(file_rechunked)
    print(f"Checking {file_rechunked.name} against its source files")
    print(ds)

    # randomly sample some times, but always check first and last
    n_samples = 30
    random_samp = random.sample(range(len(ds.time)), n_samples - 2)
    random_samp = [0, len(ds.time) - 1] + random_samp
    print(f"Checking data for {len(random_samp)} times")

    check_static_variables = True

    for ii in range(len(random_samp)):
        rr = random_samp[ii]
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
                if vv == "time":
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
        print(f"\n{ii+1}/{n_samples}")
        print(f"Checking time: {ds.time[rr].values}")
        for vv in ds.variables:
            if vv == "time":
                continue
            if "time" in ds[vv].dims:
                print(f"Checking variable: {vv}")
                diffs = ds_random[vv].values - ds[vv].isel(time=rr).values
                if np.isnan(diffs).any():
                    print(f"nans present")
                    assert np.isnan(diff).sum() == np.isnan(ds_random[vv].values).sum()
                    assert np.nanmin(np.abs(diffs)) < 1e-8
                else:
                    assert np.min(np.abs(diffs)) < 1e-8
                    ### THIS EQUATIONS NEEDS SCRUTINIZED


if __name__ == "__main__":
    args = sys.argv
    # print(args)
    if len(args) != 2:
        raise ValueError("verify_output.py takes a single arg for a valid file")
    file_rechunked = pathlib.Path(args[1])
    if not file_rechunked.exists():
        raise FileExistsError(f"File does not exist: {str(file_rechunked)}")

    result = main(file_rechunked)

    sys.exit(result)
