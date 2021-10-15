import pandas as pd
from pathlib import Path
import click

@click.command()
@click.option('-i', '--idir', help='Input directory of CSV files')
@click.option('-o', '--ofile', help='Output HDF5 file')
def make_hdf(
    idir: str,
    ofile: str
    ) -> None:
    """Process a directory of NetCDF RouteLink files to their CSV equivalents.
    
    Parameters
    ----------
    idir: str
        Input directory containing Routelink files in CSV format.
    ofile: str
        Output HDF5 file to store pandas.DataFrame
        
    Returns
    -------
    None
    """
    # Get list of files
    file_list = Path(idir).glob("*.csv")
    
    # Load data
    dfs = []
    for ifile in file_list:
        # Read file
        df = pd.read_csv(ifile, comment="#", dtype={"usgs_site_code": str}, 
            parse_dates=["time"])

        # Stowe data
        dfs.append(df)

    # Concat
    data = pd.concat(dfs, ignore_index=True)

    # Save
    data.to_hdf(ofile, key="data", format="table", complevel=1)

if __name__ == "__main__":
    make_hdf()
