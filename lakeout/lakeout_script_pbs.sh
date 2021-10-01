#!/bin/bash -l
#PBS -N lakeout
#PBS -A NRAL0017
#PBS -l select=1:ncpus=1:mem=10GB
#PBS -l walltime=02:00:00
#PBS -q casper
#PBS -j oe

export TMPDIR=/glade/scratch/$USER/temp
mkdir -p $TMPDIR

module load ncarenv python/3.7.9
unset DASK_ROOT_CONFIG
source /glade/work/jamesmcc/python_envs/379zr/bin/activate

python /glade/u/home/jamesmcc/WRF_Hydro/rechunk_retro_nwm_v21/lakeout/lakeout_to_zarr.py

exit 0
