# nwm_v21_retro_rechunk
Rechunking NWM v2.1 retrospective runs to more approachable chunks in Zarr output.

Authors: __James McCreight (NCAR), Ishita Srivastava (NCAR), and Rich Signell (USGS)__


## Overview
The National Water Model (NWM) version 2.1 retrospective simulation spans 42-years (Feb 1979 - Dec 2020). The model
domain is the continential US. Inputs are hourly and outputs are provided at hourly or 3-hourly resolution (more details
provide below and in [this document](https://drive.google.com/file/d/1zUtBZ_SM7uHqNDHLdOwGvfasVFMHfH6a/view).


The model writes output to files at each output time separately. Within those individual files the data are not chunked 
in space. For the use case of opening a full timeseries at a single point, the user would be required to read in the entire data
set. This is a very inefficient data access pattern for a very common use case. 

Enter rechunking. The goal of rechunking this dataset is to provide chunks (data pieces partitioning the dimnensions of
of the data) that support efficient data access for most use cases. 


## Data overview
Six separate zarr stores have been created, corresponding closely to the model output files, and their time resolution is noted

* chrtout: Output from the streamflow model(hourly)
* gwout: Output from the groundwater model (hourly)
* lakeout: Output from the lake model (hourly)
* ldasout: Output from the NoahMP land surface model (3-hourly)
* rtout: Output from the overland and subsurface terrain routing model (3-hourly)
* precip: Input precipitation fields from the OWP AORC forcing data set (hourly)

Additonal detail on these stores (variables contained and space-time information) is provided in the data description section 
below and via accompanying notebooks.


## Data Access

The data are currently accessible via globus but will be moved to AWS cloud. Please see
https://www2.cisl.ucar.edu/resources/storage-and-file-systems/using-the-ncar-data-sharing-service#retrieve
for details on accesing these globus data shares and let us know if permission errors arise. The following 
links will open the end points in the globus web browser app

[James' globus end point "nwm\_retro\_v2.1" (lakeout, rtout, and precip)](https://app.globus.org/file-manager?origin_id=a70eef1a-a2d3-11eb-92d2-6b08dd67ff48&origin_path=%2F). 
[Ishita's globus end point "nwmretrov2.1\_ishitas" (gwout, chrtout, and ldasout)](https://app.globus.org/file-manager?origin_id=b4122504-22f2-11ec-a47d-a50ad076c282&origin_path=%2F). 

These can alternatively be found on the NCAR casper cluster (for those with access) at the following paths:
```
/glade/p/datashare/ishitas/nwm_retro_v2.1/gwout.zarr
/glade/p/datashare/jamesmcc/nwm_retro_v2.1/lakeout.zarr
/glade/p/datashare/ishitas/nwm_retro_v2.1/chrtout.zarr
/glade/p/datashare/jamesmcc/nwm_retro_v2.1/precip.zarr
/glade/p/datashare/ishitas/nwm_retro_v2.1/ldasout.zarr
/glade/p/datashare/jamesmcc/nwm_retro_v2.1/rtout.zarr
```

## Data Description
The [accompanying notebook](data_description.ipynb) gives a detailed overview of the datasets using the xarray. 

## Use Cases
The 
