# NWM RouteLinks

Utilities used to extract metadata that links National Water Model (NWM) feature identifiers to United States Geological Survey (USGS) site codes.

## Usage

Running `make` in this directory will build the required Python environment, retrieve raw NetCDF Routelink files from NCEP and convert them to CSV. This creates two new directories: `netcdf` which will contain the raw NetCDF files and `csv` which will contain a CSV equivalent to each file in `netcdf`. You can view a list of the file URLs retrieved in `files.txt`. Actual Python code is in `scripts`. The default `make` target will generate a `RouteLinks.tar.gz` which contains all the csv files and a `RouteLink.h5` that contains all the data in a `pandas.DataFrame`.

Running `make clean` will remove the intermediate files. Running `make all-clean` will remove the final files and the intermediate files.

## Data

If you found this resource on [HydroShare](http://www.hydroshare.org/resource/d154f19f762c4ee9b74be55f504325d3), you just need to download one of the final files (`RouteLinks.tar.gz` or `RouteLink.h5`).
