import json
from pathlib import Path
import pandas as pd

ifile = Path("nwm_headwater_gages.json")

with ifile.open("r") as fo:
    data = json.loads(fo.read())

records = []
for location in data["locations"]:
    r = {}
    for prefix, attribute in location.items():
        if isinstance(attribute, dict):
            for suffix, value in attribute.items():
                r[prefix+"_"+suffix] = str(value)
        else:
            for idx, value in enumerate(attribute):
                r[prefix+f"_{idx}"] = value
    records.append(r)

df = pd.DataFrame.from_records(records).fillna(-99)

df.to_csv("usgs_gages_ii_ref_headwater_wrds.csv", index=False)
