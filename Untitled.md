```python
import warnings
warnings.catch_warnings()
import xarray as xr
```

    /glade/work/jamesmcc/python_envs/379zr/lib/python3.7/site-packages/xarray/backends/cfgrib_.py:28: UserWarning: Failed to load cfgrib - most likely there is a problem accessing the ecCodes library. Try `import cfgrib` to get the full error message
      "Failed to load cfgrib - most likely there is a problem accessing the ecCodes library. "



```python
files = {
    'gwout': '/glade/p/datashare/ishitas/nwm_retro_v2.1/gwout.zarr',
    'lakeout': '/glade/p/datashare/jamesmcc/nwm_retro_v2.1/lakeout.zarr',
    'chrtout': '/glade/p/datashare/ishitas/nwm_retro_v2.1/chrtout.zarr',
    'precip': '/glade/p/datashare/jamesmcc/nwm_retro_v2.1/precip.zarr',
    'ldasout': '/glade/p/datashare/ishitas/nwm_retro_v2.1/ldasout.zarr',
    'rtout': '/glade/p/datashare/jamesmcc/nwm_retro_v2.1/rtout.zarr', }
message = ('Please click on the dropdown carets, metadata (file) symbols, and the data' 
           'information (silos) symbols below for additional information.')
```


```python

```

# LAKEOUT



```python
lakeout_ds = xr.open_zarr(files['lakeout'])
print(message)
display(lakeout_ds)
```

    Please click on the dropdown carets, metadata (file) symbols, and the datainformation (silos) symbols below for additional information.



<div><svg style="position: absolute; width: 0; height: 0; overflow: hidden">
<defs>
<symbol id="icon-database" viewBox="0 0 32 32">
<path d="M16 0c-8.837 0-16 2.239-16 5v4c0 2.761 7.163 5 16 5s16-2.239 16-5v-4c0-2.761-7.163-5-16-5z"></path>
<path d="M16 17c-8.837 0-16-2.239-16-5v6c0 2.761 7.163 5 16 5s16-2.239 16-5v-6c0 2.761-7.163 5-16 5z"></path>
<path d="M16 26c-8.837 0-16-2.239-16-5v6c0 2.761 7.163 5 16 5s16-2.239 16-5v-6c0 2.761-7.163 5-16 5z"></path>
</symbol>
<symbol id="icon-file-text2" viewBox="0 0 32 32">
<path d="M28.681 7.159c-0.694-0.947-1.662-2.053-2.724-3.116s-2.169-2.030-3.116-2.724c-1.612-1.182-2.393-1.319-2.841-1.319h-15.5c-1.378 0-2.5 1.121-2.5 2.5v27c0 1.378 1.122 2.5 2.5 2.5h23c1.378 0 2.5-1.122 2.5-2.5v-19.5c0-0.448-0.137-1.23-1.319-2.841zM24.543 5.457c0.959 0.959 1.712 1.825 2.268 2.543h-4.811v-4.811c0.718 0.556 1.584 1.309 2.543 2.268zM28 29.5c0 0.271-0.229 0.5-0.5 0.5h-23c-0.271 0-0.5-0.229-0.5-0.5v-27c0-0.271 0.229-0.5 0.5-0.5 0 0 15.499-0 15.5 0v7c0 0.552 0.448 1 1 1h7v19.5z"></path>
<path d="M23 26h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
<path d="M23 22h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
<path d="M23 18h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
</symbol>
</defs>
</svg>
<style>/* CSS stylesheet for displaying xarray objects in jupyterlab.
 *
 */

:root {
  --xr-font-color0: var(--jp-content-font-color0, rgba(0, 0, 0, 1));
  --xr-font-color2: var(--jp-content-font-color2, rgba(0, 0, 0, 0.54));
  --xr-font-color3: var(--jp-content-font-color3, rgba(0, 0, 0, 0.38));
  --xr-border-color: var(--jp-border-color2, #e0e0e0);
  --xr-disabled-color: var(--jp-layout-color3, #bdbdbd);
  --xr-background-color: var(--jp-layout-color0, white);
  --xr-background-color-row-even: var(--jp-layout-color1, white);
  --xr-background-color-row-odd: var(--jp-layout-color2, #eeeeee);
}

html[theme=dark],
body.vscode-dark {
  --xr-font-color0: rgba(255, 255, 255, 1);
  --xr-font-color2: rgba(255, 255, 255, 0.54);
  --xr-font-color3: rgba(255, 255, 255, 0.38);
  --xr-border-color: #1F1F1F;
  --xr-disabled-color: #515151;
  --xr-background-color: #111111;
  --xr-background-color-row-even: #111111;
  --xr-background-color-row-odd: #313131;
}

.xr-wrap {
  display: block;
  min-width: 300px;
  max-width: 700px;
}

.xr-text-repr-fallback {
  /* fallback to plain text repr when CSS is not injected (untrusted notebook) */
  display: none;
}

.xr-header {
  padding-top: 6px;
  padding-bottom: 6px;
  margin-bottom: 4px;
  border-bottom: solid 1px var(--xr-border-color);
}

.xr-header > div,
.xr-header > ul {
  display: inline;
  margin-top: 0;
  margin-bottom: 0;
}

.xr-obj-type,
.xr-array-name {
  margin-left: 2px;
  margin-right: 10px;
}

.xr-obj-type {
  color: var(--xr-font-color2);
}

.xr-sections {
  padding-left: 0 !important;
  display: grid;
  grid-template-columns: 150px auto auto 1fr 20px 20px;
}

.xr-section-item {
  display: contents;
}

.xr-section-item input {
  display: none;
}

.xr-section-item input + label {
  color: var(--xr-disabled-color);
}

.xr-section-item input:enabled + label {
  cursor: pointer;
  color: var(--xr-font-color2);
}

.xr-section-item input:enabled + label:hover {
  color: var(--xr-font-color0);
}

.xr-section-summary {
  grid-column: 1;
  color: var(--xr-font-color2);
  font-weight: 500;
}

.xr-section-summary > span {
  display: inline-block;
  padding-left: 0.5em;
}

.xr-section-summary-in:disabled + label {
  color: var(--xr-font-color2);
}

.xr-section-summary-in + label:before {
  display: inline-block;
  content: '►';
  font-size: 11px;
  width: 15px;
  text-align: center;
}

.xr-section-summary-in:disabled + label:before {
  color: var(--xr-disabled-color);
}

.xr-section-summary-in:checked + label:before {
  content: '▼';
}

.xr-section-summary-in:checked + label > span {
  display: none;
}

.xr-section-summary,
.xr-section-inline-details {
  padding-top: 4px;
  padding-bottom: 4px;
}

.xr-section-inline-details {
  grid-column: 2 / -1;
}

.xr-section-details {
  display: none;
  grid-column: 1 / -1;
  margin-bottom: 5px;
}

.xr-section-summary-in:checked ~ .xr-section-details {
  display: contents;
}

.xr-array-wrap {
  grid-column: 1 / -1;
  display: grid;
  grid-template-columns: 20px auto;
}

.xr-array-wrap > label {
  grid-column: 1;
  vertical-align: top;
}

.xr-preview {
  color: var(--xr-font-color3);
}

.xr-array-preview,
.xr-array-data {
  padding: 0 5px !important;
  grid-column: 2;
}

.xr-array-data,
.xr-array-in:checked ~ .xr-array-preview {
  display: none;
}

.xr-array-in:checked ~ .xr-array-data,
.xr-array-preview {
  display: inline-block;
}

.xr-dim-list {
  display: inline-block !important;
  list-style: none;
  padding: 0 !important;
  margin: 0;
}

.xr-dim-list li {
  display: inline-block;
  padding: 0;
  margin: 0;
}

.xr-dim-list:before {
  content: '(';
}

.xr-dim-list:after {
  content: ')';
}

.xr-dim-list li:not(:last-child):after {
  content: ',';
  padding-right: 5px;
}

.xr-has-index {
  font-weight: bold;
}

.xr-var-list,
.xr-var-item {
  display: contents;
}

.xr-var-item > div,
.xr-var-item label,
.xr-var-item > .xr-var-name span {
  background-color: var(--xr-background-color-row-even);
  margin-bottom: 0;
}

.xr-var-item > .xr-var-name:hover span {
  padding-right: 5px;
}

.xr-var-list > li:nth-child(odd) > div,
.xr-var-list > li:nth-child(odd) > label,
.xr-var-list > li:nth-child(odd) > .xr-var-name span {
  background-color: var(--xr-background-color-row-odd);
}

.xr-var-name {
  grid-column: 1;
}

.xr-var-dims {
  grid-column: 2;
}

.xr-var-dtype {
  grid-column: 3;
  text-align: right;
  color: var(--xr-font-color2);
}

.xr-var-preview {
  grid-column: 4;
}

.xr-var-name,
.xr-var-dims,
.xr-var-dtype,
.xr-preview,
.xr-attrs dt {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  padding-right: 10px;
}

.xr-var-name:hover,
.xr-var-dims:hover,
.xr-var-dtype:hover,
.xr-attrs dt:hover {
  overflow: visible;
  width: auto;
  z-index: 1;
}

.xr-var-attrs,
.xr-var-data {
  display: none;
  background-color: var(--xr-background-color) !important;
  padding-bottom: 5px !important;
}

.xr-var-attrs-in:checked ~ .xr-var-attrs,
.xr-var-data-in:checked ~ .xr-var-data {
  display: block;
}

.xr-var-data > table {
  float: right;
}

.xr-var-name span,
.xr-var-data,
.xr-attrs {
  padding-left: 25px !important;
}

.xr-attrs,
.xr-var-attrs,
.xr-var-data {
  grid-column: 1 / -1;
}

dl.xr-attrs {
  padding: 0;
  margin: 0;
  display: grid;
  grid-template-columns: 125px auto;
}

.xr-attrs dt,
.xr-attrs dd {
  padding: 0;
  margin: 0;
  float: left;
  padding-right: 10px;
  width: auto;
}

.xr-attrs dt {
  font-weight: normal;
  grid-column: 1;
}

.xr-attrs dt:hover span {
  display: inline-block;
  background: var(--xr-background-color);
  padding-right: 10px;
}

.xr-attrs dd {
  grid-column: 2;
  white-space: pre-wrap;
  word-break: break-all;
}

.xr-icon-database,
.xr-icon-file-text2 {
  display: inline-block;
  vertical-align: middle;
  width: 1em;
  height: 1.5em !important;
  stroke-width: 0;
  stroke: currentColor;
  fill: currentColor;
}
</style><pre class='xr-text-repr-fallback'>&lt;xarray.Dataset&gt;
Dimensions:         (feature_id: 5783, time: 367439)
Coordinates:
  * feature_id      (feature_id) int32 491 531 747 ... 947070204 1021092845
    latitude        (feature_id) float32 dask.array&lt;chunksize=(5783,), meta=np.ndarray&gt;
    longitude       (feature_id) float32 dask.array&lt;chunksize=(5783,), meta=np.ndarray&gt;
  * time            (time) datetime64[ns] 1979-02-01T01:00:00 ... 2020-12-31T...
Data variables:
    crs             |S1 ...
    inflow          (time, feature_id) float64 dask.array&lt;chunksize=(8064, 500), meta=np.ndarray&gt;
    outflow         (time, feature_id) float64 dask.array&lt;chunksize=(8064, 500), meta=np.ndarray&gt;
    water_sfc_elev  (time, feature_id) float32 dask.array&lt;chunksize=(8064, 500), meta=np.ndarray&gt;
Attributes:
    Conventions:                  CF-1.6
    TITLE:                        OUTPUT FROM WRF-Hydro v5.2.0-beta2
    code_version:                 v5.2.0-beta2
    featureType:                  timeSeries
    model_configuration:          retrospective
    model_output_type:            reservoir
    proj4:                        +proj=lcc +units=m +a=6370000.0 +b=6370000....
    reservoir_assimilated_value:  Assimilation not performed
    reservoir_type:               1 = level pool everywhere
    station_dimension:            lake_id</pre><div class='xr-wrap' hidden><div class='xr-header'><div class='xr-obj-type'>xarray.Dataset</div></div><ul class='xr-sections'><li class='xr-section-item'><input id='section-e7d19054-39a7-410b-9e62-5eac09826dbd' class='xr-section-summary-in' type='checkbox' disabled ><label for='section-e7d19054-39a7-410b-9e62-5eac09826dbd' class='xr-section-summary'  title='Expand/collapse section'>Dimensions:</label><div class='xr-section-inline-details'><ul class='xr-dim-list'><li><span class='xr-has-index'>feature_id</span>: 5783</li><li><span class='xr-has-index'>time</span>: 367439</li></ul></div><div class='xr-section-details'></div></li><li class='xr-section-item'><input id='section-71feaf83-deca-4e92-9e09-3f33d9270109' class='xr-section-summary-in' type='checkbox'  checked><label for='section-71feaf83-deca-4e92-9e09-3f33d9270109' class='xr-section-summary' >Coordinates: <span>(4)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>feature_id</span></div><div class='xr-var-dims'>(feature_id)</div><div class='xr-var-dtype'>int32</div><div class='xr-var-preview xr-preview'>491 531 ... 947070204 1021092845</div><input id='attrs-b9e9d5e3-0233-41b9-8402-da978e46bf7f' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-b9e9d5e3-0233-41b9-8402-da978e46bf7f' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-024fd90b-ce56-4db1-a654-186df1262cbb' class='xr-var-data-in' type='checkbox'><label for='data-024fd90b-ce56-4db1-a654-186df1262cbb' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>cf_role :</span></dt><dd>timeseries_id</dd><dt><span>comment :</span></dt><dd>ComID from NHDPlusV2 waterbody layer</dd><dt><span>long_name :</span></dt><dd>Lake ComID</dd></dl></div><div class='xr-var-data'><pre>array([       491,        531,        747, ...,  947070203,  947070204,
       1021092845], dtype=int32)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>latitude</span></div><div class='xr-var-dims'>(feature_id)</div><div class='xr-var-dtype'>float32</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(5783,), meta=np.ndarray&gt;</div><input id='attrs-cacf68c3-c926-40d7-a8ef-ebed91599a5f' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-cacf68c3-c926-40d7-a8ef-ebed91599a5f' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-c786f829-a8b4-466c-898b-e738bb8a08da' class='xr-var-data-in' type='checkbox'><label for='data-c786f829-a8b4-466c-898b-e738bb8a08da' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Lake latitude</dd><dt><span>standard_name :</span></dt><dd>latitude</dd><dt><span>units :</span></dt><dd>degrees_north</dd></dl></div><div class='xr-var-data'><table>
    <tr>
        <td>
            <table>
                <thead>
                    <tr>
                        <td> </td>
                        <th> Array </th>
                        <th> Chunk </th>
                    </tr>
                </thead>
                <tbody>

                    <tr>
                        <th> Bytes </th>
                        <td> 22.59 kiB </td>
                        <td> 22.59 kiB </td>
                    </tr>

                    <tr>
                        <th> Shape </th>
                        <td> (5783,) </td>
                        <td> (5783,) </td>
                    </tr>
                    <tr>
                        <th> Count </th>
                        <td> 2 Tasks </td>
                        <td> 1 Chunks </td>
                    </tr>
                    <tr>
                    <th> Type </th>
                    <td> float32 </td>
                    <td> numpy.ndarray </td>
                    </tr>
                </tbody>
            </table>
        </td>
        <td>
        <svg width="170" height="75" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="0" y1="0" x2="120" y2="0" style="stroke-width:2" />
  <line x1="0" y1="25" x2="120" y2="25" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="0" y1="0" x2="0" y2="25" style="stroke-width:2" />
  <line x1="120" y1="0" x2="120" y2="25" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="0.0,0.0 120.0,0.0 120.0,25.412616514582485 0.0,25.412616514582485" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="60.000000" y="45.412617" font-size="1.0rem" font-weight="100" text-anchor="middle" >5783</text>
  <text x="140.000000" y="12.706308" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(0,140.000000,12.706308)">1</text>
</svg>
        </td>
    </tr>
</table></div></li><li class='xr-var-item'><div class='xr-var-name'><span>longitude</span></div><div class='xr-var-dims'>(feature_id)</div><div class='xr-var-dtype'>float32</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(5783,), meta=np.ndarray&gt;</div><input id='attrs-735ab436-de3b-464c-b4a4-53910ce0e930' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-735ab436-de3b-464c-b4a4-53910ce0e930' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-234e2423-4bd0-4e37-abbf-af1f602c6eaf' class='xr-var-data-in' type='checkbox'><label for='data-234e2423-4bd0-4e37-abbf-af1f602c6eaf' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Lake longitude</dd><dt><span>standard_name :</span></dt><dd>longitude</dd><dt><span>units :</span></dt><dd>degrees_east</dd></dl></div><div class='xr-var-data'><table>
    <tr>
        <td>
            <table>
                <thead>
                    <tr>
                        <td> </td>
                        <th> Array </th>
                        <th> Chunk </th>
                    </tr>
                </thead>
                <tbody>

                    <tr>
                        <th> Bytes </th>
                        <td> 22.59 kiB </td>
                        <td> 22.59 kiB </td>
                    </tr>

                    <tr>
                        <th> Shape </th>
                        <td> (5783,) </td>
                        <td> (5783,) </td>
                    </tr>
                    <tr>
                        <th> Count </th>
                        <td> 2 Tasks </td>
                        <td> 1 Chunks </td>
                    </tr>
                    <tr>
                    <th> Type </th>
                    <td> float32 </td>
                    <td> numpy.ndarray </td>
                    </tr>
                </tbody>
            </table>
        </td>
        <td>
        <svg width="170" height="75" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="0" y1="0" x2="120" y2="0" style="stroke-width:2" />
  <line x1="0" y1="25" x2="120" y2="25" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="0" y1="0" x2="0" y2="25" style="stroke-width:2" />
  <line x1="120" y1="0" x2="120" y2="25" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="0.0,0.0 120.0,0.0 120.0,25.412616514582485 0.0,25.412616514582485" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="60.000000" y="45.412617" font-size="1.0rem" font-weight="100" text-anchor="middle" >5783</text>
  <text x="140.000000" y="12.706308" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(0,140.000000,12.706308)">1</text>
</svg>
        </td>
    </tr>
</table></div></li><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>time</span></div><div class='xr-var-dims'>(time)</div><div class='xr-var-dtype'>datetime64[ns]</div><div class='xr-var-preview xr-preview'>1979-02-01T01:00:00 ... 2020-12-...</div><input id='attrs-78e7d20c-f191-4403-b6ce-36999eeb90ca' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-78e7d20c-f191-4403-b6ce-36999eeb90ca' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-bb0f5415-774b-42ef-b71c-8909640ec358' class='xr-var-data-in' type='checkbox'><label for='data-bb0f5415-774b-42ef-b71c-8909640ec358' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>valid output time</dd><dt><span>standard_name :</span></dt><dd>time</dd><dt><span>valid_max :</span></dt><dd>4862880</dd><dt><span>valid_min :</span></dt><dd>4777980</dd></dl></div><div class='xr-var-data'><pre>array([&#x27;1979-02-01T01:00:00.000000000&#x27;, &#x27;1979-02-01T02:00:00.000000000&#x27;,
       &#x27;1979-02-01T03:00:00.000000000&#x27;, ..., &#x27;2020-12-31T21:00:00.000000000&#x27;,
       &#x27;2020-12-31T22:00:00.000000000&#x27;, &#x27;2020-12-31T23:00:00.000000000&#x27;],
      dtype=&#x27;datetime64[ns]&#x27;)</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-45120542-ce0d-4ecb-a78c-d72e7296a55c' class='xr-section-summary-in' type='checkbox'  checked><label for='section-45120542-ce0d-4ecb-a78c-d72e7296a55c' class='xr-section-summary' >Data variables: <span>(4)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-var-name'><span>crs</span></div><div class='xr-var-dims'>()</div><div class='xr-var-dtype'>|S1</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-31db4c6f-30d6-48ed-895e-3f8dd24d67cc' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-31db4c6f-30d6-48ed-895e-3f8dd24d67cc' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-0373539d-5e12-4f70-8e31-eb258e06278d' class='xr-var-data-in' type='checkbox'><label for='data-0373539d-5e12-4f70-8e31-eb258e06278d' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>_CoordinateAxes :</span></dt><dd>latitude longitude</dd><dt><span>esri_pe_string :</span></dt><dd>GEOGCS[&quot;GCS_WGS_1984&quot;,DATUM[&quot;D_WGS_1984&quot;,SPHEROID[&quot;WGS_1984&quot;,6378137.0,298.257223563]],PRIMEM[&quot;Greenwich&quot;,0.0],UNIT[&quot;Degree&quot;,0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision</dd><dt><span>grid_mapping_name :</span></dt><dd>latitude longitude</dd><dt><span>inverse_flattening :</span></dt><dd>298.2572326660156</dd><dt><span>long_name :</span></dt><dd>CRS definition</dd><dt><span>longitude_of_prime_meridian :</span></dt><dd>0.0</dd><dt><span>semi_major_axis :</span></dt><dd>6378137.0</dd><dt><span>semi_minor_axis :</span></dt><dd>6356752.5</dd><dt><span>spatial_ref :</span></dt><dd>GEOGCS[&quot;GCS_WGS_1984&quot;,DATUM[&quot;D_WGS_1984&quot;,SPHEROID[&quot;WGS_1984&quot;,6378137.0,298.257223563]],PRIMEM[&quot;Greenwich&quot;,0.0],UNIT[&quot;Degree&quot;,0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision</dd><dt><span>transform_name :</span></dt><dd>latitude longitude</dd></dl></div><div class='xr-var-data'><pre>array(b&#x27;&#x27;, dtype=&#x27;|S1&#x27;)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>inflow</span></div><div class='xr-var-dims'>(time, feature_id)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(8064, 500), meta=np.ndarray&gt;</div><input id='attrs-5158844b-0237-4012-887d-ee553781ef15' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-5158844b-0237-4012-887d-ee553781ef15' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-04110fea-77b0-4fa5-ade6-e62e73ba3db4' class='xr-var-data-in' type='checkbox'><label for='data-04110fea-77b0-4fa5-ade6-e62e73ba3db4' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>grid_mapping :</span></dt><dd>crs</dd><dt><span>long_name :</span></dt><dd>Lake Inflow</dd><dt><span>units :</span></dt><dd>m3 s-1</dd></dl></div><div class='xr-var-data'><table>
    <tr>
        <td>
            <table>
                <thead>
                    <tr>
                        <td> </td>
                        <th> Array </th>
                        <th> Chunk </th>
                    </tr>
                </thead>
                <tbody>

                    <tr>
                        <th> Bytes </th>
                        <td> 15.83 GiB </td>
                        <td> 30.76 MiB </td>
                    </tr>

                    <tr>
                        <th> Shape </th>
                        <td> (367439, 5783) </td>
                        <td> (8064, 500) </td>
                    </tr>
                    <tr>
                        <th> Count </th>
                        <td> 553 Tasks </td>
                        <td> 552 Chunks </td>
                    </tr>
                    <tr>
                    <th> Type </th>
                    <td> float64 </td>
                    <td> numpy.ndarray </td>
                    </tr>
                </tbody>
            </table>
        </td>
        <td>
        <svg width="77" height="170" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="0" y1="0" x2="27" y2="0" style="stroke-width:2" />
  <line x1="0" y1="5" x2="27" y2="5" />
  <line x1="0" y1="10" x2="27" y2="10" />
  <line x1="0" y1="18" x2="27" y2="18" />
  <line x1="0" y1="23" x2="27" y2="23" />
  <line x1="0" y1="31" x2="27" y2="31" />
  <line x1="0" y1="36" x2="27" y2="36" />
  <line x1="0" y1="42" x2="27" y2="42" />
  <line x1="0" y1="50" x2="27" y2="50" />
  <line x1="0" y1="55" x2="27" y2="55" />
  <line x1="0" y1="63" x2="27" y2="63" />
  <line x1="0" y1="68" x2="27" y2="68" />
  <line x1="0" y1="76" x2="27" y2="76" />
  <line x1="0" y1="81" x2="27" y2="81" />
  <line x1="0" y1="86" x2="27" y2="86" />
  <line x1="0" y1="94" x2="27" y2="94" />
  <line x1="0" y1="100" x2="27" y2="100" />
  <line x1="0" y1="107" x2="27" y2="107" />
  <line x1="0" y1="113" x2="27" y2="113" />
  <line x1="0" y1="120" x2="27" y2="120" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="0" y1="0" x2="0" y2="120" style="stroke-width:2" />
  <line x1="2" y1="0" x2="2" y2="120" />
  <line x1="4" y1="0" x2="4" y2="120" />
  <line x1="7" y1="0" x2="7" y2="120" />
  <line x1="9" y1="0" x2="9" y2="120" />
  <line x1="11" y1="0" x2="11" y2="120" />
  <line x1="14" y1="0" x2="14" y2="120" />
  <line x1="16" y1="0" x2="16" y2="120" />
  <line x1="19" y1="0" x2="19" y2="120" />
  <line x1="21" y1="0" x2="21" y2="120" />
  <line x1="23" y1="0" x2="23" y2="120" />
  <line x1="26" y1="0" x2="26" y2="120" />
  <line x1="27" y1="0" x2="27" y2="120" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="0.0,0.0 27.714173989998702,0.0 27.714173989998702,120.0 0.0,120.0" style="fill:#8B4903A0;stroke-width:0"/>

  <!-- Text -->
  <text x="13.857087" y="140.000000" font-size="1.0rem" font-weight="100" text-anchor="middle" >5783</text>
  <text x="47.714174" y="60.000000" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(-90,47.714174,60.000000)">367439</text>
</svg>
        </td>
    </tr>
</table></div></li><li class='xr-var-item'><div class='xr-var-name'><span>outflow</span></div><div class='xr-var-dims'>(time, feature_id)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(8064, 500), meta=np.ndarray&gt;</div><input id='attrs-16c95ab5-7056-4a88-a6a1-fb4b44ff67c8' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-16c95ab5-7056-4a88-a6a1-fb4b44ff67c8' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-1537841d-c123-4610-9e52-6749e3a02c02' class='xr-var-data-in' type='checkbox'><label for='data-1537841d-c123-4610-9e52-6749e3a02c02' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>grid_mapping :</span></dt><dd>crs</dd><dt><span>long_name :</span></dt><dd>Lake Outflow</dd><dt><span>units :</span></dt><dd>m3 s-1</dd></dl></div><div class='xr-var-data'><table>
    <tr>
        <td>
            <table>
                <thead>
                    <tr>
                        <td> </td>
                        <th> Array </th>
                        <th> Chunk </th>
                    </tr>
                </thead>
                <tbody>

                    <tr>
                        <th> Bytes </th>
                        <td> 15.83 GiB </td>
                        <td> 30.76 MiB </td>
                    </tr>

                    <tr>
                        <th> Shape </th>
                        <td> (367439, 5783) </td>
                        <td> (8064, 500) </td>
                    </tr>
                    <tr>
                        <th> Count </th>
                        <td> 553 Tasks </td>
                        <td> 552 Chunks </td>
                    </tr>
                    <tr>
                    <th> Type </th>
                    <td> float64 </td>
                    <td> numpy.ndarray </td>
                    </tr>
                </tbody>
            </table>
        </td>
        <td>
        <svg width="77" height="170" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="0" y1="0" x2="27" y2="0" style="stroke-width:2" />
  <line x1="0" y1="5" x2="27" y2="5" />
  <line x1="0" y1="10" x2="27" y2="10" />
  <line x1="0" y1="18" x2="27" y2="18" />
  <line x1="0" y1="23" x2="27" y2="23" />
  <line x1="0" y1="31" x2="27" y2="31" />
  <line x1="0" y1="36" x2="27" y2="36" />
  <line x1="0" y1="42" x2="27" y2="42" />
  <line x1="0" y1="50" x2="27" y2="50" />
  <line x1="0" y1="55" x2="27" y2="55" />
  <line x1="0" y1="63" x2="27" y2="63" />
  <line x1="0" y1="68" x2="27" y2="68" />
  <line x1="0" y1="76" x2="27" y2="76" />
  <line x1="0" y1="81" x2="27" y2="81" />
  <line x1="0" y1="86" x2="27" y2="86" />
  <line x1="0" y1="94" x2="27" y2="94" />
  <line x1="0" y1="100" x2="27" y2="100" />
  <line x1="0" y1="107" x2="27" y2="107" />
  <line x1="0" y1="113" x2="27" y2="113" />
  <line x1="0" y1="120" x2="27" y2="120" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="0" y1="0" x2="0" y2="120" style="stroke-width:2" />
  <line x1="2" y1="0" x2="2" y2="120" />
  <line x1="4" y1="0" x2="4" y2="120" />
  <line x1="7" y1="0" x2="7" y2="120" />
  <line x1="9" y1="0" x2="9" y2="120" />
  <line x1="11" y1="0" x2="11" y2="120" />
  <line x1="14" y1="0" x2="14" y2="120" />
  <line x1="16" y1="0" x2="16" y2="120" />
  <line x1="19" y1="0" x2="19" y2="120" />
  <line x1="21" y1="0" x2="21" y2="120" />
  <line x1="23" y1="0" x2="23" y2="120" />
  <line x1="26" y1="0" x2="26" y2="120" />
  <line x1="27" y1="0" x2="27" y2="120" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="0.0,0.0 27.714173989998702,0.0 27.714173989998702,120.0 0.0,120.0" style="fill:#8B4903A0;stroke-width:0"/>

  <!-- Text -->
  <text x="13.857087" y="140.000000" font-size="1.0rem" font-weight="100" text-anchor="middle" >5783</text>
  <text x="47.714174" y="60.000000" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(-90,47.714174,60.000000)">367439</text>
</svg>
        </td>
    </tr>
</table></div></li><li class='xr-var-item'><div class='xr-var-name'><span>water_sfc_elev</span></div><div class='xr-var-dims'>(time, feature_id)</div><div class='xr-var-dtype'>float32</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(8064, 500), meta=np.ndarray&gt;</div><input id='attrs-6d1683e3-1484-42f5-bb67-40e61dd3e368' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-6d1683e3-1484-42f5-bb67-40e61dd3e368' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-5b7b248e-1825-4592-849d-5720c5629fd7' class='xr-var-data-in' type='checkbox'><label for='data-5b7b248e-1825-4592-849d-5720c5629fd7' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>comment :</span></dt><dd>If reservoir_type = 4, water_sfc_elev is invalid because this value corresponds only to level pool</dd><dt><span>long_name :</span></dt><dd>Water Surface Elevation</dd><dt><span>units :</span></dt><dd>m</dd></dl></div><div class='xr-var-data'><table>
    <tr>
        <td>
            <table>
                <thead>
                    <tr>
                        <td> </td>
                        <th> Array </th>
                        <th> Chunk </th>
                    </tr>
                </thead>
                <tbody>

                    <tr>
                        <th> Bytes </th>
                        <td> 7.92 GiB </td>
                        <td> 15.38 MiB </td>
                    </tr>

                    <tr>
                        <th> Shape </th>
                        <td> (367439, 5783) </td>
                        <td> (8064, 500) </td>
                    </tr>
                    <tr>
                        <th> Count </th>
                        <td> 553 Tasks </td>
                        <td> 552 Chunks </td>
                    </tr>
                    <tr>
                    <th> Type </th>
                    <td> float32 </td>
                    <td> numpy.ndarray </td>
                    </tr>
                </tbody>
            </table>
        </td>
        <td>
        <svg width="77" height="170" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="0" y1="0" x2="27" y2="0" style="stroke-width:2" />
  <line x1="0" y1="5" x2="27" y2="5" />
  <line x1="0" y1="10" x2="27" y2="10" />
  <line x1="0" y1="18" x2="27" y2="18" />
  <line x1="0" y1="23" x2="27" y2="23" />
  <line x1="0" y1="31" x2="27" y2="31" />
  <line x1="0" y1="36" x2="27" y2="36" />
  <line x1="0" y1="42" x2="27" y2="42" />
  <line x1="0" y1="50" x2="27" y2="50" />
  <line x1="0" y1="55" x2="27" y2="55" />
  <line x1="0" y1="63" x2="27" y2="63" />
  <line x1="0" y1="68" x2="27" y2="68" />
  <line x1="0" y1="76" x2="27" y2="76" />
  <line x1="0" y1="81" x2="27" y2="81" />
  <line x1="0" y1="86" x2="27" y2="86" />
  <line x1="0" y1="94" x2="27" y2="94" />
  <line x1="0" y1="100" x2="27" y2="100" />
  <line x1="0" y1="107" x2="27" y2="107" />
  <line x1="0" y1="113" x2="27" y2="113" />
  <line x1="0" y1="120" x2="27" y2="120" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="0" y1="0" x2="0" y2="120" style="stroke-width:2" />
  <line x1="2" y1="0" x2="2" y2="120" />
  <line x1="4" y1="0" x2="4" y2="120" />
  <line x1="7" y1="0" x2="7" y2="120" />
  <line x1="9" y1="0" x2="9" y2="120" />
  <line x1="11" y1="0" x2="11" y2="120" />
  <line x1="14" y1="0" x2="14" y2="120" />
  <line x1="16" y1="0" x2="16" y2="120" />
  <line x1="19" y1="0" x2="19" y2="120" />
  <line x1="21" y1="0" x2="21" y2="120" />
  <line x1="23" y1="0" x2="23" y2="120" />
  <line x1="26" y1="0" x2="26" y2="120" />
  <line x1="27" y1="0" x2="27" y2="120" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="0.0,0.0 27.714173989998702,0.0 27.714173989998702,120.0 0.0,120.0" style="fill:#8B4903A0;stroke-width:0"/>

  <!-- Text -->
  <text x="13.857087" y="140.000000" font-size="1.0rem" font-weight="100" text-anchor="middle" >5783</text>
  <text x="47.714174" y="60.000000" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(-90,47.714174,60.000000)">367439</text>
</svg>
        </td>
    </tr>
</table></div></li></ul></div></li><li class='xr-section-item'><input id='section-b0bd6257-3927-4fd8-b5e4-39f8533a5621' class='xr-section-summary-in' type='checkbox'  ><label for='section-b0bd6257-3927-4fd8-b5e4-39f8533a5621' class='xr-section-summary' >Attributes: <span>(10)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><dl class='xr-attrs'><dt><span>Conventions :</span></dt><dd>CF-1.6</dd><dt><span>TITLE :</span></dt><dd>OUTPUT FROM WRF-Hydro v5.2.0-beta2</dd><dt><span>code_version :</span></dt><dd>v5.2.0-beta2</dd><dt><span>featureType :</span></dt><dd>timeSeries</dd><dt><span>model_configuration :</span></dt><dd>retrospective</dd><dt><span>model_output_type :</span></dt><dd>reservoir</dd><dt><span>proj4 :</span></dt><dd>+proj=lcc +units=m +a=6370000.0 +b=6370000.0 +lat_1=30.0 +lat_2=60.0 +lat_0=40.0 +lon_0=-97.0 +x_0=0 +y_0=0 +k_0=1.0 +nadgrids=@</dd><dt><span>reservoir_assimilated_value :</span></dt><dd>Assimilation not performed</dd><dt><span>reservoir_type :</span></dt><dd>1 = level pool everywhere</dd><dt><span>station_dimension :</span></dt><dd>lake_id</dd></dl></div></li></ul></div></div>


## GWOUT


```python
gwout_ds = xr.open_zarr(files['gwout'])
print(message)
display(gwout_ds)
```

    Please click on the dropdown carets, metadata (file) symbols, and the datainformation (silos) symbols below for additional information.



<div><svg style="position: absolute; width: 0; height: 0; overflow: hidden">
<defs>
<symbol id="icon-database" viewBox="0 0 32 32">
<path d="M16 0c-8.837 0-16 2.239-16 5v4c0 2.761 7.163 5 16 5s16-2.239 16-5v-4c0-2.761-7.163-5-16-5z"></path>
<path d="M16 17c-8.837 0-16-2.239-16-5v6c0 2.761 7.163 5 16 5s16-2.239 16-5v-6c0 2.761-7.163 5-16 5z"></path>
<path d="M16 26c-8.837 0-16-2.239-16-5v6c0 2.761 7.163 5 16 5s16-2.239 16-5v-6c0 2.761-7.163 5-16 5z"></path>
</symbol>
<symbol id="icon-file-text2" viewBox="0 0 32 32">
<path d="M28.681 7.159c-0.694-0.947-1.662-2.053-2.724-3.116s-2.169-2.030-3.116-2.724c-1.612-1.182-2.393-1.319-2.841-1.319h-15.5c-1.378 0-2.5 1.121-2.5 2.5v27c0 1.378 1.122 2.5 2.5 2.5h23c1.378 0 2.5-1.122 2.5-2.5v-19.5c0-0.448-0.137-1.23-1.319-2.841zM24.543 5.457c0.959 0.959 1.712 1.825 2.268 2.543h-4.811v-4.811c0.718 0.556 1.584 1.309 2.543 2.268zM28 29.5c0 0.271-0.229 0.5-0.5 0.5h-23c-0.271 0-0.5-0.229-0.5-0.5v-27c0-0.271 0.229-0.5 0.5-0.5 0 0 15.499-0 15.5 0v7c0 0.552 0.448 1 1 1h7v19.5z"></path>
<path d="M23 26h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
<path d="M23 22h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
<path d="M23 18h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
</symbol>
</defs>
</svg>
<style>/* CSS stylesheet for displaying xarray objects in jupyterlab.
 *
 */

:root {
  --xr-font-color0: var(--jp-content-font-color0, rgba(0, 0, 0, 1));
  --xr-font-color2: var(--jp-content-font-color2, rgba(0, 0, 0, 0.54));
  --xr-font-color3: var(--jp-content-font-color3, rgba(0, 0, 0, 0.38));
  --xr-border-color: var(--jp-border-color2, #e0e0e0);
  --xr-disabled-color: var(--jp-layout-color3, #bdbdbd);
  --xr-background-color: var(--jp-layout-color0, white);
  --xr-background-color-row-even: var(--jp-layout-color1, white);
  --xr-background-color-row-odd: var(--jp-layout-color2, #eeeeee);
}

html[theme=dark],
body.vscode-dark {
  --xr-font-color0: rgba(255, 255, 255, 1);
  --xr-font-color2: rgba(255, 255, 255, 0.54);
  --xr-font-color3: rgba(255, 255, 255, 0.38);
  --xr-border-color: #1F1F1F;
  --xr-disabled-color: #515151;
  --xr-background-color: #111111;
  --xr-background-color-row-even: #111111;
  --xr-background-color-row-odd: #313131;
}

.xr-wrap {
  display: block;
  min-width: 300px;
  max-width: 700px;
}

.xr-text-repr-fallback {
  /* fallback to plain text repr when CSS is not injected (untrusted notebook) */
  display: none;
}

.xr-header {
  padding-top: 6px;
  padding-bottom: 6px;
  margin-bottom: 4px;
  border-bottom: solid 1px var(--xr-border-color);
}

.xr-header > div,
.xr-header > ul {
  display: inline;
  margin-top: 0;
  margin-bottom: 0;
}

.xr-obj-type,
.xr-array-name {
  margin-left: 2px;
  margin-right: 10px;
}

.xr-obj-type {
  color: var(--xr-font-color2);
}

.xr-sections {
  padding-left: 0 !important;
  display: grid;
  grid-template-columns: 150px auto auto 1fr 20px 20px;
}

.xr-section-item {
  display: contents;
}

.xr-section-item input {
  display: none;
}

.xr-section-item input + label {
  color: var(--xr-disabled-color);
}

.xr-section-item input:enabled + label {
  cursor: pointer;
  color: var(--xr-font-color2);
}

.xr-section-item input:enabled + label:hover {
  color: var(--xr-font-color0);
}

.xr-section-summary {
  grid-column: 1;
  color: var(--xr-font-color2);
  font-weight: 500;
}

.xr-section-summary > span {
  display: inline-block;
  padding-left: 0.5em;
}

.xr-section-summary-in:disabled + label {
  color: var(--xr-font-color2);
}

.xr-section-summary-in + label:before {
  display: inline-block;
  content: '►';
  font-size: 11px;
  width: 15px;
  text-align: center;
}

.xr-section-summary-in:disabled + label:before {
  color: var(--xr-disabled-color);
}

.xr-section-summary-in:checked + label:before {
  content: '▼';
}

.xr-section-summary-in:checked + label > span {
  display: none;
}

.xr-section-summary,
.xr-section-inline-details {
  padding-top: 4px;
  padding-bottom: 4px;
}

.xr-section-inline-details {
  grid-column: 2 / -1;
}

.xr-section-details {
  display: none;
  grid-column: 1 / -1;
  margin-bottom: 5px;
}

.xr-section-summary-in:checked ~ .xr-section-details {
  display: contents;
}

.xr-array-wrap {
  grid-column: 1 / -1;
  display: grid;
  grid-template-columns: 20px auto;
}

.xr-array-wrap > label {
  grid-column: 1;
  vertical-align: top;
}

.xr-preview {
  color: var(--xr-font-color3);
}

.xr-array-preview,
.xr-array-data {
  padding: 0 5px !important;
  grid-column: 2;
}

.xr-array-data,
.xr-array-in:checked ~ .xr-array-preview {
  display: none;
}

.xr-array-in:checked ~ .xr-array-data,
.xr-array-preview {
  display: inline-block;
}

.xr-dim-list {
  display: inline-block !important;
  list-style: none;
  padding: 0 !important;
  margin: 0;
}

.xr-dim-list li {
  display: inline-block;
  padding: 0;
  margin: 0;
}

.xr-dim-list:before {
  content: '(';
}

.xr-dim-list:after {
  content: ')';
}

.xr-dim-list li:not(:last-child):after {
  content: ',';
  padding-right: 5px;
}

.xr-has-index {
  font-weight: bold;
}

.xr-var-list,
.xr-var-item {
  display: contents;
}

.xr-var-item > div,
.xr-var-item label,
.xr-var-item > .xr-var-name span {
  background-color: var(--xr-background-color-row-even);
  margin-bottom: 0;
}

.xr-var-item > .xr-var-name:hover span {
  padding-right: 5px;
}

.xr-var-list > li:nth-child(odd) > div,
.xr-var-list > li:nth-child(odd) > label,
.xr-var-list > li:nth-child(odd) > .xr-var-name span {
  background-color: var(--xr-background-color-row-odd);
}

.xr-var-name {
  grid-column: 1;
}

.xr-var-dims {
  grid-column: 2;
}

.xr-var-dtype {
  grid-column: 3;
  text-align: right;
  color: var(--xr-font-color2);
}

.xr-var-preview {
  grid-column: 4;
}

.xr-var-name,
.xr-var-dims,
.xr-var-dtype,
.xr-preview,
.xr-attrs dt {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  padding-right: 10px;
}

.xr-var-name:hover,
.xr-var-dims:hover,
.xr-var-dtype:hover,
.xr-attrs dt:hover {
  overflow: visible;
  width: auto;
  z-index: 1;
}

.xr-var-attrs,
.xr-var-data {
  display: none;
  background-color: var(--xr-background-color) !important;
  padding-bottom: 5px !important;
}

.xr-var-attrs-in:checked ~ .xr-var-attrs,
.xr-var-data-in:checked ~ .xr-var-data {
  display: block;
}

.xr-var-data > table {
  float: right;
}

.xr-var-name span,
.xr-var-data,
.xr-attrs {
  padding-left: 25px !important;
}

.xr-attrs,
.xr-var-attrs,
.xr-var-data {
  grid-column: 1 / -1;
}

dl.xr-attrs {
  padding: 0;
  margin: 0;
  display: grid;
  grid-template-columns: 125px auto;
}

.xr-attrs dt,
.xr-attrs dd {
  padding: 0;
  margin: 0;
  float: left;
  padding-right: 10px;
  width: auto;
}

.xr-attrs dt {
  font-weight: normal;
  grid-column: 1;
}

.xr-attrs dt:hover span {
  display: inline-block;
  background: var(--xr-background-color);
  padding-right: 10px;
}

.xr-attrs dd {
  grid-column: 2;
  white-space: pre-wrap;
  word-break: break-all;
}

.xr-icon-database,
.xr-icon-file-text2 {
  display: inline-block;
  vertical-align: middle;
  width: 1em;
  height: 1.5em !important;
  stroke-width: 0;
  stroke: currentColor;
  fill: currentColor;
}
</style><pre class='xr-text-repr-fallback'>&lt;xarray.Dataset&gt;
Dimensions:     (time: 367439, feature_id: 2776738)
Coordinates:
  * feature_id  (feature_id) int32 6635572 6635590 6635598 ... 25293410 15450136
  * time        (time) datetime64[ns] 1979-02-01T01:00:00 ... 2020-12-31T23:0...
Data variables:
    depth       (time, feature_id) float64 dask.array&lt;chunksize=(672, 30000), meta=np.ndarray&gt;
    inflow      (time, feature_id) float64 dask.array&lt;chunksize=(672, 30000), meta=np.ndarray&gt;
    outflow     (time, feature_id) float64 dask.array&lt;chunksize=(672, 30000), meta=np.ndarray&gt;
Attributes:
    Conventions:          CF-1.6
    TITLE:                OUTPUT FROM WRF-Hydro v5.2.0-beta2
    code_version:         v5.2.0-beta2
    featureType:          timeSeries
    model_configuration:  retrospective
    model_output_type:    groundwater_rt
    station_dimension:    gw_id</pre><div class='xr-wrap' hidden><div class='xr-header'><div class='xr-obj-type'>xarray.Dataset</div></div><ul class='xr-sections'><li class='xr-section-item'><input id='section-156d63d7-95f1-4b12-b188-e6b4a2775684' class='xr-section-summary-in' type='checkbox' disabled ><label for='section-156d63d7-95f1-4b12-b188-e6b4a2775684' class='xr-section-summary'  title='Expand/collapse section'>Dimensions:</label><div class='xr-section-inline-details'><ul class='xr-dim-list'><li><span class='xr-has-index'>time</span>: 367439</li><li><span class='xr-has-index'>feature_id</span>: 2776738</li></ul></div><div class='xr-section-details'></div></li><li class='xr-section-item'><input id='section-78ffd1aa-e7de-4514-9884-08ba985a38d5' class='xr-section-summary-in' type='checkbox'  checked><label for='section-78ffd1aa-e7de-4514-9884-08ba985a38d5' class='xr-section-summary' >Coordinates: <span>(2)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>feature_id</span></div><div class='xr-var-dims'>(feature_id)</div><div class='xr-var-dtype'>int32</div><div class='xr-var-preview xr-preview'>6635572 6635590 ... 15450136</div><input id='attrs-15c77178-beb0-4980-a50f-9f6b15df852f' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-15c77178-beb0-4980-a50f-9f6b15df852f' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-2c57a510-932f-41b5-8b3f-1fbfd8d405f9' class='xr-var-data-in' type='checkbox'><label for='data-2c57a510-932f-41b5-8b3f-1fbfd8d405f9' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>cf_role :</span></dt><dd>timeseries_id</dd><dt><span>comment :</span></dt><dd>Groundwater Bucket ID</dd><dt><span>long_name :</span></dt><dd>Groundwater Bucket ID</dd></dl></div><div class='xr-var-data'><pre>array([ 6635572,  6635590,  6635598, ..., 15448486, 25293410, 15450136],
      dtype=int32)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>time</span></div><div class='xr-var-dims'>(time)</div><div class='xr-var-dtype'>datetime64[ns]</div><div class='xr-var-preview xr-preview'>1979-02-01T01:00:00 ... 2020-12-...</div><input id='attrs-ac3b020c-5fe2-4fd5-b3a0-eec8b6e5fc58' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-ac3b020c-5fe2-4fd5-b3a0-eec8b6e5fc58' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-4018842b-2e9b-45ae-9aa0-de1100fec245' class='xr-var-data-in' type='checkbox'><label for='data-4018842b-2e9b-45ae-9aa0-de1100fec245' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>valid output time</dd><dt><span>standard_name :</span></dt><dd>time</dd><dt><span>valid_max :</span></dt><dd>4862880</dd><dt><span>valid_min :</span></dt><dd>4777980</dd></dl></div><div class='xr-var-data'><pre>array([&#x27;1979-02-01T01:00:00.000000000&#x27;, &#x27;1979-02-01T02:00:00.000000000&#x27;,
       &#x27;1979-02-01T03:00:00.000000000&#x27;, ..., &#x27;2020-12-31T21:00:00.000000000&#x27;,
       &#x27;2020-12-31T22:00:00.000000000&#x27;, &#x27;2020-12-31T23:00:00.000000000&#x27;],
      dtype=&#x27;datetime64[ns]&#x27;)</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-2e46e076-482f-4eec-835b-5263be574d68' class='xr-section-summary-in' type='checkbox'  checked><label for='section-2e46e076-482f-4eec-835b-5263be574d68' class='xr-section-summary' >Data variables: <span>(3)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-var-name'><span>depth</span></div><div class='xr-var-dims'>(time, feature_id)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(672, 30000), meta=np.ndarray&gt;</div><input id='attrs-bc626830-4044-466f-8b66-20b254b1d458' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-bc626830-4044-466f-8b66-20b254b1d458' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-2a33c15e-99cf-48fb-80ae-08b1b2310218' class='xr-var-data-in' type='checkbox'><label for='data-2a33c15e-99cf-48fb-80ae-08b1b2310218' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Bucket Depth</dd><dt><span>units :</span></dt><dd>mm</dd></dl></div><div class='xr-var-data'><table>
    <tr>
        <td>
            <table>
                <thead>
                    <tr>
                        <td> </td>
                        <th> Array </th>
                        <th> Chunk </th>
                    </tr>
                </thead>
                <tbody>

                    <tr>
                        <th> Bytes </th>
                        <td> 7.42 TiB </td>
                        <td> 153.81 MiB </td>
                    </tr>

                    <tr>
                        <th> Shape </th>
                        <td> (367439, 2776738) </td>
                        <td> (672, 30000) </td>
                    </tr>
                    <tr>
                        <th> Count </th>
                        <td> 50872 Tasks </td>
                        <td> 50871 Chunks </td>
                    </tr>
                    <tr>
                    <th> Type </th>
                    <td> float64 </td>
                    <td> numpy.ndarray </td>
                    </tr>
                </tbody>
            </table>
        </td>
        <td>
        <svg width="170" height="90" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="0" y1="0" x2="120" y2="0" style="stroke-width:2" />
  <line x1="0" y1="2" x2="120" y2="2" />
  <line x1="0" y1="4" x2="120" y2="4" />
  <line x1="0" y1="6" x2="120" y2="6" />
  <line x1="0" y1="8" x2="120" y2="8" />
  <line x1="0" y1="10" x2="120" y2="10" />
  <line x1="0" y1="12" x2="120" y2="12" />
  <line x1="0" y1="14" x2="120" y2="14" />
  <line x1="0" y1="16" x2="120" y2="16" />
  <line x1="0" y1="18" x2="120" y2="18" />
  <line x1="0" y1="21" x2="120" y2="21" />
  <line x1="0" y1="23" x2="120" y2="23" />
  <line x1="0" y1="25" x2="120" y2="25" />
  <line x1="0" y1="27" x2="120" y2="27" />
  <line x1="0" y1="29" x2="120" y2="29" />
  <line x1="0" y1="31" x2="120" y2="31" />
  <line x1="0" y1="33" x2="120" y2="33" />
  <line x1="0" y1="35" x2="120" y2="35" />
  <line x1="0" y1="37" x2="120" y2="37" />
  <line x1="0" y1="40" x2="120" y2="40" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="0" y1="0" x2="0" y2="40" style="stroke-width:2" />
  <line x1="5" y1="0" x2="5" y2="40" />
  <line x1="11" y1="0" x2="11" y2="40" />
  <line x1="18" y1="0" x2="18" y2="40" />
  <line x1="24" y1="0" x2="24" y2="40" />
  <line x1="31" y1="0" x2="31" y2="40" />
  <line x1="37" y1="0" x2="37" y2="40" />
  <line x1="44" y1="0" x2="44" y2="40" />
  <line x1="50" y1="0" x2="50" y2="40" />
  <line x1="57" y1="0" x2="57" y2="40" />
  <line x1="62" y1="0" x2="62" y2="40" />
  <line x1="68" y1="0" x2="68" y2="40" />
  <line x1="75" y1="0" x2="75" y2="40" />
  <line x1="81" y1="0" x2="81" y2="40" />
  <line x1="88" y1="0" x2="88" y2="40" />
  <line x1="94" y1="0" x2="94" y2="40" />
  <line x1="101" y1="0" x2="101" y2="40" />
  <line x1="107" y1="0" x2="107" y2="40" />
  <line x1="114" y1="0" x2="114" y2="40" />
  <line x1="120" y1="0" x2="120" y2="40" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="0.0,0.0 120.0,0.0 120.0,40.085781428943086 0.0,40.085781428943086" style="fill:#8B4903A0;stroke-width:0"/>

  <!-- Text -->
  <text x="60.000000" y="60.085781" font-size="1.0rem" font-weight="100" text-anchor="middle" >2776738</text>
  <text x="140.000000" y="20.042891" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(-90,140.000000,20.042891)">367439</text>
</svg>
        </td>
    </tr>
</table></div></li><li class='xr-var-item'><div class='xr-var-name'><span>inflow</span></div><div class='xr-var-dims'>(time, feature_id)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(672, 30000), meta=np.ndarray&gt;</div><input id='attrs-94c4711b-979c-4ad3-8bc5-bc1356d414c5' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-94c4711b-979c-4ad3-8bc5-bc1356d414c5' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-f23abdc2-7ea9-4126-ab21-f5d487cf9269' class='xr-var-data-in' type='checkbox'><label for='data-f23abdc2-7ea9-4126-ab21-f5d487cf9269' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Bucket Inflow</dd><dt><span>units :</span></dt><dd>m3 s-1</dd></dl></div><div class='xr-var-data'><table>
    <tr>
        <td>
            <table>
                <thead>
                    <tr>
                        <td> </td>
                        <th> Array </th>
                        <th> Chunk </th>
                    </tr>
                </thead>
                <tbody>

                    <tr>
                        <th> Bytes </th>
                        <td> 7.42 TiB </td>
                        <td> 153.81 MiB </td>
                    </tr>

                    <tr>
                        <th> Shape </th>
                        <td> (367439, 2776738) </td>
                        <td> (672, 30000) </td>
                    </tr>
                    <tr>
                        <th> Count </th>
                        <td> 50872 Tasks </td>
                        <td> 50871 Chunks </td>
                    </tr>
                    <tr>
                    <th> Type </th>
                    <td> float64 </td>
                    <td> numpy.ndarray </td>
                    </tr>
                </tbody>
            </table>
        </td>
        <td>
        <svg width="170" height="90" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="0" y1="0" x2="120" y2="0" style="stroke-width:2" />
  <line x1="0" y1="2" x2="120" y2="2" />
  <line x1="0" y1="4" x2="120" y2="4" />
  <line x1="0" y1="6" x2="120" y2="6" />
  <line x1="0" y1="8" x2="120" y2="8" />
  <line x1="0" y1="10" x2="120" y2="10" />
  <line x1="0" y1="12" x2="120" y2="12" />
  <line x1="0" y1="14" x2="120" y2="14" />
  <line x1="0" y1="16" x2="120" y2="16" />
  <line x1="0" y1="18" x2="120" y2="18" />
  <line x1="0" y1="21" x2="120" y2="21" />
  <line x1="0" y1="23" x2="120" y2="23" />
  <line x1="0" y1="25" x2="120" y2="25" />
  <line x1="0" y1="27" x2="120" y2="27" />
  <line x1="0" y1="29" x2="120" y2="29" />
  <line x1="0" y1="31" x2="120" y2="31" />
  <line x1="0" y1="33" x2="120" y2="33" />
  <line x1="0" y1="35" x2="120" y2="35" />
  <line x1="0" y1="37" x2="120" y2="37" />
  <line x1="0" y1="40" x2="120" y2="40" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="0" y1="0" x2="0" y2="40" style="stroke-width:2" />
  <line x1="5" y1="0" x2="5" y2="40" />
  <line x1="11" y1="0" x2="11" y2="40" />
  <line x1="18" y1="0" x2="18" y2="40" />
  <line x1="24" y1="0" x2="24" y2="40" />
  <line x1="31" y1="0" x2="31" y2="40" />
  <line x1="37" y1="0" x2="37" y2="40" />
  <line x1="44" y1="0" x2="44" y2="40" />
  <line x1="50" y1="0" x2="50" y2="40" />
  <line x1="57" y1="0" x2="57" y2="40" />
  <line x1="62" y1="0" x2="62" y2="40" />
  <line x1="68" y1="0" x2="68" y2="40" />
  <line x1="75" y1="0" x2="75" y2="40" />
  <line x1="81" y1="0" x2="81" y2="40" />
  <line x1="88" y1="0" x2="88" y2="40" />
  <line x1="94" y1="0" x2="94" y2="40" />
  <line x1="101" y1="0" x2="101" y2="40" />
  <line x1="107" y1="0" x2="107" y2="40" />
  <line x1="114" y1="0" x2="114" y2="40" />
  <line x1="120" y1="0" x2="120" y2="40" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="0.0,0.0 120.0,0.0 120.0,40.085781428943086 0.0,40.085781428943086" style="fill:#8B4903A0;stroke-width:0"/>

  <!-- Text -->
  <text x="60.000000" y="60.085781" font-size="1.0rem" font-weight="100" text-anchor="middle" >2776738</text>
  <text x="140.000000" y="20.042891" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(-90,140.000000,20.042891)">367439</text>
</svg>
        </td>
    </tr>
</table></div></li><li class='xr-var-item'><div class='xr-var-name'><span>outflow</span></div><div class='xr-var-dims'>(time, feature_id)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(672, 30000), meta=np.ndarray&gt;</div><input id='attrs-60d0ee4a-6313-4a29-b7e0-4e730e69b6ef' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-60d0ee4a-6313-4a29-b7e0-4e730e69b6ef' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-1f9192a8-1e4f-4785-9d9f-25e4be32bdf4' class='xr-var-data-in' type='checkbox'><label for='data-1f9192a8-1e4f-4785-9d9f-25e4be32bdf4' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Bucket Outflow</dd><dt><span>units :</span></dt><dd>m3 s-1</dd></dl></div><div class='xr-var-data'><table>
    <tr>
        <td>
            <table>
                <thead>
                    <tr>
                        <td> </td>
                        <th> Array </th>
                        <th> Chunk </th>
                    </tr>
                </thead>
                <tbody>

                    <tr>
                        <th> Bytes </th>
                        <td> 7.42 TiB </td>
                        <td> 153.81 MiB </td>
                    </tr>

                    <tr>
                        <th> Shape </th>
                        <td> (367439, 2776738) </td>
                        <td> (672, 30000) </td>
                    </tr>
                    <tr>
                        <th> Count </th>
                        <td> 50872 Tasks </td>
                        <td> 50871 Chunks </td>
                    </tr>
                    <tr>
                    <th> Type </th>
                    <td> float64 </td>
                    <td> numpy.ndarray </td>
                    </tr>
                </tbody>
            </table>
        </td>
        <td>
        <svg width="170" height="90" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="0" y1="0" x2="120" y2="0" style="stroke-width:2" />
  <line x1="0" y1="2" x2="120" y2="2" />
  <line x1="0" y1="4" x2="120" y2="4" />
  <line x1="0" y1="6" x2="120" y2="6" />
  <line x1="0" y1="8" x2="120" y2="8" />
  <line x1="0" y1="10" x2="120" y2="10" />
  <line x1="0" y1="12" x2="120" y2="12" />
  <line x1="0" y1="14" x2="120" y2="14" />
  <line x1="0" y1="16" x2="120" y2="16" />
  <line x1="0" y1="18" x2="120" y2="18" />
  <line x1="0" y1="21" x2="120" y2="21" />
  <line x1="0" y1="23" x2="120" y2="23" />
  <line x1="0" y1="25" x2="120" y2="25" />
  <line x1="0" y1="27" x2="120" y2="27" />
  <line x1="0" y1="29" x2="120" y2="29" />
  <line x1="0" y1="31" x2="120" y2="31" />
  <line x1="0" y1="33" x2="120" y2="33" />
  <line x1="0" y1="35" x2="120" y2="35" />
  <line x1="0" y1="37" x2="120" y2="37" />
  <line x1="0" y1="40" x2="120" y2="40" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="0" y1="0" x2="0" y2="40" style="stroke-width:2" />
  <line x1="5" y1="0" x2="5" y2="40" />
  <line x1="11" y1="0" x2="11" y2="40" />
  <line x1="18" y1="0" x2="18" y2="40" />
  <line x1="24" y1="0" x2="24" y2="40" />
  <line x1="31" y1="0" x2="31" y2="40" />
  <line x1="37" y1="0" x2="37" y2="40" />
  <line x1="44" y1="0" x2="44" y2="40" />
  <line x1="50" y1="0" x2="50" y2="40" />
  <line x1="57" y1="0" x2="57" y2="40" />
  <line x1="62" y1="0" x2="62" y2="40" />
  <line x1="68" y1="0" x2="68" y2="40" />
  <line x1="75" y1="0" x2="75" y2="40" />
  <line x1="81" y1="0" x2="81" y2="40" />
  <line x1="88" y1="0" x2="88" y2="40" />
  <line x1="94" y1="0" x2="94" y2="40" />
  <line x1="101" y1="0" x2="101" y2="40" />
  <line x1="107" y1="0" x2="107" y2="40" />
  <line x1="114" y1="0" x2="114" y2="40" />
  <line x1="120" y1="0" x2="120" y2="40" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="0.0,0.0 120.0,0.0 120.0,40.085781428943086 0.0,40.085781428943086" style="fill:#8B4903A0;stroke-width:0"/>

  <!-- Text -->
  <text x="60.000000" y="60.085781" font-size="1.0rem" font-weight="100" text-anchor="middle" >2776738</text>
  <text x="140.000000" y="20.042891" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(-90,140.000000,20.042891)">367439</text>
</svg>
        </td>
    </tr>
</table></div></li></ul></div></li><li class='xr-section-item'><input id='section-3e73dd03-ba45-4deb-862a-5a4d0926f7fd' class='xr-section-summary-in' type='checkbox'  checked><label for='section-3e73dd03-ba45-4deb-862a-5a4d0926f7fd' class='xr-section-summary' >Attributes: <span>(7)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><dl class='xr-attrs'><dt><span>Conventions :</span></dt><dd>CF-1.6</dd><dt><span>TITLE :</span></dt><dd>OUTPUT FROM WRF-Hydro v5.2.0-beta2</dd><dt><span>code_version :</span></dt><dd>v5.2.0-beta2</dd><dt><span>featureType :</span></dt><dd>timeSeries</dd><dt><span>model_configuration :</span></dt><dd>retrospective</dd><dt><span>model_output_type :</span></dt><dd>groundwater_rt</dd><dt><span>station_dimension :</span></dt><dd>gw_id</dd></dl></div></li></ul></div></div>



```python

```
