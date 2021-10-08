# nwm_v21_retro_rechunk
Rechunking NWM v2.1 retrospective runs to more approachable chunks in Zarr output.

Authors: __James McCreight (NCAR), Ishita Srivastava (NCAR), and Rich Signell (USGS)__


## Overview
The National Water Model (NWM) version 2.1 retrospective simulation spans 42-years (Feb 1979 - Dec 2020). The model
domain is the continential US. Inputs are hourly and outputs are provided at hourly or 3-hourly resolution (more details
provide below and in [this document](https://drive.google.com/file/d/1zUtBZ_SM7uHqNDHLdOwGvfasVFMHfH6a/view)).

The model writes separate files at each output time. Within those individual files the data are not chunked 
in space. In the use case of opening a full timeseries at a single point or a sub-region, the user would be required to 
read in the entire data set: a very inefficient data access pattern for a very common use case. 

Enter rechunking. The goal of rechunking this model dataset is to provide chunks (data pieces partitioning the dimnensions of
of the data) that support efficient data access for most use cases. In the case that a specific, intensive use case would benefit
from a different chunk scheme, these datasets can be rechunked to accomodate that pattern. 

Examples of use cases will be supplied below, including re-rechunking.


## Data overview
Six separate zarr stores have been created, corresponding closely to the model output files, and their time resolution is noted

* gwout: Output from the groundwater model (hourly)
* chrtout: Output from the streamflow model(hourly)
* lakeout: Output from the lake model (hourly)
* ldasout: Output from the NoahMP land surface model (3-hourly)
* rtout: Output from the overland and subsurface terrain routing model (3-hourly)
* precip: Input precipitation fields from the OWP AORC forcing data set (hourly)

Additonal detail on these stores (variables contained and space-time information) is provided in the data description section 
below and via accompanying notebooks.


## Data Access

The data are currently pending delivery to AWS cloud as are further details here.

For those with access to NCAR computing resources, these can alternatively be found at the following paths:
```
/glade/p/datashare/ishitas/nwm_retro_v2.1/gwout.zarr
/glade/p/datashare/jamesmcc/nwm_retro_v2.1/lakeout.zarr
/glade/p/datashare/ishitas/nwm_retro_v2.1/chrtout.zarr
/glade/p/datashare/jamesmcc/nwm_retro_v2.1/precip.zarr
/glade/p/datashare/ishitas/nwm_retro_v2.1/ldasout.zarr
/glade/p/datashare/jamesmcc/nwm_retro_v2.1/rtout.zarr
```


## Data Description

Data as accessed by `xarray.open_zarr` can be found in the accompanying notebook
[(html)](https://htmlpreview.github.io/?https://github.com/NCAR/rechunk\_retro_nwm\_v21/blob/main/notebooks/data\_description.html) 
[(jupyter\_notebook)](https://github.com/NCAR/rechunk_retro_nwm_v21/blob/main/notebooks/data_description.ipynb). This includes
metadata, chunking schemes, and data types for all variables and coordinates. 

Further details about the Zarr stores are provided in this accompanying notebook 
[(html)](https://htmlpreview.github.io/?https://github.com/NCAR/rechunk_retro_nwm_v21/blob/main/notebooks/data_description_detail.html) 
[(jupyter notebook)](https://github.com/NCAR/rechunk_retro_nwm_v21/blob/main/notebooks/data_description_detail.ipynb)
which contains the xarray dataset reports and also xarray and Zarr details for each variable showing storage data types, levels of 
compression and other details. Note that the difference in the data types between xarray and zarr result from the use of scale\_factor 
and add\_offset metadata in the underlying Zarr data set which xarray uses to recover floating point variables from the stored 
integers. 


## Use Cases

* Example of retrieving and plotting a single timeserires from the chrtout store
[(html)](https://htmlpreview.github.io/?https://github.com/NCAR/rechunk_retro_nwm_v21/blob/main/notebooks/usage_example_streamflow_timeseries.html) 
[(jupyter notebook)](https://github.com/NCAR/rechunk_retro_nwm_v21/blob/main/notebooks/usage_example_streamflow_timeseries.ipynb)

* Example of subsetting and rechunking the store to optimize data access pattern: selecting only streamflow gages from chrtout
[(html)](https://htmlpreview.github.io/?https://github.com/NCAR/rechunk_retro_nwm_v21/blob/main/notebooks/usage_example_rerechunk_chrtout.html) 
[(jupyter notebook)](https://github.com/NCAR/rechunk_retro_nwm_v21/blob/main/notebooks/usage_example_rerechunk_chrtout.ipynb)


## Code overview
An overview of the code used can be found in [README_code.md](README_code.md).
