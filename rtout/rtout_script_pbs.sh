#!/bin/bash -l
#PBS -N rtout
#PBS -A NRAL0017
#PBS -l select=1:ncpus=1:mem=10GB
#PBS -l walltime=05:00:00
#PBS -q casper
#PBS -j oe
#PBS -k oed

export TMPDIR=/glade/scratch/$USER/temp
mkdir -p $TMPDIR

module load ncarenv python/3.7.9
source /glade/work/jamesmcc/python_envs/379zr/bin/activate

python /glade/u/home/jamesmcc/WRF_Hydro/rechunk_retro_nwm_v21/rtout/rtout_to_zarr.py > /glade/scratch/jamesmcc/retro_collect/rtout/rtout_log

exit 0
