import pandas as pd
import math
from pathlib import Path

# config
project_root = Path(__file__).resolve().parent.parent.parent # get the root directory of the project (2 levels up)
input_file = project_root / 'data' / 'input' / 'db' / 'coordinates_long_lat.xlsx'
output_file = project_root / 'data' / 'output' / 'db' / 'coordinates_long_lat_results.xlsx'

# Cartesian-to-Spherical function
def rect2sph(A):
    projlen = math.sqrt(A[0]**2 + A[1]**2)
    lat = math.atan(A[2]/projlen) * 180 / math.pi

    if A[1] >= 0:
        lon = math.acos(A[0]/projlen) * 180 / math.pi
    else:
        lon = -math.acos(A[0]/projlen) * 180 / math.pi

    if projlen == 0:
        lon = 0.0
    # current longitudes from -180 to +180. Switch strings below ON if you need longitudes from 0 to 360.
    # if lon < 0:
    #     lon += 360

    rad = math.sqrt(A[0]**2 + A[1]**2 + A[2]**2)
    return [round(lat, 2), round(lon, 2), round(rad, 2)]

# Read Excel file
df = pd.read_excel(input_file)

# rows processing
for idx, row in df.iterrows():
    x = row.get('x')
    y = row.get('y')
    z = row.get('z')

    # x is a number
    if pd.notnull(x) and isinstance(x, (int, float)):
        A = [x, y, z]
        lat, lon, _ = rect2sph(A)
        df.at[idx, 'Latitude'] = lat
        df.at[idx, 'Longitude'] = lon

# Save results
df.to_excel(output_file, index=False)