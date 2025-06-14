import pandas as pd
import trimesh
import numpy as np
from pathlib import Path

# input parameters
sphere_radius = 0.02  # set the diameter = 0.04 m
# config
project_root = Path(__file__).resolve().parent.parent.parent # get the root directory of the project (2 levels up)
input_excel = project_root / 'data' / 'output' / 'db' / 'coordinates_cartesian_Fornasier.xlsx'
output_obj = project_root / 'data' / 'output' /  'obj' / 'shapefile_Fornasier.obj'

# load Excel
df = pd.read_excel(input_excel)
# validate columns
required = ['BS', 'X', 'Y', 'Z']
if not all(col in df.columns for col in required):
    raise ValueError(f"Excel file must contain columns: {required}")

# create a scene of spheres
scene = trimesh.Scene()

for idx, row in df.iterrows():
    bs = str(row['BS'])
    x, y, z = row['X'], row['Y'], row['Z']

    if pd.isnull([x, y, z]).any():
        print(f"Skipping invalid point at row {idx}")
        continue

    # create unit sphere, then scale
    sphere = trimesh.creation.icosphere(radius=sphere_radius, subdivisions=2)

    # translate to the target position
    sphere.apply_translation([x, y, z])

    # add to scene with name
    scene.add_geometry(sphere, node_name=bs)

print(f"Total objects added: {len(scene.geometry)}")

# === Export to OBJ ===
with open(output_obj, 'w') as f:
    f.write(trimesh.exchange.obj.export_obj(scene))