import math
import trimesh
import numpy as np

# [-1.06555, 0.867515, 0.0117387] 0.49, 140.85, 1.37
# [1.16249001, 0.363859236, 1.223576546]	45.13	17.38

# === Parameters ===
lon = 17.38  # degrees
lat = 45.13  # degrees
max_radius_km = 3.5
shape_model_path = "C:/Learning/Coding/GIT/67P-coordinates/data/input/model/SPG1.0_SPC1.5_merged_shape_1M.ply"
# coord_module_path = "C:/Learning/Coding/GIT/67P-coordinates/src/coordinates/67P_coord.py"

# === Function to convert spherical to unit vector ===
def sph2unitvec(lat, lon):
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)
    x = math.cos(lat_rad) * math.cos(lon_rad)
    y = math.cos(lat_rad) * math.sin(lon_rad)
    z = math.sin(lat_rad)
    return [x, y, z]

# === Load the shape model ===
print("Loading shape model...")
mesh = trimesh.load_mesh(shape_model_path)
if not isinstance(mesh, trimesh.Trimesh):
    mesh = mesh.dump().sum()

# === Define the ray ===
origin = np.array([[0.0, 0.0, 0.0]])
direction = np.array([sph2unitvec(lat, lon)])

# === Ray tracing ===
print("Computing ray intersections...")
locations, index_ray, index_tri = mesh.ray.intersects_location(ray_origins=origin, ray_directions=direction)

if len(locations) == 0:
    print("No intersections found with the shape model.")
else:
    dists = np.linalg.norm(locations - origin, axis=1)
    within_radius = dists <= max_radius_km

    total_hits = len(locations)
    valid_hits = np.count_nonzero(within_radius)

    print(f"\nTotal intersections found: {total_hits}")
    print(f"Intersections within {max_radius_km} km: {valid_hits}")

    if valid_hits == 0:
        print(f"No intersections found within {max_radius_km} km.")
    else:
        print("\nList of valid intersections (within 3.5 km):")
        for i, (point, dist) in enumerate(zip(locations, dists)):
            if within_radius[i]:
                print(f"  #{i + 1}: X={point[0]:.4f}, Y={point[1]:.4f}, Z={point[2]:.4f}, Radius={dist:.4f} km")

        idx_max = np.argmax(dists * within_radius)
        point = locations[idx_max]

        print(f"\n✔ Farthest valid intersection within {max_radius_km} km:")
        print(f"  Cartesian coordinates (X, Y, Z): {point}")
        print(f"  Radius from origin: {dists[idx_max]:.4f} km")
