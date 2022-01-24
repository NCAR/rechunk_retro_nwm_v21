# Rechunking National Water Model v2.1 retrospective simulations to more (cloud-)approachable chunks in Zarr format.
Authors: _James McCreight (NCAR), Ishita Srivastava (NCAR), Rich Signell (USGS), and Yongxin Zhang (NCAR)_


## Overview
The National Water Model (NWM) version 2.1 retrospective simulation spans 42-years (Feb 1979 - Dec 2020). The model
domain is the continential US. Inputs are hourly and outputs are provided at hourly or 3-hourly resolution. Additional details
are provided below and in this
[retrospective overview document](https://github.com/NCAR/rechunk_retro_nwm_v21/blob/main/ancillary/NWMv2.1_42YrRetrospective_OutputVarsFullPhysicsRun.pdf).

The model writes separate files at each output time. Within those individual files the data are not chunked 
in space. In the use case of opening a full timeseries at a single point or a sub-region, the user would be required to 
read in the entire data set: a very inefficient data access pattern for a very common use case. 

Enter rechunking. The goal of rechunking this model dataset is to provide chunks (data pieces partitioning the dimnensions of
of the data) that support efficient data access for most use cases. When a specific, intensive use case would benefit
from a different chunk scheme than that provided, the provided datasets can be rechunked to accomodate that pattern. 
Examples of use cases are supplied, including re-rechunking.


## Data overview
Six separate zarr stores have been created, corresponding closely to the model output files. The time resolution is noted for each product. 

* lakeout: Output from the lake model (hourly, 5.5GB)
* gwout: Output from the groundwater model (hourly, 1.7TB)
* chrtout: Output from the streamflow model(hourly, 1.4TB)
* precip: Input precipitation fields from the OWP AORC forcing data set (hourly, 2.0TB)
* ldasout: Output from the NoahMP land surface model (3-hourly, pending)
* rtout: Output from the overland and subsurface terrain routing model (3-hourly, pending)


Additonal detail on these stores (variables contained and space-time information) is provided in the data description section 
below and via accompanying notebooks.


## Data Access

[Cloud on AWS]
[Landing page](https://registry.opendata.aws/nwm-archive/)  
[NWM v2.1 Zarr Bucket](https://noaa-nwm-retrospective-2-1-zarr-pds.s3.amazonaws.com/index.html)  

For those with access to NCAR computing resources, these can alternatively be found at the following paths:
```
/glade/campaign/ncar/USGS_Water/NWMV21_retro_zarr/lakeout.zarr
/glade/campaign/ncar/USGS_Water/NWMV21_retro_zarr/gwout.zarr
/glade/campaign/ncar/USGS_Water/NWMV21_retro_zarr/chrtout.zarr
/glade/campaign/ncar/USGS_Water/NWMV21_retro_zarr/precip.zarr
/glade/campaign/ncar/USGS_Water/NWMV21_retro_zarr/ldasout.zarr
/glade/campaign/ncar/USGS_Water/NWMV21_retro_zarr/rtout.zarr
```


## Data Description

Data as accessed by `xarray.open_zarr` can be found in the accompanying notebook
[(html)](https://nbviewer.org/github/NCAR/rechunk\_retro_nwm\_v21/blob/main/notebooks/data\_description.ipynb) 
[(jupyter\_notebook)](https://github.com/NCAR/rechunk_retro_nwm_v21/blob/main/notebooks/data_description.ipynb). This includes
metadata, chunking schemes, and data types for all variables and coordinates. 

Further details in this accompanying notebook 
[(html)](https://nbviewer.org/github/NCAR/rechunk_retro_nwm_v21/blob/main/notebooks/data_description_detail.ipynb) 
[(jupyter notebook)](https://github.com/NCAR/rechunk_retro_nwm_v21/blob/main/notebooks/data_description_detail.ipynb)
including the xarray dataset reports and also xarray and Zarr details for each variable showing storage data types, levels of 
compression and other information. Note that the difference in the data types between xarray and zarr result from the use of scale\_factor 
and add\_offset metadata in the underlying Zarr data set which xarray uses to recover floating point variables from the stored 
integers. 


## Use Cases

* Example of retrieving and plotting a single timeserires from the chrtout store
[(html)](https://nbviewer.org/github/NCAR/rechunk_retro_nwm_v21/blob/main/notebooks/usage_example_streamflow_timeseries.ipynb) 
[(jupyter notebook)](https://github.com/NCAR/rechunk_retro_nwm_v21/blob/main/notebooks/usage_example_streamflow_timeseries.ipynb)

* Example of subsetting and rechunking the store to optimize data access pattern: selecting only streamflow gages from chrtout
[(html)](https://nbviewer.org/github/NCAR/rechunk_retro_nwm_v21/blob/main/notebooks/usage_example_rerechunk_chrtout.ipynb) 
[(jupyter notebook)](https://github.com/NCAR/rechunk_retro_nwm_v21/blob/main/notebooks/usage_example_rerechunk_chrtout.ipynb)


## Code overview
An overview of the code used can be found in [README_code.md](README_code.md).
