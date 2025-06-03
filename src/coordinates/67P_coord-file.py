import pandas as pd
import math

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
    if lon < 0:
        lon += 360

    rad = math.sqrt(A[0]**2 + A[1]**2 + A[2]**2)
    return [round(lat, 2), round(lon, 2), round(rad, 2)]

# path
input_file = 'C:/Learning/Coding/GIT/67P-coordinates/data/input/db/coordinates_long_lat_cliff_exposure.xlsx'
output_file = 'C:/Learning/Coding/GIT/67P-coordinates/data/output/coordinates_long_lat_results_cliff_exposure.xlsx'

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