
Import packages 
===============

.. code:: 

    import xarray as xr
    import matplotlib.pyplot as plt
    import seawater
    import numpy as np
    import pandas as pd
    import cartopy.crs as ccrs
    from cartopy.feature import NaturalEarthFeature
    from mpl_toolkits.basemap import Basemap
    import matplotlib.ticker as mticker
    from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
    import matplotlib.dates as mdates
    import datetime as dt
    import pylab
    from matplotlib.dates import YearLocator, MonthLocator, DateFormatter
    import matplotlib.ticker as ticker
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    from mpl_toolkits.axes_grid1.axes_divider import make_axes_area_auto_adjustable
    import matplotlib as mpl
    import matplotlib.transforms as mtransforms
    from matplotlib.patches import Circle
    from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage,
                                      AnnotationBbox)
    from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, mark_inset
    from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar
    from matplotlib.offsetbox import OffsetImage,AnchoredOffsetbox
    import matplotlib.image as image


.. parsed-literal::

    /home/lenovo/miniconda3/envs/envplot/lib/python3.10/site-packages/scipy/__init__.py:155: UserWarning: A NumPy version >=1.18.5 and <1.25.0 is required for this version of SciPy (detected version 1.25.2
      warnings.warn(f"A NumPy version >={np_minversion} and <{np_maxversion}"


load data
---------

.. code:: 

    data = xr.open_dataset('5905017_prof.nc')
    data




.. raw:: html

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
    body[data-theme=dark],
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
      display: block !important;
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
    Dimensions:                       (N_PROF: 202, N_PARAM: 3, N_LEVELS: 999,
                                       N_CALIB: 1, N_HISTORY: 0)
    Dimensions without coordinates: N_PROF, N_PARAM, N_LEVELS, N_CALIB, N_HISTORY
    Data variables: (12/64)
        DATA_TYPE                     object b&#x27;Argo profile    &#x27;
        FORMAT_VERSION                object b&#x27;3.1 &#x27;
        HANDBOOK_VERSION              object b&#x27;1.2 &#x27;
        REFERENCE_DATE_TIME           object b&#x27;19500101000000&#x27;
        DATE_CREATION                 object b&#x27;20160111211846&#x27;
        DATE_UPDATE                   object b&#x27;20210803081648&#x27;
        ...                            ...
        HISTORY_ACTION                (N_HISTORY, N_PROF) object 
        HISTORY_PARAMETER             (N_HISTORY, N_PROF) object 
        HISTORY_START_PRES            (N_HISTORY, N_PROF) float32 
        HISTORY_STOP_PRES             (N_HISTORY, N_PROF) float32 
        HISTORY_PREVIOUS_VALUE        (N_HISTORY, N_PROF) float32 
        HISTORY_QCTEST                (N_HISTORY, N_PROF) object 
    Attributes:
        title:                Argo float vertical profile
        institution:          FR GDAC
        source:               Argo float
        history:              2021-08-03T08:16:48Z creation
        references:           http://www.argodatamgt.org/Documentation
        user_manual_version:  3.1
        Conventions:          Argo-3.1 CF-1.6
        featureType:          trajectoryProfile</pre><div class='xr-wrap' style='display:none'><div class='xr-header'><div class='xr-obj-type'>xarray.Dataset</div></div><ul class='xr-sections'><li class='xr-section-item'><input id='section-d3acf5b6-1aa3-425c-8eeb-0bfd46aa5f77' class='xr-section-summary-in' type='checkbox' disabled ><label for='section-d3acf5b6-1aa3-425c-8eeb-0bfd46aa5f77' class='xr-section-summary'  title='Expand/collapse section'>Dimensions:</label><div class='xr-section-inline-details'><ul class='xr-dim-list'><li><span>N_PROF</span>: 202</li><li><span>N_PARAM</span>: 3</li><li><span>N_LEVELS</span>: 999</li><li><span>N_CALIB</span>: 1</li><li><span>N_HISTORY</span>: 0</li></ul></div><div class='xr-section-details'></div></li><li class='xr-section-item'><input id='section-e5a0f896-e927-4565-9b94-e974660f0790' class='xr-section-summary-in' type='checkbox' disabled ><label for='section-e5a0f896-e927-4565-9b94-e974660f0790' class='xr-section-summary'  title='Expand/collapse section'>Coordinates: <span>(0)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'></ul></div></li><li class='xr-section-item'><input id='section-64432ade-cf8f-4272-81f4-a9f669d3304c' class='xr-section-summary-in' type='checkbox'  ><label for='section-64432ade-cf8f-4272-81f4-a9f669d3304c' class='xr-section-summary' >Data variables: <span>(64)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-var-name'><span>DATA_TYPE</span></div><div class='xr-var-dims'>()</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-f82e7a3e-f448-43ba-a93b-2bdb7e1ae077' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-f82e7a3e-f448-43ba-a93b-2bdb7e1ae077' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-097d05ab-8898-4b2a-80be-30b92c57ffa7' class='xr-var-data-in' type='checkbox'><label for='data-097d05ab-8898-4b2a-80be-30b92c57ffa7' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Data type</dd><dt><span>conventions :</span></dt><dd>Argo reference table 1</dd></dl></div><div class='xr-var-data'><pre>array(b&#x27;Argo profile    &#x27;, dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>FORMAT_VERSION</span></div><div class='xr-var-dims'>()</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-9cfc9f8a-8cb1-4868-a155-707a5842932c' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-9cfc9f8a-8cb1-4868-a155-707a5842932c' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-08764a1e-22e0-4c91-a2ca-c4fa257eed69' class='xr-var-data-in' type='checkbox'><label for='data-08764a1e-22e0-4c91-a2ca-c4fa257eed69' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>File format version</dd></dl></div><div class='xr-var-data'><pre>array(b&#x27;3.1 &#x27;, dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>HANDBOOK_VERSION</span></div><div class='xr-var-dims'>()</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-4ceb23a4-f379-48ff-bf1d-ef72ed3ec634' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-4ceb23a4-f379-48ff-bf1d-ef72ed3ec634' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-15a7be32-3df7-4e46-aea8-59f209ab078f' class='xr-var-data-in' type='checkbox'><label for='data-15a7be32-3df7-4e46-aea8-59f209ab078f' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Data handbook version</dd></dl></div><div class='xr-var-data'><pre>array(b&#x27;1.2 &#x27;, dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>REFERENCE_DATE_TIME</span></div><div class='xr-var-dims'>()</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-b5207fdf-6ede-4670-a196-91fffaff3eeb' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-b5207fdf-6ede-4670-a196-91fffaff3eeb' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-44b833a4-008f-4a11-8758-a4427a165ce6' class='xr-var-data-in' type='checkbox'><label for='data-44b833a4-008f-4a11-8758-a4427a165ce6' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Date of reference for Julian days</dd><dt><span>conventions :</span></dt><dd>YYYYMMDDHHMISS</dd></dl></div><div class='xr-var-data'><pre>array(b&#x27;19500101000000&#x27;, dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>DATE_CREATION</span></div><div class='xr-var-dims'>()</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-f7c4280f-f2b9-45a8-b666-852f313234a8' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-f7c4280f-f2b9-45a8-b666-852f313234a8' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-857ca821-cf3f-49f1-9086-d70704dedf8d' class='xr-var-data-in' type='checkbox'><label for='data-857ca821-cf3f-49f1-9086-d70704dedf8d' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Date of file creation</dd><dt><span>conventions :</span></dt><dd>YYYYMMDDHHMISS</dd></dl></div><div class='xr-var-data'><pre>array(b&#x27;20160111211846&#x27;, dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>DATE_UPDATE</span></div><div class='xr-var-dims'>()</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-d6eedf42-3bcb-44ec-8b0a-2b6a76cecaff' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-d6eedf42-3bcb-44ec-8b0a-2b6a76cecaff' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-58340b40-7df0-4ac6-b52e-861fb511920a' class='xr-var-data-in' type='checkbox'><label for='data-58340b40-7df0-4ac6-b52e-861fb511920a' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Date of update of this file</dd><dt><span>conventions :</span></dt><dd>YYYYMMDDHHMISS</dd></dl></div><div class='xr-var-data'><pre>array(b&#x27;20210803081648&#x27;, dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>PLATFORM_NUMBER</span></div><div class='xr-var-dims'>(N_PROF)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-c9f41557-151d-46aa-b706-698333d74a56' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-c9f41557-151d-46aa-b706-698333d74a56' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-70f86214-531c-4cfa-b524-77eb3e944eea' class='xr-var-data-in' type='checkbox'><label for='data-70f86214-531c-4cfa-b524-77eb3e944eea' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Float unique identifier</dd><dt><span>conventions :</span></dt><dd>WMO float identifier : A9IIIII</dd></dl></div><div class='xr-var-data'><pre>array([b&#x27;5905017 &#x27;, b&#x27;5905017 &#x27;, b&#x27;5905017 &#x27;, ..., b&#x27;5905017 &#x27;, b&#x27;5905017 &#x27;,
           b&#x27;5905017 &#x27;], dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>PROJECT_NAME</span></div><div class='xr-var-dims'>(N_PROF)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-4fd743dc-1ddc-449e-a8ac-429df50f5d1c' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-4fd743dc-1ddc-449e-a8ac-429df50f5d1c' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-583e6f10-786d-4438-ab67-fb0e5af964c5' class='xr-var-data-in' type='checkbox'><label for='data-583e6f10-786d-4438-ab67-fb0e5af964c5' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Name of the project</dd></dl></div><div class='xr-var-data'><pre>array([b&#x27;Argo Australia                                                  &#x27;,
           b&#x27;Argo Australia                                                  &#x27;,
           b&#x27;Argo Australia                                                  &#x27;,
           ...,
           b&#x27;Argo Australia                                                  &#x27;,
           b&#x27;Argo Australia                                                  &#x27;,
           b&#x27;Argo Australia                                                  &#x27;],
          dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>PI_NAME</span></div><div class='xr-var-dims'>(N_PROF)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-3b3bb669-9e90-40fa-8612-39f347db1b8d' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-3b3bb669-9e90-40fa-8612-39f347db1b8d' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-ae71f33b-8633-4f1a-833c-5aad4dae6f65' class='xr-var-data-in' type='checkbox'><label for='data-ae71f33b-8633-4f1a-833c-5aad4dae6f65' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Name of the principal investigator</dd></dl></div><div class='xr-var-data'><pre>array([b&#x27;Susan Wijffels                                                  &#x27;,
           b&#x27;Susan Wijffels                                                  &#x27;,
           b&#x27;Susan Wijffels                                                  &#x27;,
           ...,
           b&#x27;Susan Wijffels                                                  &#x27;,
           b&#x27;Susan Wijffels                                                  &#x27;,
           b&#x27;Susan Wijffels                                                  &#x27;],
          dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>STATION_PARAMETERS</span></div><div class='xr-var-dims'>(N_PROF, N_PARAM)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-e3fa854a-9a9b-4a9b-aa32-f53bf5932dbe' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-e3fa854a-9a9b-4a9b-aa32-f53bf5932dbe' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-dd871eeb-50a9-405a-a290-96163cf361e3' class='xr-var-data-in' type='checkbox'><label for='data-dd871eeb-50a9-405a-a290-96163cf361e3' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>List of available parameters for the station</dd><dt><span>conventions :</span></dt><dd>Argo reference table 3</dd></dl></div><div class='xr-var-data'><pre>array([[b&#x27;PRES            &#x27;, b&#x27;TEMP            &#x27;, b&#x27;PSAL            &#x27;],
           [b&#x27;PRES            &#x27;, b&#x27;TEMP            &#x27;, b&#x27;PSAL            &#x27;],
           [b&#x27;PRES            &#x27;, b&#x27;TEMP            &#x27;, b&#x27;PSAL            &#x27;],
           ...,
           [b&#x27;PRES            &#x27;, b&#x27;TEMP            &#x27;, b&#x27;PSAL            &#x27;],
           [b&#x27;PRES            &#x27;, b&#x27;TEMP            &#x27;, b&#x27;PSAL            &#x27;],
           [b&#x27;PRES            &#x27;, b&#x27;TEMP            &#x27;, b&#x27;PSAL            &#x27;]],
          dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>CYCLE_NUMBER</span></div><div class='xr-var-dims'>(N_PROF)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-d027fc24-bef9-4bcb-8fd3-19950d7822b0' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-d027fc24-bef9-4bcb-8fd3-19950d7822b0' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-5e1b02a3-f580-4b81-81f8-f5156eda9f35' class='xr-var-data-in' type='checkbox'><label for='data-5e1b02a3-f580-4b81-81f8-f5156eda9f35' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Float cycle number</dd><dt><span>conventions :</span></dt><dd>0...N, 0 : launch cycle (if exists), 1 : first complete cycle</dd></dl></div><div class='xr-var-data'><pre>array([  1.,   2.,   3., ..., 200., 201., 202.])</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>DIRECTION</span></div><div class='xr-var-dims'>(N_PROF)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-fc0b05de-0170-4712-8b14-773aa891619f' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-fc0b05de-0170-4712-8b14-773aa891619f' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-10022b4f-a8f9-4f71-b696-22cdb66ec693' class='xr-var-data-in' type='checkbox'><label for='data-10022b4f-a8f9-4f71-b696-22cdb66ec693' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Direction of the station profiles</dd><dt><span>conventions :</span></dt><dd>A: ascending profiles, D: descending profiles</dd></dl></div><div class='xr-var-data'><pre>array([b&#x27;A&#x27;, b&#x27;A&#x27;, b&#x27;A&#x27;, ..., b&#x27;A&#x27;, b&#x27;A&#x27;, b&#x27;A&#x27;], dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>DATA_CENTRE</span></div><div class='xr-var-dims'>(N_PROF)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-430f3410-c183-4738-b35c-b13546df2603' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-430f3410-c183-4738-b35c-b13546df2603' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-324607e6-04c0-490d-8e8b-25cbcfce893b' class='xr-var-data-in' type='checkbox'><label for='data-324607e6-04c0-490d-8e8b-25cbcfce893b' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Data centre in charge of float data processing</dd><dt><span>conventions :</span></dt><dd>Argo reference table 4</dd></dl></div><div class='xr-var-data'><pre>array([b&#x27;CS&#x27;, b&#x27;CS&#x27;, b&#x27;CS&#x27;, ..., b&#x27;CS&#x27;, b&#x27;CS&#x27;, b&#x27;CS&#x27;], dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>DC_REFERENCE</span></div><div class='xr-var-dims'>(N_PROF)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-7caf6fa8-834c-47e9-9497-6bc0eaf638fe' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-7caf6fa8-834c-47e9-9497-6bc0eaf638fe' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-ec04b5b9-d17e-4ed0-8fcf-c29fe1983ec3' class='xr-var-data-in' type='checkbox'><label for='data-ec04b5b9-d17e-4ed0-8fcf-c29fe1983ec3' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Station unique identifier in data centre</dd><dt><span>conventions :</span></dt><dd>Data centre convention</dd></dl></div><div class='xr-var-data'><pre>array([b&#x27;5905017/1                       &#x27;,
           b&#x27;5905017/2                       &#x27;,
           b&#x27;5905017/3                       &#x27;, ...,
           b&#x27;5905017/200                     &#x27;,
           b&#x27;5905017/201                     &#x27;,
           b&#x27;5905017/202                     &#x27;], dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>DATA_STATE_INDICATOR</span></div><div class='xr-var-dims'>(N_PROF)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-68bd303d-70e6-4261-bf64-18d801549684' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-68bd303d-70e6-4261-bf64-18d801549684' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-59e680ea-0872-48de-966e-e1678bf99067' class='xr-var-data-in' type='checkbox'><label for='data-59e680ea-0872-48de-966e-e1678bf99067' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Degree of processing the data have passed through</dd><dt><span>conventions :</span></dt><dd>Argo reference table 6</dd></dl></div><div class='xr-var-data'><pre>array([b&#x27;2C  &#x27;, b&#x27;2C  &#x27;, b&#x27;2C  &#x27;, ..., b&#x27;2C  &#x27;, b&#x27;2C  &#x27;, b&#x27;2C  &#x27;], dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>DATA_MODE</span></div><div class='xr-var-dims'>(N_PROF)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-8e3ba54e-936d-4c75-b6d9-8374049a4a47' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-8e3ba54e-936d-4c75-b6d9-8374049a4a47' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-1119ab30-378d-4cd4-a901-6950c3af03fc' class='xr-var-data-in' type='checkbox'><label for='data-1119ab30-378d-4cd4-a901-6950c3af03fc' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Delayed mode or real time data</dd><dt><span>conventions :</span></dt><dd>R : real time; D : delayed mode; A : real time with adjustment</dd></dl></div><div class='xr-var-data'><pre>array([b&#x27;D&#x27;, b&#x27;D&#x27;, b&#x27;D&#x27;, ..., b&#x27;D&#x27;, b&#x27;D&#x27;, b&#x27;D&#x27;], dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>PLATFORM_TYPE</span></div><div class='xr-var-dims'>(N_PROF)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-30087ea4-8227-463e-bf89-1977f6e90b60' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-30087ea4-8227-463e-bf89-1977f6e90b60' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-f1cfcc1c-b3da-4db3-99f1-28c686284308' class='xr-var-data-in' type='checkbox'><label for='data-f1cfcc1c-b3da-4db3-99f1-28c686284308' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Type of float</dd><dt><span>conventions :</span></dt><dd>Argo reference table 23</dd></dl></div><div class='xr-var-data'><pre>array([b&#x27;APEX                            &#x27;,
           b&#x27;APEX                            &#x27;,
           b&#x27;APEX                            &#x27;, ...,
           b&#x27;APEX                            &#x27;,
           b&#x27;APEX                            &#x27;,
           b&#x27;APEX                            &#x27;], dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>FLOAT_SERIAL_NO</span></div><div class='xr-var-dims'>(N_PROF)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-de01be06-04f4-4c4a-b896-d3f6c5490fee' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-de01be06-04f4-4c4a-b896-d3f6c5490fee' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-c6e85f6f-8a06-4472-a0b1-fdf625183ae7' class='xr-var-data-in' type='checkbox'><label for='data-c6e85f6f-8a06-4472-a0b1-fdf625183ae7' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Serial number of the float</dd></dl></div><div class='xr-var-data'><pre>array([b&#x27;7432                            &#x27;,
           b&#x27;7432                            &#x27;,
           b&#x27;7432                            &#x27;, ...,
           b&#x27;7432                            &#x27;,
           b&#x27;7432                            &#x27;,
           b&#x27;7432                            &#x27;], dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>FIRMWARE_VERSION</span></div><div class='xr-var-dims'>(N_PROF)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-ee4ba954-c132-43ea-9730-b022a191589b' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-ee4ba954-c132-43ea-9730-b022a191589b' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-af921faa-39da-4f37-8897-977d0059dc06' class='xr-var-data-in' type='checkbox'><label for='data-af921faa-39da-4f37-8897-977d0059dc06' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Instrument firmware version</dd></dl></div><div class='xr-var-data'><pre>array([b&#x27;Apf9iSbe41-CP-DT                &#x27;,
           b&#x27;Apf9iSbe41-CP-DT                &#x27;,
           b&#x27;Apf9iSbe41-CP-DT                &#x27;, ...,
           b&#x27;Apf9iSbe41-CP-DT                &#x27;,
           b&#x27;Apf9iSbe41-CP-DT                &#x27;,
           b&#x27;Apf9iSbe41-CP-DT                &#x27;], dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>WMO_INST_TYPE</span></div><div class='xr-var-dims'>(N_PROF)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-0ee2bbf1-5552-41d2-85ec-59b20fc75471' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-0ee2bbf1-5552-41d2-85ec-59b20fc75471' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-50306162-eed4-406a-abec-543fc905fdb7' class='xr-var-data-in' type='checkbox'><label for='data-50306162-eed4-406a-abec-543fc905fdb7' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Coded instrument type</dd><dt><span>conventions :</span></dt><dd>Argo reference table 8</dd></dl></div><div class='xr-var-data'><pre>array([b&#x27;846 &#x27;, b&#x27;846 &#x27;, b&#x27;846 &#x27;, ..., b&#x27;846 &#x27;, b&#x27;846 &#x27;, b&#x27;846 &#x27;], dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>JULD</span></div><div class='xr-var-dims'>(N_PROF)</div><div class='xr-var-dtype'>datetime64[ns]</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-950457e5-780b-4a49-9871-7aa574d0065e' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-950457e5-780b-4a49-9871-7aa574d0065e' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-4a4c335e-d0c6-4deb-a0ab-f1566b83c283' class='xr-var-data-in' type='checkbox'><label for='data-4a4c335e-d0c6-4deb-a0ab-f1566b83c283' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Julian day (UTC) of the station relative to REFERENCE_DATE_TIME</dd><dt><span>standard_name :</span></dt><dd>time</dd><dt><span>conventions :</span></dt><dd>Relative julian days with decimal part (as parts of day)</dd><dt><span>resolution :</span></dt><dd>0.0</dd><dt><span>axis :</span></dt><dd>T</dd></dl></div><div class='xr-var-data'><pre>array([&#x27;2016-01-07T22:06:34.000000000&#x27;, &#x27;2016-01-17T15:35:41.000000000&#x27;,
           &#x27;2016-01-27T09:41:07.000000000&#x27;, ..., &#x27;2021-05-06T13:48:53.000000000&#x27;,
           &#x27;2021-05-16T07:15:29.000000000&#x27;, &#x27;2021-05-26T02:10:37.000000000&#x27;],
          dtype=&#x27;datetime64[ns]&#x27;)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>JULD_QC</span></div><div class='xr-var-dims'>(N_PROF)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-5d8e01cc-622f-4057-99fa-7b1cd1d37659' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-5d8e01cc-622f-4057-99fa-7b1cd1d37659' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-0bc103ea-0fa3-4117-b6b3-7bb4762c2436' class='xr-var-data-in' type='checkbox'><label for='data-0bc103ea-0fa3-4117-b6b3-7bb4762c2436' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Quality on date and time</dd><dt><span>conventions :</span></dt><dd>Argo reference table 2</dd></dl></div><div class='xr-var-data'><pre>array([b&#x27;1&#x27;, b&#x27;1&#x27;, b&#x27;1&#x27;, ..., b&#x27;1&#x27;, b&#x27;1&#x27;, b&#x27;1&#x27;], dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>JULD_LOCATION</span></div><div class='xr-var-dims'>(N_PROF)</div><div class='xr-var-dtype'>datetime64[ns]</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-e3566acf-2941-4cfc-a4a8-5efeb8289a96' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-e3566acf-2941-4cfc-a4a8-5efeb8289a96' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-fcf148fc-72b9-47f3-8702-462ba348c843' class='xr-var-data-in' type='checkbox'><label for='data-fcf148fc-72b9-47f3-8702-462ba348c843' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Julian day (UTC) of the location relative to REFERENCE_DATE_TIME</dd><dt><span>conventions :</span></dt><dd>Relative julian days with decimal part (as parts of day)</dd><dt><span>resolution :</span></dt><dd>0.0</dd></dl></div><div class='xr-var-data'><pre>array([&#x27;2016-01-07T22:21:30.000000000&#x27;, &#x27;2016-01-17T15:52:10.000000000&#x27;,
           &#x27;2016-01-27T09:56:39.999999744&#x27;, ..., &#x27;2021-05-06T14:03:30.000000000&#x27;,
           &#x27;2021-05-16T07:43:40.000000000&#x27;, &#x27;2021-05-26T02:25:29.999999744&#x27;],
          dtype=&#x27;datetime64[ns]&#x27;)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>LATITUDE</span></div><div class='xr-var-dims'>(N_PROF)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-053e42ed-765d-4de2-bd54-7297399eeed1' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-053e42ed-765d-4de2-bd54-7297399eeed1' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-583ef38b-ffa2-43a2-8eee-a0cdee166429' class='xr-var-data-in' type='checkbox'><label for='data-583ef38b-ffa2-43a2-8eee-a0cdee166429' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Latitude of the station, best estimate</dd><dt><span>standard_name :</span></dt><dd>latitude</dd><dt><span>units :</span></dt><dd>degree_north</dd><dt><span>valid_min :</span></dt><dd>-90.0</dd><dt><span>valid_max :</span></dt><dd>90.0</dd><dt><span>axis :</span></dt><dd>Y</dd></dl></div><div class='xr-var-data'><pre>array([-11.023, -11.672, -12.201, ...,  -8.83 ,  -8.782,  -8.68 ])</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>LONGITUDE</span></div><div class='xr-var-dims'>(N_PROF)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-8cbc0d11-73a1-4900-9507-08138d009b9d' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-8cbc0d11-73a1-4900-9507-08138d009b9d' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-a48027a3-168e-4fb5-969e-4aa2a09f658f' class='xr-var-data-in' type='checkbox'><label for='data-a48027a3-168e-4fb5-969e-4aa2a09f658f' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Longitude of the station, best estimate</dd><dt><span>standard_name :</span></dt><dd>longitude</dd><dt><span>units :</span></dt><dd>degree_east</dd><dt><span>valid_min :</span></dt><dd>-180.0</dd><dt><span>valid_max :</span></dt><dd>180.0</dd><dt><span>axis :</span></dt><dd>X</dd></dl></div><div class='xr-var-data'><pre>array([111.729, 111.496, 111.126, ..., 112.087, 112.252, 112.753])</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>POSITION_QC</span></div><div class='xr-var-dims'>(N_PROF)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-fc2019f7-0f49-40b1-a32b-98dad1be8969' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-fc2019f7-0f49-40b1-a32b-98dad1be8969' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-96bbc5be-fb4f-451e-8c1b-38d79721725b' class='xr-var-data-in' type='checkbox'><label for='data-96bbc5be-fb4f-451e-8c1b-38d79721725b' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Quality on position (latitude and longitude)</dd><dt><span>conventions :</span></dt><dd>Argo reference table 2</dd></dl></div><div class='xr-var-data'><pre>array([b&#x27;1&#x27;, b&#x27;1&#x27;, b&#x27;1&#x27;, ..., b&#x27;1&#x27;, b&#x27;1&#x27;, b&#x27;1&#x27;], dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>POSITIONING_SYSTEM</span></div><div class='xr-var-dims'>(N_PROF)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-be9b8f83-614c-44ed-b942-1eeaea690d63' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-be9b8f83-614c-44ed-b942-1eeaea690d63' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-e0c126ab-ca35-4388-bbf3-76d31dc1cdf2' class='xr-var-data-in' type='checkbox'><label for='data-e0c126ab-ca35-4388-bbf3-76d31dc1cdf2' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Positioning system</dd></dl></div><div class='xr-var-data'><pre>array([b&#x27;GPS     &#x27;, b&#x27;GPS     &#x27;, b&#x27;GPS     &#x27;, ..., b&#x27;GPS     &#x27;, b&#x27;GPS     &#x27;,
           b&#x27;GPS     &#x27;], dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>PROFILE_PRES_QC</span></div><div class='xr-var-dims'>(N_PROF)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-39a6f9d2-de3e-4262-8506-701e447e8591' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-39a6f9d2-de3e-4262-8506-701e447e8591' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-c719fc78-9312-40b6-93f5-b4dc2d017af3' class='xr-var-data-in' type='checkbox'><label for='data-c719fc78-9312-40b6-93f5-b4dc2d017af3' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Global quality flag of PRES profile</dd><dt><span>conventions :</span></dt><dd>Argo reference table 2a</dd></dl></div><div class='xr-var-data'><pre>array([b&#x27;A&#x27;, b&#x27;A&#x27;, b&#x27;A&#x27;, ..., b&#x27;A&#x27;, b&#x27;A&#x27;, b&#x27;A&#x27;], dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>PROFILE_TEMP_QC</span></div><div class='xr-var-dims'>(N_PROF)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-286ac3ce-b528-4251-bc3f-1968e2b6a962' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-286ac3ce-b528-4251-bc3f-1968e2b6a962' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-5fe707b6-27fc-4ea4-99de-0ff432201739' class='xr-var-data-in' type='checkbox'><label for='data-5fe707b6-27fc-4ea4-99de-0ff432201739' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Global quality flag of TEMP profile</dd><dt><span>conventions :</span></dt><dd>Argo reference table 2a</dd></dl></div><div class='xr-var-data'><pre>array([b&#x27;A&#x27;, b&#x27;A&#x27;, b&#x27;A&#x27;, ..., b&#x27;A&#x27;, b&#x27;A&#x27;, b&#x27;A&#x27;], dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>PROFILE_PSAL_QC</span></div><div class='xr-var-dims'>(N_PROF)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-e0677417-b902-4aaa-b3e0-22e92b18ec91' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-e0677417-b902-4aaa-b3e0-22e92b18ec91' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-9c798c60-fa1d-4c07-8250-7a6e1742f820' class='xr-var-data-in' type='checkbox'><label for='data-9c798c60-fa1d-4c07-8250-7a6e1742f820' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Global quality flag of PSAL profile</dd><dt><span>conventions :</span></dt><dd>Argo reference table 2a</dd></dl></div><div class='xr-var-data'><pre>array([b&#x27;A&#x27;, b&#x27;A&#x27;, b&#x27;A&#x27;, ..., b&#x27;F&#x27;, b&#x27;F&#x27;, b&#x27;F&#x27;], dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>VERTICAL_SAMPLING_SCHEME</span></div><div class='xr-var-dims'>(N_PROF)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-f3bd9768-3fee-4b05-96a7-aef4cafac721' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-f3bd9768-3fee-4b05-96a7-aef4cafac721' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-27081590-7f0a-41c4-91d3-12d62a617b85' class='xr-var-data-in' type='checkbox'><label for='data-27081590-7f0a-41c4-91d3-12d62a617b85' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Vertical sampling scheme</dd><dt><span>conventions :</span></dt><dd>Argo reference table 16</dd></dl></div><div class='xr-var-data'><pre>array([b&#x27;Primary sampling: averaged []                                                                                                                                                                                                                                   &#x27;,
           b&#x27;Primary sampling: averaged []                                                                                                                                                                                                                                   &#x27;,
           b&#x27;Primary sampling: averaged []                                                                                                                                                                                                                                   &#x27;,
           ...,
           b&#x27;Primary sampling: averaged []                                                                                                                                                                                                                                   &#x27;,
           b&#x27;Primary sampling: averaged []                                                                                                                                                                                                                                   &#x27;,
           b&#x27;Primary sampling: averaged []                                                                                                                                                                                                                                   &#x27;],
          dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>CONFIG_MISSION_NUMBER</span></div><div class='xr-var-dims'>(N_PROF)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-b9ac6354-d060-4c5d-9d6f-280bfc9fee08' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-b9ac6354-d060-4c5d-9d6f-280bfc9fee08' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-234f14d3-3b47-41dd-a439-88603d003c96' class='xr-var-data-in' type='checkbox'><label for='data-234f14d3-3b47-41dd-a439-88603d003c96' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Unique number denoting the missions performed by the float</dd><dt><span>conventions :</span></dt><dd>1...N, 1 : first complete mission</dd></dl></div><div class='xr-var-data'><pre>array([1., 1., 1., ..., 1., 1., 1.])</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>PRES</span></div><div class='xr-var-dims'>(N_PROF, N_LEVELS)</div><div class='xr-var-dtype'>float32</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-f8372e2d-bce2-4354-8f37-f82daf032b2f' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-f8372e2d-bce2-4354-8f37-f82daf032b2f' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-ca3972eb-f911-4576-836e-b859d4ed78dc' class='xr-var-data-in' type='checkbox'><label for='data-ca3972eb-f911-4576-836e-b859d4ed78dc' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Sea water pressure, equals 0 at sea-level</dd><dt><span>standard_name :</span></dt><dd>sea_water_pressure</dd><dt><span>units :</span></dt><dd>decibar</dd><dt><span>valid_min :</span></dt><dd>0.0</dd><dt><span>valid_max :</span></dt><dd>12000.0</dd><dt><span>C_format :</span></dt><dd>%7.1f</dd><dt><span>FORTRAN_format :</span></dt><dd>F7.1</dd><dt><span>resolution :</span></dt><dd>1.0</dd><dt><span>axis :</span></dt><dd>Z</dd></dl></div><div class='xr-var-data'><pre>[201798 values with dtype=float32]</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>PRES_QC</span></div><div class='xr-var-dims'>(N_PROF, N_LEVELS)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-f7639cc0-43a7-4c3e-8960-13cee4e3d8f5' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-f7639cc0-43a7-4c3e-8960-13cee4e3d8f5' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-2c9d989c-5cd8-430f-b6b3-3c9662fcf884' class='xr-var-data-in' type='checkbox'><label for='data-2c9d989c-5cd8-430f-b6b3-3c9662fcf884' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>quality flag</dd><dt><span>conventions :</span></dt><dd>Argo reference table 2</dd></dl></div><div class='xr-var-data'><pre>[201798 values with dtype=object]</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>PRES_ADJUSTED</span></div><div class='xr-var-dims'>(N_PROF, N_LEVELS)</div><div class='xr-var-dtype'>float32</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-7d1bd76e-ccf4-44b6-83fc-e3fbca3ff9da' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-7d1bd76e-ccf4-44b6-83fc-e3fbca3ff9da' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-d78ffc90-8a5e-4265-a953-fd27ad575a39' class='xr-var-data-in' type='checkbox'><label for='data-d78ffc90-8a5e-4265-a953-fd27ad575a39' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Sea water pressure, equals 0 at sea-level</dd><dt><span>standard_name :</span></dt><dd>sea_water_pressure</dd><dt><span>units :</span></dt><dd>decibar</dd><dt><span>valid_min :</span></dt><dd>0.0</dd><dt><span>valid_max :</span></dt><dd>12000.0</dd><dt><span>C_format :</span></dt><dd>%7.1f</dd><dt><span>FORTRAN_format :</span></dt><dd>F7.1</dd><dt><span>resolution :</span></dt><dd>1.0</dd><dt><span>axis :</span></dt><dd>Z</dd></dl></div><div class='xr-var-data'><pre>[201798 values with dtype=float32]</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>PRES_ADJUSTED_QC</span></div><div class='xr-var-dims'>(N_PROF, N_LEVELS)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-d76c816e-b723-4abd-a41e-fc6c6ce5d1a7' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-d76c816e-b723-4abd-a41e-fc6c6ce5d1a7' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-e22a4e21-f42d-4371-b17a-f90f7b6b8722' class='xr-var-data-in' type='checkbox'><label for='data-e22a4e21-f42d-4371-b17a-f90f7b6b8722' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>quality flag</dd><dt><span>conventions :</span></dt><dd>Argo reference table 2</dd></dl></div><div class='xr-var-data'><pre>[201798 values with dtype=object]</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>PRES_ADJUSTED_ERROR</span></div><div class='xr-var-dims'>(N_PROF, N_LEVELS)</div><div class='xr-var-dtype'>float32</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-9798fe71-f609-4fd1-81cd-b83e0cfd3d2d' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-9798fe71-f609-4fd1-81cd-b83e0cfd3d2d' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-f45cf181-32a7-4ab1-aff9-c55aee80d58a' class='xr-var-data-in' type='checkbox'><label for='data-f45cf181-32a7-4ab1-aff9-c55aee80d58a' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Contains the error on the adjusted values as determined by the delayed mode QC process</dd><dt><span>units :</span></dt><dd>decibar</dd><dt><span>C_format :</span></dt><dd>%7.1f</dd><dt><span>FORTRAN_format :</span></dt><dd>F7.1</dd><dt><span>resolution :</span></dt><dd>1.0</dd></dl></div><div class='xr-var-data'><pre>[201798 values with dtype=float32]</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>TEMP</span></div><div class='xr-var-dims'>(N_PROF, N_LEVELS)</div><div class='xr-var-dtype'>float32</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-f1cec51b-99be-4ed6-bae4-ae3765a6f0d5' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-f1cec51b-99be-4ed6-bae4-ae3765a6f0d5' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-4bcf48c8-3447-462d-9881-fd1f686a9555' class='xr-var-data-in' type='checkbox'><label for='data-4bcf48c8-3447-462d-9881-fd1f686a9555' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Sea temperature in-situ ITS-90 scale</dd><dt><span>standard_name :</span></dt><dd>sea_water_temperature</dd><dt><span>units :</span></dt><dd>degree_Celsius</dd><dt><span>valid_min :</span></dt><dd>-2.5</dd><dt><span>valid_max :</span></dt><dd>40.0</dd><dt><span>C_format :</span></dt><dd>%9.3f</dd><dt><span>FORTRAN_format :</span></dt><dd>F9.3</dd><dt><span>resolution :</span></dt><dd>0.001</dd></dl></div><div class='xr-var-data'><pre>[201798 values with dtype=float32]</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>TEMP_QC</span></div><div class='xr-var-dims'>(N_PROF, N_LEVELS)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-5deed6b1-eef8-4f0e-bead-486915d1c55c' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-5deed6b1-eef8-4f0e-bead-486915d1c55c' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-b3af97be-136c-4023-a95a-3ec0c3da13c6' class='xr-var-data-in' type='checkbox'><label for='data-b3af97be-136c-4023-a95a-3ec0c3da13c6' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>quality flag</dd><dt><span>conventions :</span></dt><dd>Argo reference table 2</dd></dl></div><div class='xr-var-data'><pre>[201798 values with dtype=object]</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>TEMP_ADJUSTED</span></div><div class='xr-var-dims'>(N_PROF, N_LEVELS)</div><div class='xr-var-dtype'>float32</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-8a2c993e-8e6a-4001-9085-b05e1957d1fc' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-8a2c993e-8e6a-4001-9085-b05e1957d1fc' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-211f3616-dcb2-4924-be34-1fbcf7c568d7' class='xr-var-data-in' type='checkbox'><label for='data-211f3616-dcb2-4924-be34-1fbcf7c568d7' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Sea temperature in-situ ITS-90 scale</dd><dt><span>standard_name :</span></dt><dd>sea_water_temperature</dd><dt><span>units :</span></dt><dd>degree_Celsius</dd><dt><span>valid_min :</span></dt><dd>-2.5</dd><dt><span>valid_max :</span></dt><dd>40.0</dd><dt><span>C_format :</span></dt><dd>%9.3f</dd><dt><span>FORTRAN_format :</span></dt><dd>F9.3</dd><dt><span>resolution :</span></dt><dd>0.001</dd></dl></div><div class='xr-var-data'><pre>[201798 values with dtype=float32]</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>TEMP_ADJUSTED_QC</span></div><div class='xr-var-dims'>(N_PROF, N_LEVELS)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-d56a466d-e1b7-4e53-86c3-6115ad2b5d61' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-d56a466d-e1b7-4e53-86c3-6115ad2b5d61' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-f0f721b4-7eff-416e-94b5-cf85dd50034d' class='xr-var-data-in' type='checkbox'><label for='data-f0f721b4-7eff-416e-94b5-cf85dd50034d' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>quality flag</dd><dt><span>conventions :</span></dt><dd>Argo reference table 2</dd></dl></div><div class='xr-var-data'><pre>[201798 values with dtype=object]</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>TEMP_ADJUSTED_ERROR</span></div><div class='xr-var-dims'>(N_PROF, N_LEVELS)</div><div class='xr-var-dtype'>float32</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-de28608c-a716-49ef-9974-0500b46e7ab4' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-de28608c-a716-49ef-9974-0500b46e7ab4' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-c71db45c-e625-483c-a17e-599bcb50735c' class='xr-var-data-in' type='checkbox'><label for='data-c71db45c-e625-483c-a17e-599bcb50735c' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Contains the error on the adjusted values as determined by the delayed mode QC process</dd><dt><span>units :</span></dt><dd>degree_Celsius</dd><dt><span>C_format :</span></dt><dd>%9.3f</dd><dt><span>FORTRAN_format :</span></dt><dd>F9.3</dd><dt><span>resolution :</span></dt><dd>0.001</dd></dl></div><div class='xr-var-data'><pre>[201798 values with dtype=float32]</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>PSAL</span></div><div class='xr-var-dims'>(N_PROF, N_LEVELS)</div><div class='xr-var-dtype'>float32</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-e7b80408-003e-43f6-a5bb-cd69e61ae655' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-e7b80408-003e-43f6-a5bb-cd69e61ae655' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-6d583c81-c4c7-4d03-a538-6205a4ecf047' class='xr-var-data-in' type='checkbox'><label for='data-6d583c81-c4c7-4d03-a538-6205a4ecf047' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Practical salinity</dd><dt><span>standard_name :</span></dt><dd>sea_water_salinity</dd><dt><span>units :</span></dt><dd>psu</dd><dt><span>valid_min :</span></dt><dd>2.0</dd><dt><span>valid_max :</span></dt><dd>41.0</dd><dt><span>C_format :</span></dt><dd>%9.3f</dd><dt><span>FORTRAN_format :</span></dt><dd>F9.3</dd><dt><span>resolution :</span></dt><dd>0.001</dd></dl></div><div class='xr-var-data'><pre>[201798 values with dtype=float32]</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>PSAL_QC</span></div><div class='xr-var-dims'>(N_PROF, N_LEVELS)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-82ca3d26-71da-4ec2-8cc6-f0ba2f2c87e6' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-82ca3d26-71da-4ec2-8cc6-f0ba2f2c87e6' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-f4315e8e-8221-4354-ae09-cfcd967771b3' class='xr-var-data-in' type='checkbox'><label for='data-f4315e8e-8221-4354-ae09-cfcd967771b3' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>quality flag</dd><dt><span>conventions :</span></dt><dd>Argo reference table 2</dd></dl></div><div class='xr-var-data'><pre>[201798 values with dtype=object]</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>PSAL_ADJUSTED</span></div><div class='xr-var-dims'>(N_PROF, N_LEVELS)</div><div class='xr-var-dtype'>float32</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-376108d1-2e32-4799-a6e2-2ad0bfe78be3' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-376108d1-2e32-4799-a6e2-2ad0bfe78be3' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-63b4543b-71aa-4889-bc4a-7725071a6d26' class='xr-var-data-in' type='checkbox'><label for='data-63b4543b-71aa-4889-bc4a-7725071a6d26' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Practical salinity</dd><dt><span>standard_name :</span></dt><dd>sea_water_salinity</dd><dt><span>units :</span></dt><dd>psu</dd><dt><span>valid_min :</span></dt><dd>2.0</dd><dt><span>valid_max :</span></dt><dd>41.0</dd><dt><span>C_format :</span></dt><dd>%9.3f</dd><dt><span>FORTRAN_format :</span></dt><dd>F9.3</dd><dt><span>resolution :</span></dt><dd>0.001</dd></dl></div><div class='xr-var-data'><pre>[201798 values with dtype=float32]</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>PSAL_ADJUSTED_QC</span></div><div class='xr-var-dims'>(N_PROF, N_LEVELS)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-288ffa51-4567-4856-8f37-5983c7dedff5' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-288ffa51-4567-4856-8f37-5983c7dedff5' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-cc6ee5bd-a57a-4243-bf77-e7a1011dd450' class='xr-var-data-in' type='checkbox'><label for='data-cc6ee5bd-a57a-4243-bf77-e7a1011dd450' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>quality flag</dd><dt><span>conventions :</span></dt><dd>Argo reference table 2</dd></dl></div><div class='xr-var-data'><pre>[201798 values with dtype=object]</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>PSAL_ADJUSTED_ERROR</span></div><div class='xr-var-dims'>(N_PROF, N_LEVELS)</div><div class='xr-var-dtype'>float32</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-2e9fdacd-220f-4060-ba88-b62560f2635a' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-2e9fdacd-220f-4060-ba88-b62560f2635a' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-4fee1cc6-a4dd-471e-891e-2629e98fb9ad' class='xr-var-data-in' type='checkbox'><label for='data-4fee1cc6-a4dd-471e-891e-2629e98fb9ad' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Contains the error on the adjusted values as determined by the delayed mode QC process</dd><dt><span>units :</span></dt><dd>psu</dd><dt><span>C_format :</span></dt><dd>%9.3f</dd><dt><span>FORTRAN_format :</span></dt><dd>F9.3</dd><dt><span>resolution :</span></dt><dd>0.001</dd></dl></div><div class='xr-var-data'><pre>[201798 values with dtype=float32]</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>PARAMETER</span></div><div class='xr-var-dims'>(N_PROF, N_CALIB, N_PARAM)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-93db34bb-3c96-44fe-9305-6693eacec5a8' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-93db34bb-3c96-44fe-9305-6693eacec5a8' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-1f7e4245-f143-4a34-9e30-26f918951c98' class='xr-var-data-in' type='checkbox'><label for='data-1f7e4245-f143-4a34-9e30-26f918951c98' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>List of parameters with calibration information</dd><dt><span>conventions :</span></dt><dd>Argo reference table 3</dd></dl></div><div class='xr-var-data'><pre>array([[[b&#x27;PRES            &#x27;, b&#x27;TEMP            &#x27;, b&#x27;PSAL            &#x27;]],
    
           [[b&#x27;PRES            &#x27;, b&#x27;TEMP            &#x27;, b&#x27;PSAL            &#x27;]],
    
           ...,
    
           [[b&#x27;PRES            &#x27;, b&#x27;TEMP            &#x27;, b&#x27;PSAL            &#x27;]],
    
           [[b&#x27;PRES            &#x27;, b&#x27;TEMP            &#x27;, b&#x27;PSAL            &#x27;]]],
          dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>SCIENTIFIC_CALIB_EQUATION</span></div><div class='xr-var-dims'>(N_PROF, N_CALIB, N_PARAM)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-766b80c5-8904-42b2-91f9-e84a6a0a9a77' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-766b80c5-8904-42b2-91f9-e84a6a0a9a77' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-1fa1910d-9f00-4347-a0ab-be1982bc56e3' class='xr-var-data-in' type='checkbox'><label for='data-1fa1910d-9f00-4347-a0ab-be1982bc56e3' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Calibration equation for this parameter</dd></dl></div><div class='xr-var-data'><pre>array([[[b&#x27;PRES_ADJUSTED = PRES - [PRES_SurfaceOffsetNotTruncated_dbar]                                                                                                                                                                                                    &#x27;,
             b&#x27;no change                                                                                                                                                                                                                                                       &#x27;,
             b&#x27;PSAL_ADJUSTED = sal(CNDC,TEMP,PRES_ADJUSTED); PSAL_ADJ corrects conductivity cell thermal mass (CTM), Johnson et al, 2007, JAOT                                                                                                                                 &#x27;]],
    
           [[b&#x27;PRES_ADJUSTED = PRES - [PRES_SurfaceOffsetNotTruncated_dbar]                                                                                                                                                                                                    &#x27;,
             b&#x27;no change                                                                                                                                                                                                                                                       &#x27;,
             b&#x27;PSAL_ADJUSTED = sal(CNDC,TEMP,PRES_ADJUSTED); PSAL_ADJ corrects conductivity cell thermal mass (CTM), Johnson et al, 2007, JAOT                                                                                                                                 &#x27;]],
    
           ...,
    
           [[b&#x27;PRES_ADJUSTED = PRES - [PRES_SurfaceOffsetNotTruncated_dbar]                                                                                                                                                                                                    &#x27;,
             b&#x27;no change                                                                                                                                                                                                                                                       &#x27;,
             b&#x27;PSAL_ADJUSTED = sal(CNDC,TEMP,PRES_ADJUSTED); PSAL_ADJ corrects conductivity cell thermal mass (CTM), Johnson et al, 2007, JAOT                                                                                                                                 &#x27;]],
    
           [[b&#x27;PRES_ADJUSTED = PRES - [PRES_SurfaceOffsetNotTruncated_dbar]                                                                                                                                                                                                    &#x27;,
             b&#x27;no change                                                                                                                                                                                                                                                       &#x27;,
             b&#x27;PSAL_ADJUSTED = sal(CNDC,TEMP,PRES_ADJUSTED); PSAL_ADJ corrects conductivity cell thermal mass (CTM), Johnson et al, 2007, JAOT                                                                                                                                 &#x27;]]],
          dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>SCIENTIFIC_CALIB_COEFFICIENT</span></div><div class='xr-var-dims'>(N_PROF, N_CALIB, N_PARAM)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-2844243e-ab0a-4a37-80f1-8f0ea390ec55' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-2844243e-ab0a-4a37-80f1-8f0ea390ec55' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-7bfcf4ba-10ed-4dfc-b4c5-2bb09fef3ea4' class='xr-var-data-in' type='checkbox'><label for='data-7bfcf4ba-10ed-4dfc-b4c5-2bb09fef3ea4' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Calibration coefficients for this equation</dd></dl></div><div class='xr-var-data'><pre>array([[[b&#x27;PRES_SurfaceOffsetNotTruncated_dbar in TECH file for N-1 profile                                                                                                                                                                                                &#x27;,
             b&#x27;no change                                                                                                                                                                                                                                                       &#x27;,
             b&#x27;same as for PRES_ADJUSTED; CTL: alpha=0.1410, tau=6.68; pcond = 1.0000                                                                                                                                                                                          &#x27;]],
    
           [[b&#x27;PRES_SurfaceOffsetNotTruncated_dbar in TECH file for N-1 profile                                                                                                                                                                                                &#x27;,
             b&#x27;no change                                                                                                                                                                                                                                                       &#x27;,
             b&#x27;same as for PRES_ADJUSTED; CTL: alpha=0.1410, tau=6.68; pcond = 1.0000                                                                                                                                                                                          &#x27;]],
    
           ...,
    
           [[b&#x27;PRES_SurfaceOffsetNotTruncated_dbar in TECH file for N-1 profile                                                                                                                                                                                                &#x27;,
             b&#x27;no change                                                                                                                                                                                                                                                       &#x27;,
             b&#x27;same as for PRES_ADJUSTED; CTL: alpha=0.1410, tau=6.68; pcond = NaN                                                                                                                                                                                             &#x27;]],
    
           [[b&#x27;PRES_SurfaceOffsetNotTruncated_dbar in TECH file for N-1 profile                                                                                                                                                                                                &#x27;,
             b&#x27;no change                                                                                                                                                                                                                                                       &#x27;,
             b&#x27;same as for PRES_ADJUSTED; CTL: alpha=0.1410, tau=6.68; pcond = NaN                                                                                                                                                                                             &#x27;]]],
          dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>SCIENTIFIC_CALIB_COMMENT</span></div><div class='xr-var-dims'>(N_PROF, N_CALIB, N_PARAM)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-b9a5bb3e-eb29-4495-81a3-bf60481778fe' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-b9a5bb3e-eb29-4495-81a3-bf60481778fe' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-01b36ae2-ff47-448a-b258-73accbb3bed6' class='xr-var-data-in' type='checkbox'><label for='data-01b36ae2-ff47-448a-b258-73accbb3bed6' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Comment applying to this parameter calibration</dd></dl></div><div class='xr-var-data'><pre>array([[[b&#x27;Pressures adjusted using PRES_SurfaceOffsetNotTruncated_dbar; Pressure drift corrected; Manufacturers sensor accuracy                                                                                                                                           &#x27;,
             b&#x27;No significant temperature drift detected; Manufacturers sensor accuracy;                                                                                                                                                                                       &#x27;,
             b&#x27;Salinity drift/offset - correction applied using OW piecewise-fit based on deep theta levels and Argo and CTD reference datasets.                                                                                                                               &#x27;]],
    
           [[b&#x27;Pressures adjusted using PRES_SurfaceOffsetNotTruncated_dbar; Pressure drift corrected; Manufacturers sensor accuracy                                                                                                                                           &#x27;,
             b&#x27;No significant temperature drift detected; Manufacturers sensor accuracy;                                                                                                                                                                                       &#x27;,
             b&#x27;Salinity drift/offset - correction applied using OW piecewise-fit based on deep theta levels and Argo and CTD reference datasets.                                                                                                                               &#x27;]],
    
           ...,
    
           [[b&#x27;Pressures adjusted using PRES_SurfaceOffsetNotTruncated_dbar; Pressure drift corrected; Manufacturers sensor accuracy                                                                                                                                           &#x27;,
             b&#x27;No significant temperature drift detected; Manufacturers sensor accuracy;                                                                                                                                                                                       &#x27;,
             b&#x27;Anomalous salinity data, cannot be corrected                                                                                                                                                                                                                    &#x27;]],
    
           [[b&#x27;Pressures adjusted using PRES_SurfaceOffsetNotTruncated_dbar; Pressure drift corrected; Manufacturers sensor accuracy                                                                                                                                           &#x27;,
             b&#x27;No significant temperature drift detected; Manufacturers sensor accuracy;                                                                                                                                                                                       &#x27;,
             b&#x27;Anomalous salinity data, cannot be corrected                                                                                                                                                                                                                    &#x27;]]],
          dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>SCIENTIFIC_CALIB_DATE</span></div><div class='xr-var-dims'>(N_PROF, N_CALIB, N_PARAM)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-fbdbcb66-97db-4fff-9fcd-e5ef2ea6fce3' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-fbdbcb66-97db-4fff-9fcd-e5ef2ea6fce3' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-765a5ac1-ea3b-4005-970e-dd657dd12bdc' class='xr-var-data-in' type='checkbox'><label for='data-765a5ac1-ea3b-4005-970e-dd657dd12bdc' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Date of calibration</dd><dt><span>conventions :</span></dt><dd>YYYYMMDDHHMISS</dd></dl></div><div class='xr-var-data'><pre>array([[[b&#x27;20210803061803&#x27;, b&#x27;20210803061803&#x27;, b&#x27;20210803061803&#x27;]],
    
           [[b&#x27;20210803061803&#x27;, b&#x27;20210803061803&#x27;, b&#x27;20210803061803&#x27;]],
    
           ...,
    
           [[b&#x27;20210803061803&#x27;, b&#x27;20210803061803&#x27;, b&#x27;20210803061803&#x27;]],
    
           [[b&#x27;20210803061803&#x27;, b&#x27;20210803061803&#x27;, b&#x27;20210803061803&#x27;]]],
          dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>HISTORY_INSTITUTION</span></div><div class='xr-var-dims'>(N_HISTORY, N_PROF)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-658ad41a-8042-410b-9f73-322f53ba6346' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-658ad41a-8042-410b-9f73-322f53ba6346' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-275c3a55-10e6-403f-9763-157d273fd719' class='xr-var-data-in' type='checkbox'><label for='data-275c3a55-10e6-403f-9763-157d273fd719' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Institution which performed action</dd><dt><span>conventions :</span></dt><dd>Argo reference table 4</dd></dl></div><div class='xr-var-data'><pre>array([], shape=(0, 202), dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>HISTORY_STEP</span></div><div class='xr-var-dims'>(N_HISTORY, N_PROF)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-59deedfd-cbe1-497f-8536-8131a4598c72' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-59deedfd-cbe1-497f-8536-8131a4598c72' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-29d15d18-1e4f-4431-aad9-5a02ac2e75a2' class='xr-var-data-in' type='checkbox'><label for='data-29d15d18-1e4f-4431-aad9-5a02ac2e75a2' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Step in data processing</dd><dt><span>conventions :</span></dt><dd>Argo reference table 12</dd></dl></div><div class='xr-var-data'><pre>array([], shape=(0, 202), dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>HISTORY_SOFTWARE</span></div><div class='xr-var-dims'>(N_HISTORY, N_PROF)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-6f85c080-dd3f-4918-a3e5-30c26f1b1811' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-6f85c080-dd3f-4918-a3e5-30c26f1b1811' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-62aa1ad6-15f8-40a6-a7b2-906939e30d00' class='xr-var-data-in' type='checkbox'><label for='data-62aa1ad6-15f8-40a6-a7b2-906939e30d00' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Name of software which performed action</dd><dt><span>conventions :</span></dt><dd>Institution dependent</dd></dl></div><div class='xr-var-data'><pre>array([], shape=(0, 202), dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>HISTORY_SOFTWARE_RELEASE</span></div><div class='xr-var-dims'>(N_HISTORY, N_PROF)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-9d5cd4c0-cf46-4c6e-b8ee-a1e227e5c51f' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-9d5cd4c0-cf46-4c6e-b8ee-a1e227e5c51f' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-fcbf97b7-d6a7-45ea-8314-433eaac6fad0' class='xr-var-data-in' type='checkbox'><label for='data-fcbf97b7-d6a7-45ea-8314-433eaac6fad0' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Version/release of software which performed action</dd><dt><span>conventions :</span></dt><dd>Institution dependent</dd></dl></div><div class='xr-var-data'><pre>array([], shape=(0, 202), dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>HISTORY_REFERENCE</span></div><div class='xr-var-dims'>(N_HISTORY, N_PROF)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-c65a2ace-b0fd-4147-992d-ff58a82139e4' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-c65a2ace-b0fd-4147-992d-ff58a82139e4' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-de32a2ad-c600-4278-90e0-f65c0cabc332' class='xr-var-data-in' type='checkbox'><label for='data-de32a2ad-c600-4278-90e0-f65c0cabc332' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Reference of database</dd><dt><span>conventions :</span></dt><dd>Institution dependent</dd></dl></div><div class='xr-var-data'><pre>array([], shape=(0, 202), dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>HISTORY_DATE</span></div><div class='xr-var-dims'>(N_HISTORY, N_PROF)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-05f74198-bb32-4142-bef9-55935224a59c' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-05f74198-bb32-4142-bef9-55935224a59c' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-e9608669-56cc-4aae-b6d0-b2e574af7590' class='xr-var-data-in' type='checkbox'><label for='data-e9608669-56cc-4aae-b6d0-b2e574af7590' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Date the history record was created</dd><dt><span>conventions :</span></dt><dd>YYYYMMDDHHMISS</dd></dl></div><div class='xr-var-data'><pre>array([], shape=(0, 202), dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>HISTORY_ACTION</span></div><div class='xr-var-dims'>(N_HISTORY, N_PROF)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-8ada3d8a-56ed-4bf1-9a01-9cf0d0637c7d' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-8ada3d8a-56ed-4bf1-9a01-9cf0d0637c7d' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-3cd87e73-2b90-40e7-a495-26176f35fb0e' class='xr-var-data-in' type='checkbox'><label for='data-3cd87e73-2b90-40e7-a495-26176f35fb0e' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Action performed on data</dd><dt><span>conventions :</span></dt><dd>Argo reference table 7</dd></dl></div><div class='xr-var-data'><pre>array([], shape=(0, 202), dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>HISTORY_PARAMETER</span></div><div class='xr-var-dims'>(N_HISTORY, N_PROF)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-0ae21b5b-e599-4c25-83b3-1edfca3f1efe' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-0ae21b5b-e599-4c25-83b3-1edfca3f1efe' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-08cfc070-264c-4286-86b5-35e2c5eb8b69' class='xr-var-data-in' type='checkbox'><label for='data-08cfc070-264c-4286-86b5-35e2c5eb8b69' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Station parameter action is performed on</dd><dt><span>conventions :</span></dt><dd>Argo reference table 3</dd></dl></div><div class='xr-var-data'><pre>array([], shape=(0, 202), dtype=object)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>HISTORY_START_PRES</span></div><div class='xr-var-dims'>(N_HISTORY, N_PROF)</div><div class='xr-var-dtype'>float32</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-6f2e5eb7-667d-4b29-bd1b-fec441676591' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-6f2e5eb7-667d-4b29-bd1b-fec441676591' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-277d01c9-d96a-4898-aee1-6ecb79e6bfd7' class='xr-var-data-in' type='checkbox'><label for='data-277d01c9-d96a-4898-aee1-6ecb79e6bfd7' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Start pressure action applied on</dd><dt><span>units :</span></dt><dd>decibar</dd></dl></div><div class='xr-var-data'><pre>array([], shape=(0, 202), dtype=float32)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>HISTORY_STOP_PRES</span></div><div class='xr-var-dims'>(N_HISTORY, N_PROF)</div><div class='xr-var-dtype'>float32</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-b3f50922-c779-432b-bdfc-4c2e58d75c57' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-b3f50922-c779-432b-bdfc-4c2e58d75c57' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-5856695b-6fcf-4cb5-8e1e-418bdf853c74' class='xr-var-data-in' type='checkbox'><label for='data-5856695b-6fcf-4cb5-8e1e-418bdf853c74' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Stop pressure action applied on</dd><dt><span>units :</span></dt><dd>decibar</dd></dl></div><div class='xr-var-data'><pre>array([], shape=(0, 202), dtype=float32)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>HISTORY_PREVIOUS_VALUE</span></div><div class='xr-var-dims'>(N_HISTORY, N_PROF)</div><div class='xr-var-dtype'>float32</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-3c28232c-69d3-49b4-9936-08e51fdaa381' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-3c28232c-69d3-49b4-9936-08e51fdaa381' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-85137dfa-23b7-44f8-9f74-967ec8600946' class='xr-var-data-in' type='checkbox'><label for='data-85137dfa-23b7-44f8-9f74-967ec8600946' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Parameter/Flag previous value before action</dd></dl></div><div class='xr-var-data'><pre>array([], shape=(0, 202), dtype=float32)</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>HISTORY_QCTEST</span></div><div class='xr-var-dims'>(N_HISTORY, N_PROF)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-07ff2e62-5cee-4904-9474-91c5698458ce' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-07ff2e62-5cee-4904-9474-91c5698458ce' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-7da7878b-2dff-4eba-957e-c86b0f7db35a' class='xr-var-data-in' type='checkbox'><label for='data-7da7878b-2dff-4eba-957e-c86b0f7db35a' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>long_name :</span></dt><dd>Documentation of tests performed, tests failed (in hex form)</dd><dt><span>conventions :</span></dt><dd>Write tests performed when ACTION=QCP$; tests failed when ACTION=QCF$</dd></dl></div><div class='xr-var-data'><pre>array([], shape=(0, 202), dtype=object)</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-215b914b-f222-4d55-aef8-1f1d6996240c' class='xr-section-summary-in' type='checkbox'  checked><label for='section-215b914b-f222-4d55-aef8-1f1d6996240c' class='xr-section-summary' >Attributes: <span>(8)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><dl class='xr-attrs'><dt><span>title :</span></dt><dd>Argo float vertical profile</dd><dt><span>institution :</span></dt><dd>FR GDAC</dd><dt><span>source :</span></dt><dd>Argo float</dd><dt><span>history :</span></dt><dd>2021-08-03T08:16:48Z creation</dd><dt><span>references :</span></dt><dd>http://www.argodatamgt.org/Documentation</dd><dt><span>user_manual_version :</span></dt><dd>3.1</dd><dt><span>Conventions :</span></dt><dd>Argo-3.1 CF-1.6</dd><dt><span>featureType :</span></dt><dd>trajectoryProfile</dd></dl></div></li></ul></div></div>



.. code:: 

    plt.figure(figsize=(12,6),dpi=300)
    ax = plt.axes(projection=ccrs.PlateCarree())
    plt.rcParams['font.size'] = '24'
    plt.rcParams['font.weight'] = 'bold'
    plt.rcParams['figure.figsize'] = [10,6]
    
    # Gridlines
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                      linewidth=1, color='gray', alpha=0.5, linestyle='--')
    gl.xlabels_top = False
    gl.ylabels_right = False
    #gl.xlocator = mticker.MaxNLocator(7)
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    
    map = Basemap(llcrnrlon=102.5,llcrnrlat=-15,
                  urcrnrlon=117.,urcrnrlat=-1,
                  resolution='i', lat_0 = -19, lon_0 = 1)
    
    map.drawmapboundary(fill_color='white')
    map.fillcontinents(color='grey',lake_color='aqua')
    map.drawcoastlines()
    
    # Set the aspect ratio to pseudo-Mercator
    plt.gca().set_aspect(1 / np.cos(np.deg2rad( np.mean(plt.ylim()) )))
    
    # Simple map of a float track
    map.plot(data.LONGITUDE, data.LATITUDE, c='lightgrey')
    map.scatter(data.LONGITUDE, data.LATITUDE, c=data.JULD, cmap='RdYlBu_r')
    
    cbar = plt.colorbar(pad=0.01,aspect=20,
                        shrink=0.9)
    #cbar = plt.colorbar(pad=0.02)
    #cbar = plt.colorbar(im,fraction=0.046, pad=0.04);
    
    # Fix the colorbar ticks
    cbar.ax.set_yticklabels(pd.to_datetime(
                            cbar.get_ticks()).strftime(date_format='%Y',),
                           size=22,weight='bold',);
    
    #                        (cbar.get_ticks()).strftime(
    #                            date_format='%Y-%m-%d'),size=16,weight='bold');
    
    plt.title('Trajectory map of Argo #%d' % (
        data.PLATFORM_NUMBER[1].values),
              fontweight='bold',size=20);
    #plt.title('Argo Float #%d on %s' % (data.PLATFORM_NUMBER[nprof].values, data.JULD[nprof].dt.strftime('%Y-%m-%d').values), fontweight='bold');
    
    #ax.plot(data.LONGITUDE, data.LATITUDE, linewidth=1, color='royalblue');
    plt.show()
    
    # Set the aspect ratio to pseudo-Mercator
    #plt.gca().set_aspect(1 / np.cos(np.deg2rad( np.mean(plt.ylim()) )))
    
    plt.savefig("argo5905017_map.png")


.. parsed-literal::

    /home/lenovo/miniconda3/envs/envplot/lib/python3.10/site-packages/cartopy/mpl/gridliner.py:451: UserWarning: The .xlabels_top attribute is deprecated. Please use .top_labels to toggle visibility instead.
      warnings.warn('The .xlabels_top attribute is deprecated. Please '
    /home/lenovo/miniconda3/envs/envplot/lib/python3.10/site-packages/cartopy/mpl/gridliner.py:487: UserWarning: The .ylabels_right attribute is deprecated. Please use .right_labels to toggle visibility instead.
      warnings.warn('The .ylabels_right attribute is deprecated. Please '
    /tmp/ipykernel_10019/1442338318.py:37: UserWarning: FixedFormatter should only be used together with FixedLocator
      cbar.ax.set_yticklabels(pd.to_datetime(



.. figure:: /images/output_13_1.png
   :alt: alt text goes here
   :align: center
   :width: 800px
   


.. parsed-literal::

    <Figure size 1000x600 with 0 Axes>


.. code:: 

    timestamps = data['JULD'].values
    # Stack NumPy array of datetimes to create a 2D grid
    time_2D = np.tile(data['JULD'].values,(len(data['N_LEVELS']),1)).T
    time_2D




.. parsed-literal::

    array([['2016-01-07T22:06:34.000000000', '2016-01-07T22:06:34.000000000',
            '2016-01-07T22:06:34.000000000', ...,
            '2016-01-07T22:06:34.000000000', '2016-01-07T22:06:34.000000000',
            '2016-01-07T22:06:34.000000000'],
           ['2016-01-17T15:35:41.000000000', '2016-01-17T15:35:41.000000000',
            '2016-01-17T15:35:41.000000000', ...,
            '2016-01-17T15:35:41.000000000', '2016-01-17T15:35:41.000000000',
            '2016-01-17T15:35:41.000000000'],
           ['2016-01-27T09:41:07.000000000', '2016-01-27T09:41:07.000000000',
            '2016-01-27T09:41:07.000000000', ...,
            '2016-01-27T09:41:07.000000000', '2016-01-27T09:41:07.000000000',
            '2016-01-27T09:41:07.000000000'],
           ...,
           ['2021-05-06T13:48:53.000000000', '2021-05-06T13:48:53.000000000',
            '2021-05-06T13:48:53.000000000', ...,
            '2021-05-06T13:48:53.000000000', '2021-05-06T13:48:53.000000000',
            '2021-05-06T13:48:53.000000000'],
           ['2021-05-16T07:15:29.000000000', '2021-05-16T07:15:29.000000000',
            '2021-05-16T07:15:29.000000000', ...,
            '2021-05-16T07:15:29.000000000', '2021-05-16T07:15:29.000000000',
            '2021-05-16T07:15:29.000000000'],
           ['2021-05-26T02:10:37.000000000', '2021-05-26T02:10:37.000000000',
            '2021-05-26T02:10:37.000000000', ...,
            '2021-05-26T02:10:37.000000000', '2021-05-26T02:10:37.000000000',
            '2021-05-26T02:10:37.000000000']], dtype='datetime64[ns]')



.. code:: 

    # ---
    # 1. datetime_to_float
    # Function to convert an array from NumPy datetime64 to Python float format
    def datetime_to_float(dt):
      return (dt - np.datetime64('1900-01-01')) / np.timedelta64(1,'D')
    # ---
    
    # ---
    # 2. float_to_datetime
    # Function to convert an array from Python float to NumPy datetime64 format
    def float_to_datetime(nums):
      return (nums * np.timedelta64(1,'D')) + np.datetime64('1900-01-01')
    # ---
    
    # ---
    # 3. interpolate_depth_section
    # Function to interpolate data from a specified float parameter to a uniform time and pressure grid
    def interpolate_depth_section(param_name,specify_qc_flags=None,pres_interval=1.0):
      """
      Arguments:
          param_name: string with netCDF file parameter name (e.g., 'TEMP_ADJUSTED') to interpolate
          specify_qc_flags: None to ignore QC flags
                            or a list of QC flags (e.g., [1,2,3]) indicating which data to retain before interpolation
          pres_interval: vertical resolution for interpolating pressure (z) axis (default: 1.0 dbar)
      
      Returns:
          time_coord: 1-D NumPy array with original profile timestamps in np.datetime64 format
          pres_coord: 1-D NumPy array with a uniform pressure (z) coordinate from 0 dbar to the deepest recorded
                      pressure value, at a resolution of <pres_interval> dbar
          time_grid: 2-D NumPy array with the meshed grid of time_coord
          pres_grid: 2-D NumPy array with the meshed grid of pres_coord
          param_gridded: 2-D NumPy array with the interpolated parameter values at the locations of time_grid and pres_grid
    
      """
    
      # New grid points
      time_coord = data['JULD'].values
      pres_coord = np.arange(0,data['PRES'].max(),pres_interval)
      time_grid, pres_grid = np.meshgrid(time_coord,pres_coord)
      time_grid = datetime_to_float(time_grid)     # Convert from np.datetime64 to float
    
      # 1-D (flattened) versions of old grids and parameter values
      time_1D = np.tile(data['JULD'].values,(len(data['N_LEVELS']),1)).T.flatten()
      pres_1D = data['PRES'].values.flatten()
      param_1D = data[param_name].values.flatten()
      if param_1D.dtype == object:         # If parameter is an array of QC flag data
        param_1D = param_1D.astype(float)  # Convert QC flags from dtype 'object' to float
        interp_method = 'nearest'          # Use nearest-neighbor interpolation for QC flags to avoid unwanted averaging
      else:
        interp_method = 'linear'           # Use bilinear interpolation for normal data fields
    
      # Extract only values matching specified QC flags
      if specify_qc_flags is not None:
        qc_1D = data[param_name + '_QC'].values.astype(float).flatten()
        qc_mask = np.tile(False,len(qc_1D))
        for qc_flag in specify_qc_flags:
          qc_mask = np.logical_or(qc_mask,qc_1D == qc_flag)
        time_1D = time_1D[qc_mask]
        pres_1D = pres_1D[qc_mask]
        param_1D = param_1D[qc_mask]
    
      # Remove NaN values before interpolation
      time_1D = datetime_to_float(time_1D[~np.isnan(param_1D)])       # Convert from np.datetime64 to float
      pres_1D = pres_1D[~np.isnan(param_1D)]
      param_1D = param_1D[~np.isnan(param_1D)]
    
      # Interpolate from irregular points to grid
      param_gridded = interpolate.griddata((time_1D,pres_1D),param_1D,(time_grid,pres_grid),method=interp_method)
    
      # Return coordinates, grid, and gridded data
      return time_coord, pres_coord, float_to_datetime(time_grid), pres_grid, param_gridded
    # ---

.. code:: 

    # Function for repetitive parts of plot
    def config_depth_section0(cbar_label,title):
      plt.ylim([0,1000])
      plt.gca().invert_yaxis()
      plt.ylabel('Depth (m)',fontsize=12)
      if 'SALINITY' in cbar_label: extend = 'min'
      else:                       extend = 'neither'
      plt.colorbar(label=cbar_label,extend=extend,pad=0.02)
      plt.title(title)
    
    # Create subplots
    left = dt.date(2016, 1, 1)
    right = dt.date(2021, 5, 31)
    
    plt.figure(figsize=(16,6),dpi=300)
    
    ax1 = plt.subplot(1,1,1)
    cmap = plt.cm.get_cmap("viridis").copy()
    #cmap = plt.get_cmap('viridis')
    cmap.set_under('0.5')
    plt.pcolor(time_2D,data['PRES_ADJUSTED'].values,data['TEMP_ADJUSTED_QC'].values.astype(float),cmap='Set1',vmin=0.5,vmax=9.5)
    config_depth_section0('Temperature QC flag',"")
    plt.gca().set_xbound(left, right)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'),)



.. parsed-literal::

    /tmp/ipykernel_30818/3168967982.py:21: UserWarning: The input coordinates to pcolor are interpreted as cell centers, but are not monotonically increasing or decreasing. This may lead to incorrectly calculated cell edges, in which case, please supply explicit cell edges to pcolor.
      plt.pcolor(time_2D,data['PRES_ADJUSTED'].values,data['TEMP_ADJUSTED_QC'].values.astype(float),cmap='Set1',vmin=0.5,vmax=9.5)



.. figure:: /images/output_16_1.png
   :alt: alt text goes here
   :align: center
   :width: 800px
   


.. code:: 

    # Function for repetitive parts of plot
    def config_depth_section0(cbar_label,title):
      plt.ylim([0,1000])
      plt.gca().invert_yaxis()
      plt.ylabel('Depth (m)',fontsize=12)
      if 'SALINITY' in cbar_label: extend = 'min'
      else:                       extend = 'neither'
      plt.colorbar(label=cbar_label,extend=extend,pad=0.02)
      plt.title(title)
    
    # Create subplots
    left = dt.date(2016, 1, 1)
    right = dt.date(2021, 5, 31)
    
    plt.figure(figsize=(16,6),dpi=300)
    
    fig, (ax1,ax2) = plt.subplots(nrows=2,sharex=True,sharey=True,
                                 constrained_layout=True,)
    ax1 = plt.subplot(2,1,1)
    cmap = plt.cm.get_cmap("viridis").copy()
    #cmap = plt.get_cmap('viridis')
    cmap.set_under('0.5')
    im=plt.pcolor(time_2D,data['PRES_ADJUSTED'].values,data['TEMP_ADJUSTED_QC'].values.astype(float),cmap='Set1',vmin=0.5,vmax=9.5)
    #config_depth_section0('Temperature QC flag',"")
    plt.ylim([0,1000])
    plt.gca().invert_yaxis()
    #ax1.annotate("a)", xy=(0.01, 0.92),
    #             xycoords=ax1.transAxes,
    #             fontsize=12,color='white',weight='bold')
    
    ax2 = plt.subplot(2,1,2,)
    plt.pcolor(time_2D,data['PRES_ADJUSTED'].values,data['PSAL_ADJUSTED_QC'].values.astype(float),cmap='Set1',vmin=0.5,vmax=9.5)
    plt.ylim([0,1000])
    plt.gca().invert_yaxis()
    #ax2.annotate("b)", xy=(0.01, 0.92),
    #             xycoords=ax2.transAxes,
    #             fontsize=12,color='white',weight='bold')
    
    plt.gca().set_xbound(left, right)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'),)
    cax,kw = mpl.colorbar.make_axes([ax for ax in (ax1,ax2)],pad=0.02)
    fig.colorbar(im, cax=cax, **kw,label='QC Flag')
    fig.supylabel('Depth (m)')
    
    plt.savefig("argo5905017_QC.png")


.. parsed-literal::

    /tmp/ipykernel_10019/1069935262.py:20: MatplotlibDeprecationWarning: The get_cmap function was deprecated in Matplotlib 3.7 and will be removed two minor releases later. Use ``matplotlib.colormaps[name]`` or ``matplotlib.colormaps.get_cmap(obj)`` instead.
      cmap = plt.cm.get_cmap("viridis").copy()
    /tmp/ipykernel_10019/1069935262.py:23: UserWarning: The input coordinates to pcolor are interpreted as cell centers, but are not monotonically increasing or decreasing. This may lead to incorrectly calculated cell edges, in which case, please supply explicit cell edges to pcolor.
      im=plt.pcolor(time_2D,data['PRES_ADJUSTED'].values,data['TEMP_ADJUSTED_QC'].values.astype(float),cmap='Set1',vmin=0.5,vmax=9.5)
    /tmp/ipykernel_10019/1069935262.py:32: UserWarning: The input coordinates to pcolor are interpreted as cell centers, but are not monotonically increasing or decreasing. This may lead to incorrectly calculated cell edges, in which case, please supply explicit cell edges to pcolor.
      plt.pcolor(time_2D,data['PRES_ADJUSTED'].values,data['PSAL_ADJUSTED_QC'].values.astype(float),cmap='Set1',vmin=0.5,vmax=9.5)



.. parsed-literal::

    <Figure size 4800x1800 with 0 Axes>



.. figure:: /images/output_17_2.png
   :alt: alt text goes here
   :align: center
   :width: 800px
   


.. code:: 

    # Create subplots
    left = dt.date(2016, 1, 1)
    right = dt.date(2021, 5, 31)
    
    plt.figure(figsize=(16,6),dpi=300)
    
    fig, (ax1,ax2) = plt.subplots(nrows=2,sharex=True,
                                 constrained_layout=True,)
    ax1 = plt.subplot(2,1,1)
    cmap = plt.cm.get_cmap("hsv_r").copy()
    #cmap = plt.get_cmap('viridis')
    cmap.set_under('0.5')
    im=plt.pcolor(time_2D,data['PRES_ADJUSTED'].
               values,data['TEMP_ADJUSTED'].values.astype(float),
               cmap=cmap,vmin=0,vmax=32)
    plt.ylim([0,250])
    plt.gca().invert_yaxis()
    #ax1.annotate("(a)", xy=(0.92, 0.92),
    #             xycoords=ax1.transAxes,
    #             fontsize=12,color='black',weight='bold')
    cs1=plt.contour(time_2D,data['PRES_ADJUSTED'].values,
                data['TEMP_ADJUSTED'].values.astype(float),levels=[27],colors='k')
    ax1.clabel(cs1,inline=1,fontsize=12)
    
    
    ax2 = plt.subplot(2,1,2,)
    plt.pcolor(time_2D,data['PRES_ADJUSTED'].values,
               data['TEMP_ADJUSTED'].values.astype(float),
               cmap=cmap,vmin=0,vmax=32)
    plt.ylim([250,1000])
    plt.gca().invert_yaxis()
    
    plt.gca().set_xbound(left, right)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'),)
    cax,kw = mpl.colorbar.make_axes([ax for ax in (ax1,ax2)],pad=0.02)
    fig.colorbar(im, cax=cax, **kw,label='Temperature ($^\circ$C)')
    fig.supylabel('Depth (m)')
    
    plt.savefig("argo5905017_Tdiv.png")


.. parsed-literal::

    /tmp/ipykernel_30818/1964040261.py:13: UserWarning: The input coordinates to pcolor are interpreted as cell centers, but are not monotonically increasing or decreasing. This may lead to incorrectly calculated cell edges, in which case, please supply explicit cell edges to pcolor.
      im=plt.pcolor(time_2D,data['PRES_ADJUSTED'].
    /tmp/ipykernel_30818/1964040261.py:27: UserWarning: The input coordinates to pcolor are interpreted as cell centers, but are not monotonically increasing or decreasing. This may lead to incorrectly calculated cell edges, in which case, please supply explicit cell edges to pcolor.
      plt.pcolor(time_2D,data['PRES_ADJUSTED'].values,



.. parsed-literal::

    <Figure size 4800x1800 with 0 Axes>



.. figure:: /images/output_18_2.png
   :alt: alt text goes here
   :align: center
   :width: 800px
   

.. code:: 

    # Create subplots
    left = dt.date(2016, 1, 1)
    right = dt.date(2021, 5, 31)
    
    plt.figure(figsize=(10,6),dpi=300)
    plt.rcParams['font.size'] = '14'
    plt.figure().set_figwidth(20)
    plt.rcParams['figure.figsize'] = [6.8, 5]
    plt.rcParams['font.weight'] = 'normal'
    
    fig, (ax1,ax2) = plt.subplots(nrows=2,sharex=True,
                                 constrained_layout=True,)
    ax1 = plt.subplot(2,1,1)
    cmap = plt.cm.get_cmap("hsv_r").copy()
    #cmap = plt.get_cmap('viridis')
    cmap.set_under('0.5')
    im=plt.pcolor(time_2D,data['PRES_ADJUSTED'].
               values,data['TEMP_ADJUSTED'].values.astype(float),
               cmap=cmap,vmin=0,vmax=32)
    plt.ylim([0,250])
    plt.gca().invert_yaxis()
    #ax1.annotate("(a)", xy=(0.92, 0.92),
    #             xycoords=ax1.transAxes,
    #             fontsize=12,color='black',weight='bold')
    cs1=plt.contour(time_2D,data['PRES_ADJUSTED'].values,
                data['TEMP_ADJUSTED'].values.astype(float),levels=[27],colors='k')
    ax1.clabel(cs1,inline=1,fontsize=12)
    
    
    ax2 = plt.subplot(2,1,2,)
    plt.pcolor(time_2D,data['PRES_ADJUSTED'].values,
               data['TEMP_ADJUSTED'].values.astype(float),
               cmap=cmap,vmin=0,vmax=32)
    plt.ylim([250,1000])
    plt.gca().invert_yaxis()
    
    plt.gca().set_xbound(left, right)
    plt.gca().xaxis.set_major_locator(mdates.YearLocator(base=2))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'),)
    #plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'),)
    cax,kw = mpl.colorbar.make_axes([ax for ax in (ax1,ax2)],pad=0.02)
    fig.colorbar(im, cax=cax, **kw,label='Temperature ($^\circ$C)')
    fig.supylabel('Depth (m)',x=-0.01,y=0.5)
    
    #im2 = image.imread('argo5905017_map.png')
    #im2 = plt.imread('argo5905017_Tdiv.png')
    im2 = plt.imread('argo5905017_map.png')
    newax = fig.add_axes([0.11,0.08,0.41,0.38], anchor='NE')
    newax.imshow(im2,aspect='auto')
    newax.axis('off')
    #def place_image(im2, loc=3, ax=None, zoom=1, **kw):
    #    if ax==None: ax=plt.gca()
    #    imagebox = OffsetImage(im2, zoom=zoom*0.72)
    #    ab = AnchoredOffsetbox(loc=loc, child=imagebox, frameon=False, **kw)
    #    ax.add_artist(ab)
    #place_image(im2, loc=2, ax=newax, pad=0, zoom=1)
    plt.show()
    
    #axins = zoomed_inset_axes(ax2, zoom=0.5, loc='lower left')
    # fix the number of ticks on the inset axes
    #axins.yaxis.get_major_locator().set_params(nbins=7)
    #axins.xaxis.get_major_locator().set_params(nbins=7)
    #axins.tick_params(labelleft=True, labelbottom=True)
    
    plt.savefig("argo5905017_Tdiv-inset.png")


.. parsed-literal::

    /tmp/ipykernel_10019/3402651493.py:14: MatplotlibDeprecationWarning: The get_cmap function was deprecated in Matplotlib 3.7 and will be removed two minor releases later. Use ``matplotlib.colormaps[name]`` or ``matplotlib.colormaps.get_cmap(obj)`` instead.
      cmap = plt.cm.get_cmap("hsv_r").copy()
    /tmp/ipykernel_10019/3402651493.py:17: UserWarning: The input coordinates to pcolor are interpreted as cell centers, but are not monotonically increasing or decreasing. This may lead to incorrectly calculated cell edges, in which case, please supply explicit cell edges to pcolor.
      im=plt.pcolor(time_2D,data['PRES_ADJUSTED'].
    /tmp/ipykernel_10019/3402651493.py:31: UserWarning: The input coordinates to pcolor are interpreted as cell centers, but are not monotonically increasing or decreasing. This may lead to incorrectly calculated cell edges, in which case, please supply explicit cell edges to pcolor.
      plt.pcolor(time_2D,data['PRES_ADJUSTED'].values,



.. parsed-literal::

    <Figure size 3000x1800 with 0 Axes>



.. parsed-literal::

    <Figure size 2000x500 with 0 Axes>



.. figure:: /images/output_19_3.png
   :alt: alt text goes here
   :align: center
   :width: 800px
   


.. parsed-literal::

    <Figure size 680x500 with 0 Axes>


.. code:: 

    file="argo5905017_map.png"
    logo = image.imread(file)
    print(logo.shape); print(logo)


.. parsed-literal::

    (1652, 2138, 4)
    [[[1. 1. 1. 1.]
      [1. 1. 1. 1.]
      [1. 1. 1. 1.]
      ...
      [1. 1. 1. 1.]
      [1. 1. 1. 1.]
      [1. 1. 1. 1.]]
    
     [[1. 1. 1. 1.]
      [1. 1. 1. 1.]
      [1. 1. 1. 1.]
      ...
      [1. 1. 1. 1.]
      [1. 1. 1. 1.]
      [1. 1. 1. 1.]]
    
     [[1. 1. 1. 1.]
      [1. 1. 1. 1.]
      [1. 1. 1. 1.]
      ...
      [1. 1. 1. 1.]
      [1. 1. 1. 1.]
      [1. 1. 1. 1.]]
    
     ...
    
     [[1. 1. 1. 1.]
      [1. 1. 1. 1.]
      [1. 1. 1. 1.]
      ...
      [1. 1. 1. 1.]
      [1. 1. 1. 1.]
      [1. 1. 1. 1.]]
    
     [[1. 1. 1. 1.]
      [1. 1. 1. 1.]
      [1. 1. 1. 1.]
      ...
      [1. 1. 1. 1.]
      [1. 1. 1. 1.]
      [1. 1. 1. 1.]]
    
     [[1. 1. 1. 1.]
      [1. 1. 1. 1.]
      [1. 1. 1. 1.]
      ...
      [1. 1. 1. 1.]
      [1. 1. 1. 1.]
      [1. 1. 1. 1.]]]


.. code:: 

    print (logo.shape)
    
    plt.imshow(logo)
    plt.show()


.. parsed-literal::

    (1652, 2138, 4)



.. figure:: /images/output_21_1.png
   :alt: alt text goes here
   :align: center
   :width: 800px
   


.. code:: 

    # Create subplots
    left = dt.date(2016, 1, 1)
    right = dt.date(2021, 5, 31)
    
    #plt.figure(figsize=(16,6),dpi=300)
    plt.figure(figsize=(10,6),dpi=300)
    plt.rcParams['font.size'] = '14'
    plt.figure().set_figwidth(20)
    plt.rcParams['figure.figsize'] = [6.8, 5]
    plt.rcParams['font.weight'] = 'normal'
    
    fig, (ax1,ax2) = plt.subplots(nrows=2,sharex=True,
                                 constrained_layout=True,)
    ax1 = plt.subplot(2,1,1)
    cmap = plt.cm.get_cmap("jet").copy()
    #cmap = plt.get_cmap('viridis')
    cmap.set_under('0.5')
    im=plt.pcolor(time_2D,data['PRES_ADJUSTED'].
               values,data['PSAL_ADJUSTED'].values.astype(float),
               cmap=cmap,vmin=33,vmax=35.5)
    plt.ylim([0,250])
    plt.gca().invert_yaxis()
    #ax1.annotate("(b)", xy=(0.92, 0.92),
    #             xycoords=ax1.transAxes,
    #             fontsize=12,color='black',weight='bold')
    #cs1=plt.contour(time_2D,data['PRES_ADJUSTED'].values,
    #            data['PSAL_ADJUSTED'].values.astype(float),levels=[34.3],colors='r')
    #ax1.clabel(cs1,inline=1,fontsize=10,colors='k')
    cs1=plt.contour(time_2D,data['PRES_ADJUSTED'].values,
                data['PSAL_ADJUSTED'].values.astype(float),
                    levels=[34.3],colors='r')
    ax1.clabel(cs1,inline=1,fontsize=20,colors='k')
    
    ax2 = plt.subplot(2,1,2,)
    plt.pcolor(time_2D,data['PRES_ADJUSTED'].values,
               data['PSAL_ADJUSTED'].values.astype(float),
               cmap=cmap,vmin=33,vmax=35.5)
    plt.ylim([250,1000])
    plt.gca().invert_yaxis()
    cs2=plt.contour(time_2D,data['PRES_ADJUSTED'].values,
                data['PSAL_ADJUSTED'].values.astype(float),levels=[34.3],colors='r')
    ax2.clabel(cs2,inline=1,fontsize=10,colors='k')
    
    plt.gca().set_xbound(left, right)
    #plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'),)
    #cax,kw = mpl.colorbar.make_axes([ax for ax in (ax1,ax2)],pad=0.02)
    #fig.colorbar(im, cax=cax, **kw,label='Salinity (psu)')
    #fig.supylabel('Depth (m)')
    
    plt.gca().xaxis.set_major_locator(mdates.YearLocator(base=2))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    #plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'),)
    cax,kw = mpl.colorbar.make_axes([ax for ax in (ax1,ax2)],pad=0.02)
    fig.colorbar(im, cax=cax, **kw,label='Salinity')
    #fig.supylabel('Depth (m)')
    fig.supylabel('Depth (m)',x=-0.01,y=0.5)
    
    plt.savefig("argo5905017_Sdiv.png")


.. parsed-literal::

    /tmp/ipykernel_10019/480330380.py:15: MatplotlibDeprecationWarning: The get_cmap function was deprecated in Matplotlib 3.7 and will be removed two minor releases later. Use ``matplotlib.colormaps[name]`` or ``matplotlib.colormaps.get_cmap(obj)`` instead.
      cmap = plt.cm.get_cmap("jet").copy()
    /tmp/ipykernel_10019/480330380.py:18: UserWarning: The input coordinates to pcolor are interpreted as cell centers, but are not monotonically increasing or decreasing. This may lead to incorrectly calculated cell edges, in which case, please supply explicit cell edges to pcolor.
      im=plt.pcolor(time_2D,data['PRES_ADJUSTED'].
    /tmp/ipykernel_10019/480330380.py:35: UserWarning: The input coordinates to pcolor are interpreted as cell centers, but are not monotonically increasing or decreasing. This may lead to incorrectly calculated cell edges, in which case, please supply explicit cell edges to pcolor.
      plt.pcolor(time_2D,data['PRES_ADJUSTED'].values,



.. parsed-literal::

    <Figure size 3000x1800 with 0 Axes>



.. parsed-literal::

    <Figure size 2000x500 with 0 Axes>



.. figure:: /images/output_22_3.png
   :alt: alt text goes here
   :align: center
   :width: 800px
   
