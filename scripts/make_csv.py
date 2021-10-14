import xarray as xr
import pandas as pd
from pathlib import Path
import click
 
# Current time
now = pd.Timestamp.utcnow()
 
# Append to metadata
message = f'''Extracted from NetCDF on {now}
Some column names were changed when extracting from the original NetCDF format.
link -> nwm_feature_id
gages -> usgs_site_code
lat -> latitude
lon -> longitude'''

@click.command()
@click.option('-i', '--idir', help='Input directory of NetCDF files')
@click.option('-o', '--odir', help='Output directory of CSV files')
def make_csv(
    idir: str,
    odir: str
    ) -> None:
    """Process a directory of NetCDF RouteLink files to their CSV equivalents.
    
    Parameters
    ----------
    idir: str
        Input directory containing Routelink files.
    odir: str
        Output directory to save CSV files.
        
    Returns
    -------
    None
    """
    # Get list of files
    file_list = Path(idir).glob("*.nc")

    # Output directory
    odir = Path(odir)
    odir.mkdir(exist_ok=True, parents=True)

    for ifile in file_list:
        # Open dataset
        ds = xr.open_dataset(ifile)

        # Convert to a dataframe
        df = ds.to_dataframe()
        no_gage = b'               '
        df = df[df.gages != no_gage]
        df = df.rename(columns={
            'link': 'nwm_feature_id',
            'gages': 'usgs_site_code',
            'lat': 'latitude',
            'lon': 'longitude'
            })
        df['usgs_site_code'] = df['usgs_site_code'].str.decode("utf-8").str.strip()

        # Extract global attributes
        output = ''
        for key, val in ds.attrs.items():
            output += f"{key}: {val}\n"
        output += message + '\n'

        # Re-comment newlines
        output = '# ' + output.replace('\n', '\n# ') + '\n'

        # Extract data
        output += df.to_csv(index=True)

        # Write data
        stem = ifile.stem
        ofile = odir / f'{stem}.csv'
        with ofile.open("w") as fo:
            fo.write(output)

if __name__ == "__main__":
    make_csv()
