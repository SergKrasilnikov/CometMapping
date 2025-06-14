import pandas as pd
import trimesh
import numpy as np
import math

# input parameters
input_excel = "C:/Learning/Coding/GIT/67P-coordinates/data/output/coordinates_long_lat_results.xlsx"
output_excel = "C:/Learning/Coding/GIT/67P-coordinates/data/output/coordinates_long_lat_results_povered.xlsx"
shape_model_path = "C:/Learning/Coding/GIT/67P-coordinates/data/input/model/SPG1.0_SPC1.5_merged_shape_1M.ply"
max_radius_km = 3.5 # maximum distance for searching. For Comet 67P, the maximum radius is <3.5 km.

# convert spherical to unit vector
def sph2unitvec(lat, lon):
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)
    x = math.cos(lat_rad) * math.cos(lon_rad)
    y = math.cos(lat_rad) * math.sin(lon_rad)
    z = math.sin(lat_rad)
    return [x, y, z]

# load the shape model
print("Loading shape model...")
mesh = trimesh.load_mesh(shape_model_path)
if not isinstance(mesh, trimesh.Trimesh):
    mesh = mesh.dump().sum()

# optional: clean up geometry
mesh.update_faces(mesh.nondegenerate_faces())          # removes degenerate faces
mesh.update_faces(mesh.unique_faces())                # removes duplicate faces
mesh.remove_unreferenced_vertices()

print("Shape model loaded and validated.")

# read Excel input
df = pd.read_excel(input_excel)

# validate columns
if 'Longitude' not in df.columns or 'Latitude' not in df.columns:
    raise ValueError("Excel file must contain 'Longitude' and 'Latitude' columns.")

# prepare output columns
X_list, Y_list, Z_list = [], [], []

# process each point
for idx, row in df.iterrows():
    lon = row['Longitude']
    lat = row['Latitude']

    origin = np.array([[0.0, 0.0, 0.0]])
    direction = np.array([sph2unitvec(lat, lon)])

    try:
        locations, _, _ = mesh.ray.intersects_location(ray_origins=origin, ray_directions=direction)
    except Exception as e:
        print(f"    Error tracing ray for row {idx}: {e}")
        X_list.append(None)
        Y_list.append(None)
        Z_list.append(None)
        continue

    if len(locations) == 0:
        print(f"    No intersections found for row {idx} (Lon={lon}, Lat={lat})")
        X_list.append(None)
        Y_list.append(None)
        Z_list.append(None)
        continue

    dists = np.linalg.norm(locations - origin, axis=1)  # shape: (num_intersections,)
    within_radius = dists <= max_radius_km  # shape: (num_intersections,)

    if not np.any(within_radius):
        print(f"    No valid intersections within {max_radius_km} km for row {idx}")
        X_list.append(None)
        Y_list.append(None)
        Z_list.append(None)
        continue

    # Now this works safely
    masked_dists = np.where(within_radius, dists, -np.inf)
    idx_max = np.argmax(masked_dists)
    point = locations[idx_max]

    # append result
    X_list.append(point[0])
    Y_list.append(point[1])
    Z_list.append(point[2])

# add new columns to DataFrame
df['X'] = X_list
df['Y'] = Y_list
df['Z'] = Z_list

# save to new Excel
df.to_excel(output_excel, index=False)
print(f"\n✅ Conversion complete. Output saved to: {output_excel}")
