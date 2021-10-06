import pandas as pd
import pathlib

output_dir = '/glade/scratch/jamesmcc/aorc_forcing_symlinks'
for yy in range(42):
    year_dir = pathlib.Path(output_dir) / str(yy + 1979)
    if not year_dir.exists():
        _ = year_dir.mkdir()
    
input_dir_yxz = '/glade/campaign/ral/hap/zhangyx/AORC.Forcing'
input_dir_arn = '/glade/p/cisl/nwc/nwm_forcings/AORC'

strf_yxz = f'{input_dir_yxz}/%Y/%Y%m%d%H%M.LDASIN_DOMAIN1'
strf_arn = f'{input_dir_arn}/%Y%m%d%H.LDASIN_DOMAIN1'
strf_arn_2 = f'{input_dir_arn}/%Y%m%d%H00.LDASIN_DOMAIN1'
strf_jlm = f'{output_dir}/%Y/%Y%m%d%H%M.LDASIN_DOMAIN1'

dates_list = [
    {'start': '1979-02-01 00:00' , 'end': '2006-12-31 23:00', 'strf': strf_yxz, },
    {'start': '2007-01-01 00:00' , 'end': '2019-12-31 23:00', 'strf': strf_arn, },
    {'start': '2020-01-01 00:00' , 'end': '2020-12-31 23:00', 'strf': strf_arn_2, },]

for params in dates_list:
   
    start = pd.to_datetime(params['start'])
    end = pd.to_datetime(params['end'])
    strf = params['strf']

    dates = pd.date_range(start=start, end=end, freq='1h')

    for dd in dates:
        src = pathlib.Path(dd.strftime(strf_jlm))
        if not src.exists():
            tgt = pathlib.Path(dd.strftime(strf))
            assert tgt.exists()
            _ = src.symlink_to(tgt)
