import datetime as dt
import numpy as np
import pathlib
import pandas as pd
import xarray as xr

# should be the entire config.
# file_last_prev_date = dt.datetime.strptime('201811161800', '%Y%m%d%H00')
# file_last_prev_date = dt.datetime.strptime('201812122300', '%Y%m%d%H00')
file_last_prev_date = dt.datetime.strptime('201911132300', '%Y%m%d%H00')

# -------------------------------------------------------


def preprocess_precip(ds):
    drop_vars_full = [
        "reference_time", "crs", 'U2D',
        'V2D', 'LWDOWN', 'T2D',
        'Q2D', 'PSFC', 'SWDOWN',
        'LQFRAC', 'x', 'y']
    drop_vars = list(
        set(ds.variables).intersection(set(drop_vars_full)))
    ds = ds.drop(drop_vars)
    if 'valid_time' in ds.variables:
        ds= (ds
             .rename({'valid_time': 'time'})
             .set_coords('time')
             .swap_dims({'Time': 'time'})
             .drop('Times')
             .rename({'south_north': 'y', 'west_east': 'x'}))
    return ds.reset_coords(drop=True)


date_start = file_last_prev_date + dt.timedelta(hours=1)
time_chunk_size = 672
freq='1H'
dates = pd.date_range(
    start=date_start, periods=time_chunk_size, freq=freq)

input_dir = '/glade/scratch/jamesmcc/aorc_forcing_symlinks'
files = [
    pathlib.Path(
        f"{input_dir}/"
        f'{date.strftime("%Y")}/'
        f'{date.strftime("%Y%m%d%H%M")}.LDASIN_DOMAIN1'
    )
    for date in dates]

assert all([ff.exists() for ff in files])

ds = xr.open_mfdataset(
    files,
    parallel=True,
    preprocess=preprocess_precip,
    combine="by_coords",
    concat_dim="time",
    join="override",)

times = ds.time.values
print(len(times))

time_diff = np.diff(times)
wh_miss = np.where(time_diff > time_diff[0])[0]
assert len(wh_miss) == 1, "more than a single missing time! investigate."

missing_before = times[wh_miss + 0][0]
missing_after = times[wh_miss + 1][0]
missing_gap = missing_after - missing_before
n_missing_times = int(missing_gap / np.timedelta64(int(freq.split('H')[0]), 'h'))

for tt in range(n_missing_times):
    print(tt)
    time_miss = pd.to_datetime(missing_before) + dt.timedelta(hours=tt + 1)
    da_valid_time = xr.DataArray(
        np.array([str(time_miss)], dtype='datetime64[ns]'),
        dims=['Time'])

    file_bad = pathlib.Path(
        f'/glade/p/cisl/nwc/nwm_forcings/AORC/'
        f'{time_miss.strftime("%Y%m%d%H")}.LDASIN_DOMAIN1')
    ds_bad = xr.open_dataset(file_bad)
    ds_fix = ds_bad.drop('valid_time').copy()
    ds_bad.close()
    ds_fix['valid_time'] = da_valid_time

    file_replacement = pathlib.Path(
        f'/glade/scratch/jamesmcc/aorc_forcing_symlinks/'
        f'{time_miss.strftime("%Y")}/'
        f'{time_miss.strftime("%Y%m%d%H00")}.LDASIN_DOMAIN1')

    if file_replacement.exists():
        file_replacement.unlink()

    ds_fix.to_netcdf(file_replacement)
    ds_fix.close()

    ds_check = xr.open_dataset(file_replacement)
    ds_check.close()
    ds_check = xr.open_dataset(file_replacement)  # This makes no sense, there seems to be a bug in xarray
    assert ds_check.valid_time.equals(ds_fix.valid_time)
    assert ds_check.valid_time == time_miss
    ds_check.close()
    del ds_check, ds_fix, ds_bad

# Check the full.    
ds = xr.open_mfdataset(
    files,
    parallel=True,
    preprocess=preprocess_precip,
    combine="by_coords",
    concat_dim="time",
    join="override",)

assert len(ds.time) == time_chunk_size
