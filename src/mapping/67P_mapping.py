import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

# extent=[-180, 180, -90, 90]
#
# # === File paths (UPDATE THESE) ===
# excel_path = 'C:/Learning/Coding/GIT/67P-coordinates/data/output/coordinates_long_lat_results.xlsx'
# background_image_path = 'C:/Learning/Coding/GIT/67P-coordinates/data/input/map/gs_equidistant_cylindrical_lat0_lon0_ms2048.jpg'
# output_image_path = 'C:/Learning/Coding/GIT/67P-coordinates/data/output/exposure_map.jpg'
#
# # === Read Excel file ===
# df = pd.read_excel(excel_path)
#
# # === Ensure Latitude and Longitude columns exist ===
# if 'Latitude' not in df.columns or 'Longitude' not in df.columns:
#     raise ValueError("Excel file must contain 'Latitude' and 'Longitude' columns.")
#
# latitudes = df['Latitude']
# longitudes = df['Longitude']
#
# # === Load background map image ===
# img = mpimg.imread(background_image_path)
#
# # === Create figure and plot ===
# fig, ax = plt.subplots(figsize=(12, 6))
#
# # Set proper extent for equirectangular projection: [-180, 180] in lon, [-90, 90] in lat
# ax.imshow(img, extent=[-180, 180, -90, 90], aspect='auto')
#
# # Plot the points
# ax.scatter(longitudes, latitudes, color='red', s=20, label='Data Points')
#
# # Configure axis
# ax.set_xlim([-180, 180])
# ax.set_ylim([-90, 90])
# ax.set_xlabel('Longitude')
# ax.set_ylabel('Latitude')
# ax.set_title('Points on Custom Map (Equirectangular)')
# ax.grid(True, linestyle='--', alpha=0.5)
# ax.legend()
#
# # Save as JPG
# plt.tight_layout()
# plt.savefig(output_image_path, dpi=300)
# print(f"✅ Map saved to: {output_image_path}")
#
# # Show the plot
# plt.show()



import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# === File path ===
input_file = 'C:/Learning/Coding/GIT/67P-coordinates/data/output/coordinates_long_lat_results.xlsx'  # Change this to your file path

# === Read Excel file ===
df = pd.read_excel(input_file)

# === Ensure required columns exist ===
if 'Latitude' not in df.columns or 'Longitude' not in df.columns:
    raise ValueError("Excel file must contain 'Latitude' and 'Longitude' columns.")

latitudes = df['Latitude']
longitudes = df['Longitude']

# === Create a map with equirectangular projection ===
fig = plt.figure(figsize=(12, 6))
ax = plt.axes(projection=ccrs.PlateCarree())

# Add map features
ax.set_global()
ax.coastlines()
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.gridlines(draw_labels=True, linestyle='--')

# Plot the points
ax.scatter(longitudes, latitudes, color='red', s=20, transform=ccrs.PlateCarree(), label='Data Points')

plt.title('Map with Latitude and Longitude Points (Equirectangular Projection)')
plt.legend()
plt.tight_layout()
plt.show()