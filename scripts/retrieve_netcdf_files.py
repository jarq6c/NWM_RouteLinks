import requests
import click
from pathlib import Path

def download(url: str, ofile: Path):
    """Stream large files to disk.
    
    Parameters
    ----------
    url: str
        URL of file to retrieve.
    ofile: pathlib.Path
        Destination to save file.
        
    Returns
    -------
    None
    """
    response = requests.get(url, stream=True)
    with ofile.open("wb") as fo:
        for data in response.iter_content(chunk_size=1024):
            fo.write(data)

@click.command()
@click.option('-f', '--files', help='Input file with list of RouteLink URLs')
@click.option('-o', '--output', help='Output directory to download NetCDF files')
def retrieve(
    files: str,
    output: str
    ) -> None:
    """Download a list of files to an output directory.
    
    Parameters
    ----------
    files: str
        List of file URLs, one per line.
    output: str
        Download directory where all files will be saved.
        
    Returns
    -------
    None
    """
    # Get list of URLs
    with Path(files).open('r') as fi:
        urls = [line.strip() for line in fi]

    # Prepare output directory
    odir = Path(output)
    odir.mkdir(exist_ok=True, parents=True)

    # Download
    for url in urls:
        # Construct an output filename
        ofile = odir / url.split("/")[-1]
        
        # Save
        download(url, ofile)

if __name__ == "__main__":
    retrieve()
