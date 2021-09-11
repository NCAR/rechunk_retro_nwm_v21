#!/bin/bash -l
#PBS -N gwout
#PBS -A NRAL0017
#PBS -l select=1:ncpus=1:mem=10GB
#PBS -l walltime=02:00:00
#PBS -q casper
#PBS -j oe

export TMPDIR=/glade/scratch/$USER/temp
mkdir -p $TMPDIR

module load ncarenv python/3.7.9
source /glade/work/jamesmcc/python_envs/379zr/bin/activate

python /glade/u/home/jamesmcc/WRF_Hydro/rechunk_retro_nwm_v21/gwout/gwout_to_zarr.py

exit 0
