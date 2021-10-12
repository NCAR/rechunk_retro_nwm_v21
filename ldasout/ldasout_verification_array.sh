#!/bin/bash -l
#PBS -N ldasv
#PBS -A NRAL0017
#PBS -l select=1:ncpus=2:mem=8GB
#PBS -l walltime=23:00:00
#PBS -q casper
#PBS -j oe
#PBS -J 0-3

export TMPDIR=/glade/scratch/$USER/temp
mkdir -p $TMPDIR

# module load python/3.7.9
source /glade/work/jamesmcc/python_envs/379zr/bin/activate

start_arr=(0 137 273 410)
end_arr=(136 272 409 546)
start=${start_arr[${PBS_ARRAY_INDEX}]}
end=${end_arr[${PBS_ARRAY_INDEX}]}

cd /glade/u/home/jamesmcc/WRF_Hydro/rechunk_retro_nwm_v21
log_file=ldasout/ldasout_verification_${PBS_ARRAY_INDEX}.log

./verify_output.py /glade/p/datashare/ishitas/ldasout/ldasout.zarr $start $end | tee $log_file

exit 0

