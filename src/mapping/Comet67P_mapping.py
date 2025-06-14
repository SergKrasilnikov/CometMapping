import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pathlib import Path

# config
project_root = Path(__file__).resolve().parent.parent.parent # get the root directory of the project (2 levels up)
excel_file = project_root / 'data' / 'output' / 'db' / 'coordinates_long_lat_results.xlsx'
background_image = project_root / 'data' / 'input' / 'map' / 'gs_equidistant_cylindrical_lat0_lon0_ms2048.jpg'
output_image = project_root / 'data' / 'output' / 'map' / 'exposure_map.jpg'

# read the Excel file
df = pd.read_excel(excel_file)

latitudes = df['Latitude']
longitudes = df['Longitude']

# load the basemap image
img = mpimg.imread(background_image)

# plot the map
fig, ax = plt.subplots(figsize=(16, 8))
ax.imshow(img, extent=[-180, 180, -90, 90], aspect='equal')

# color mapping function
def get_color(type_value):
    if str(type_value).strip() == '1':
        return 'red'
    elif str(type_value).strip() in ['2', '3', '2, 3']:
        return 'green'
    elif str(type_value).strip() in ['4', '2, 4']:
        return 'yellow'
    else:
        return 'gray'

# plot colored points
for _, row in df.iterrows():
    lat = row['Latitude']
    lon = row['Longitude']
    type_val = row['Type']
    color = get_color(type_val)
    ax.scatter(lon, lat, color=color, s=60)

# mapp settings
ax.set_xlim([-180, 180])
ax.set_ylim([-90, 90])
ax.xaxis.tick_top()
ax.yaxis.tick_right()
plt.xticks([-180, -150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150, 180])
plt.yticks([75, 60, 45, 30, 15, 0, -15, -30, -45, -60, -75])
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
# ax.set_xlabel('Longitude')
# ax.set_ylabel('Latitude')
# ax.set_title('Map with Points Colored by Type')
ax.grid(True, color='maroon', linestyle='--', alpha=0.5)
ax.legend()

# legend
import matplotlib.patches as mpatches
legend_patches = [
    mpatches.Patch(color='red', label='Type 1'),
    mpatches.Patch(color='green', label='Type 2, 3'),
    mpatches.Patch(color='yellow', label='Type 4'),
]
ax.legend(handles=legend_patches, loc='upper right', prop={'size': 14})

# output
plt.tight_layout()
plt.savefig(output_image, dpi=600)

# show the result
plt.show()
