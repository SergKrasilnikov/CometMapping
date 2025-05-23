import math
import trimesh
import numpy as np

# [-1.06555, 0.867515, 0.0117387] 0.49, 140.85, 1.37
lon = 0.49  # longitude in degrees
lat = 140.85  # latitude in degrees
max_radius_km = 3.0
shape_model_path = "e:/Files/data/Comet67P/SPG1.0_SPC1.5_QM/SPG1.0_SPC1.5_merged_shape_1M.ply"

def sph2unitvec(lat, lon):
    """Convert latitude and longitude in degrees to a unit vector."""
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)
    x = math.cos(lat_rad) * math.cos(lon_rad)
    y = math.cos(lat_rad) * math.sin(lon_rad)
    z = math.sin(lat_rad)
    return [x, y, z]

# Load shape model
print("Loading shape model...")
mesh = trimesh.load_mesh(shape_model_path)
if not isinstance(mesh, trimesh.Trimesh):
    mesh = mesh.dump().sum()

# Define origin and ray direction
origin = np.array([[0.0, 0.0, 0.0]])
direction = np.array([sph2unitvec(lat, lon)])

# Find all intersections of the ray with the mesh
print("Computing ray intersections...")
locations, index_ray, index_tri = mesh.ray.intersects_location(ray_origins=origin, ray_directions=direction)

# Process results
if len(locations) == 0:
    print("No intersections found with the shape model.")
else:
    # Calculate distances from origin
    dists = np.linalg.norm(locations - origin, axis=1)

    # Filter only those within max_radius_km
    within_radius = dists <= max_radius_km
    if not np.any(within_radius):
        print(f"No intersection found within {max_radius_km} km.")
    else:
        # Choose the farthest intersection within the radius
        idx_farthest = np.argmax(dists * within_radius)
        point = locations[idx_farthest]
        print(f"\nFarthest valid intersection point within {max_radius_km} km:")
        print(f"Cartesian coordinates (X, Y, Z): {point}")


#
# import math
# import trimesh
# import numpy as np
#
# # === USER INPUT ===[-1.06555, 0.867515, 0.0117387] 0.49, 140.85, 1.37
# lat = 0.49
# lon = 140.85
#
# shape_model_path = "e:/Files/data/Comet67P/SPG1.0_SPC1.5_QM/SPG1.0_SPC1.5_merged_shape_1M.ply"  # full path to the PLY file
# # ==================
#
# # Convert spherical coordinates (lat, lon) to unit direction vector
# def sph2unitvec(lat, lon):
#     lat_rad = math.radians(lat)
#     lon_rad = math.radians(lon)
#     x = math.cos(lat_rad) * math.cos(lon_rad)
#     y = math.cos(lat_rad) * math.sin(lon_rad)
#     z = math.sin(lat_rad)
#     return [x, y, z]
#
# # Load the shape model mesh
# print("Loading shape model...")
# mesh = trimesh.load_mesh(shape_model_path)
# if not isinstance(mesh, trimesh.Trimesh):
#     mesh = mesh.dump().sum()
#
# # Set origin (center of comet body) and ray direction
# origin = np.array([[0.0, 0.0, 0.0]])
# direction = np.array([sph2unitvec(lat, lon)])
#
# # Perform ray intersection
# print("Computing intersection...")
# locations, index_ray, index_tri = mesh.ray.intersects_location(ray_origins=origin, ray_directions=direction)
#
# # Handle results
# if len(locations) == 0:
#     print("No intersection found with the shape model.")
# else:
#     # If multiple intersections, pick the closest one
#     dists = np.linalg.norm(locations - origin, axis=1)
#     closest_idx = np.argmin(dists)
#     point = locations[closest_idx]
#     print(f"\nCartesian coordinates (X, Y, Z): {point}")





# import math
# import trimesh
#
# lat = 29.97
# lon = 329.51
#
# def sph2unitvec(lat, lon):
#     lat_rad = math.radians(lat)
#     lon_rad = math.radians(lon)
#     x = math.cos(lat_rad) * math.cos(lon_rad)
#     y = math.cos(lat_rad) * math.sin(lon_rad)
#     z = math.sin(lat_rad)
#     return [x, y, z]
#
#
# # Load shape model
# mesh = trimesh.load("SPG1.0_SPC1.5_merged_shape_1M.ply")
#
# # Ray direction from lon/lat
# direction = sph2unitvec(lat, lon)
#
# # Ray origin (comet center)
# origin = [0, 0, 0]
#
# # Find intersection
# locations, index_ray, index_tri = mesh.ray.intersects_location(
#     ray_origins=[origin],
#     ray_directions=[direction]
# )
# print(sph2unitvec(lat, lon))
# # locations[0] is the X, Y, Z of the intersection point