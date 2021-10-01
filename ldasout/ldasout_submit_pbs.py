from ldasout_to_zarr import *

pbs_script = (
    "/glade/work/ishitas/zarr_retrospective/"  # configure this
    "rechunk_retro_nwm_v21/ldasout/ldasout_script_pbs.sh")

dates = pd.date_range(start=start_date, end=end_date, freq=freq)
files = [
    pathlib.Path(
        f"{input_dir}/"
        f'{date.strftime("%Y")}/'
        f'{date.strftime("%Y%m%d%H%M")}.LDASOUT_DOMAIN1.comp')
    for date in dates]
n_chunks = ceil(len(files) / time_chunk_size)
n_jobs = ceil(n_chunks / n_chunks_job)

qsub_str = "/bin/bash -c '"
for jj in range(n_jobs):
    if jj == 0:
        qsub_str += f"job_{jj}=`qsub -h {pbs_script}`;"
    else:
        qsub_str += f"job_{jj}=`qsub -W depend=afterany:$job_{jj-1} {pbs_script}`;"

qsub_str += "qrls $job_0;"
qsub_str += "'"
print("qsub_str: ", qsub_str)
result = subprocess.run(qsub_str, shell=True, check=True)

sys.exit(0)
