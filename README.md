# nwm_v21_retro_rechunk
Rechunking retrospective runs to more approachable chunks in Zarr output.

## Data Access
The data are accessible via globus. They are located at 
```
/glade/p/datashare/jamesmcc/gwout.zarr
/glade/p/datashare/jamesmcc/lakeout.zarr
```
Please see
https://www2.cisl.ucar.edu/resources/storage-and-file-systems/using-the-ncar-data-sharing-service#retrieve
for accessing the data and let us know if permission errors arise. 


## Reposiroty Overview
There is (or will be) a directory for each file type

```
chrtout/
lakeout/
gwout/
ldasout/
rtout/
precip_forcing/
```

in this directory will be the following for each `type`:

```
type_report.log
type_verification.log
type_script_pbs.sh
type_submit_pbs.py
type_to_zarr.py
```

These files are explained below in detail. The log files contain all (most?) of the relevant 
information for understanding the data from both zarr and xarray perspectives.


## `type_report.log`
This file is report of metadata and other attributes (file sizes, chunk shapes and sizes, storage 
types, memory types compression ratios, etc). Reports are generated by the `verify_output.py` 
script using a  command like: 

```
(379zr) jamesmcc@crhtc55[1029]:~/WRF_Hydro/rechunk_retro_nwm_v21> ./verify_output.py /glade/scratch/jamesmcc/retro_collect/gwout/gwout.zarr | tee gwout/gwout_verification.log
```

The report starts with the full path to the file being reported.  

Next is the total size of the Zarr store (from `du -shc`).  

Then the zarr infor is printed for the full store. Next the xarray infor for the store is printed. 
These provide very different information but only a high-level overview of the data set.  

Next information is printed for every variable in the store, again both from xarray and zarr 
perspectives. This is important because of two reasons: 
* The data are stored as integers and converted to other types by xarray using scale\_factor and 
add\_offset metadata attributes
* There is compression being applied by Zarr.

The individual variable information shows how xarray is representing the data in memory (e.g. 
float64), how zarr is storing the data on disk (e.g. int32), the chunk size (e.g. time, feature_id) 
the total number of bytes (without compression) and the number of bytest actually stored (the 
compression ratio being the computed from these last two numbers of bytes). Then the full chunk size
is reported (without compression) in MB. These numbers are helpful in iterating to obtain the desired 
chunk sizes. 


## `type_verification.log`
This file is the log of a verification procedure run which compares the output data against the 
input data. There is a hardwired number of datetimes (currently 30) for which the data (full space) 
are verified against the input files. That number will include the first and last times being checked
first. The remainder of the times will be drawn at random from the index of times in the zarr 
output file (without replacement). The static variables in the file are checked once (at the first 
time) and the time varying variables are checked at every time. Values are checked to have less 
absolute differece than 1e-8 and if nans are present it is required that the diffs have the same
number of nans as both of the original and zarr datasets. 


## `type_script_pbs.sh`
This simply a static scipt designed to submit the `type_to_zarr.py` to the PBS scheduler on the 
casper system at NCAR. It takes no arguments. 


## `type_submit_pbs.py`
This python script determines the number of times the `type_script_pbs.sh` needs to be executed and
submits this many dependent jobs to the PBS queue. The dependence does not require success, so the 
jobs will continue in the event one of them fails.


## `type_to_zarr.py`
This is the python script which converts a given type to a single zarr file. It checks if the output 
file already exists, and if it does it then knows to start from the end of the existing output to 
continue the rechunking. 



