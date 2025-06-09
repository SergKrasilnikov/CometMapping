import pandas as pd
import trimesh
import numpy as np

# === Config ===
input_excel = "C:/Learning/Coding/GIT/67P-coordinates/data/output/coordinates_cartesian_Fornasier.xlsx"
output_obj = "C:/Learning/Coding/GIT/67P-coordinates/data/output/shapefile_Fornasier.obj"
sphere_radius = 0.02  # Diameter = 0.04 m

# === Load Excel ===
df = pd.read_excel(input_excel)

# === Validate columns ===
required = ['BS', 'X', 'Y', 'Z']
if not all(col in df.columns for col in required):
    raise ValueError(f"Excel file must contain columns: {required}")

# === Create a scene of spheres ===
scene = trimesh.Scene()

for idx, row in df.iterrows():
    bs = str(row['BS'])
    x, y, z = row['X'], row['Y'], row['Z']

    if pd.isnull([x, y, z]).any():
        print(f"⚠️ Skipping invalid point at row {idx}")
        continue

    # Create unit sphere, then scale
    sphere = trimesh.creation.icosphere(radius=sphere_radius, subdivisions=2)

    # Translate to the target position
    sphere.apply_translation([x, y, z])

    # Add to scene with name
    scene.add_geometry(sphere, node_name=bs)

print(f"✅ Total objects added: {len(scene.geometry)}")

# === Export to OBJ ===
with open(output_obj, 'w') as f:
    f.write(trimesh.exchange.obj.export_obj(scene))

print(f"✅ OBJ file written to: {output_obj}")
