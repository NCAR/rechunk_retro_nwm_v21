import numpy as np
import xarray as xr
import pandas as pd
from dask.distributed import Client, progress, LocalCluster, performance_report
from dask_jobqueue import PBSCluster
import zarr
import time
import shutil
from rechunker import rechunk
import os, sys
import dask
import socket



def main():

    #Read from lock file:

    start_date = "1986-10-30 03:00"
    end_date  =  "1986-11-27 00:00"
    file_rechunked = "/glade/p/datashare/ishitas/ldasout/ldasout.zarr"
    os.remove('/glade/p/datashare/ishitas/ldasout/ldasout_write_in_progress.lock') 
    file_chunk_fix = file_rechunked.replace(".zarr", "_fix.zarr")
    script_path = '/glade/work/ishitas/zarr_retrospective/rechunk_retro_nwm_v21/ldasout/ldasout_to_zarr_fix.py' 
    
    cmd = 'python %s "%s" "%s" "%s"' %(script_path, start_date, end_date, file_chunk_fix)
    print("Running %s" %cmd)
    ret = os.system(cmd)
    if(ret != 0):
        print("Fix script didnt execute successfully")
        sys.exit()
    
    cluster = PBSCluster(cores=2, memory='20GB',queue='casper', project='NRAL0017')
    cluster.scale(8)
    client = Client(cluster)
    time.sleep(60)
    print(client)

    # read structure of dataset to see what's on disk
    ds_ondisk = xr.open_zarr(str(file_rechunked), consolidated=True)
    ds_B = xr.open_zarr(str(file_chunk_fix), consolidated=True)

    # get index of first new datapoint
     
    print(ds_ondisk.time.size)
    start_ix, = np.nonzero(np.isin(ds_B.time, ds_ondisk.time))
    #print(start_ix)
    # region of new data
    region_new = slice(start_ix[0], ds_B.time.size)
    #print(region_new)
        
    # get updated dataset size and create slice
    region_update = slice(ds_ondisk.time.size - int(ds_B.time.size), ds_ondisk.time.size)
    print(region_update)
    print(len(ds_B['time'].values))
    #print(ds_ondisk.time.size - int(ds_B.time.size))
    
    # write new data to zarr (all the coordinates except time needs to be dropped)
   
    ds_B.drop('x').drop('y').to_zarr(file_rechunked, region={"time": region_update})

    # produces
    ds = xr.open_zarr(file_rechunked)
    print(ds)
        
if __name__ == '__main__':
    main()
