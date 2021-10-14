# NWM RouteLinks
Utilities used to extract metadata that links National Water Model (NWM) feature identifiers to United States Geological Survey (USGS) site codes.

## Usage
Running `make` in this directory will build the required Python environment, retrieve raw NetCDF Routelink files from NCEP and convert them to CSV. This creates two new directories: `netcdf` which will contain the raw NetCDF files and `csv` which will contain a CSV equivalent to each file in `netcdf`. You can view a list of the file URLs retrieved in `files.txt`. Actual Python code is in `scripts`.
