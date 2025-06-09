# -*- coding: utf-8 -*-
# @Author  : XUNWJ
# @Contact : ssssustar@163.com
# @File    : get_tin_info.py
# @Time    : 2025/5/21 15:45
# @Desc    :
from __future__ import print_function
from __future__ import division
import bpy
import trimesh
import numpy as np
import pandas as pd

def get_all_points(points_save_path):
    # Collect the positions of all reference points in the scene (assuming it is Empty or a collection of objects)
    reference_points = []
    for obj in bpy.data.objects:
        reference_points.append((obj.name, obj.location[:]))

    # Write name + xyz to file
    with open(points_save_path, "w") as f:
        for name, loc in reference_points:
            f.write(f"{name} {loc[0]} {loc[1]} {loc[2]}\n")

def get_poits_tin(ply_model_path, points_info_path, result_save_path):
    # 1. Loading the PLY model
    mesh = trimesh.load(ply_model_path)
    pq = trimesh.proximity.ProximityQuery(mesh)
    # 2. Load reference point
    reference_points = np.genfromtxt(points_info_path, dtype=None, encoding=None)

    # To store the results
    output = []

    # Find the closest face (triangle) for each point
    for name, x, y, z in reference_points:

        pt = (x, y, z)

        # Find the nearest face
        location, distance, face_index = pq.on_surface([pt])
        # face_index = mesh.nearest.faces(pt)

        # Find the three vertex indices of the face
        vertex_indices = mesh.faces[face_index[0]]

        # Get the coordinates of the three vertices
        triangle_vertices = mesh.vertices[vertex_indices]

        # Save: reference point + three vertices of the corresponding triangle
        output.append({
            'name': name,
            'point': list(pt),
            'triangle_vertices': triangle_vertices.tolist()
        })

    # # Writing to a file
    # with open(result_save_path, "w") as f:
    #     for item in output:
    #         f.write(f"Name: {item['name']}\n")
    #         f.write(f"Point: {item['point']}\n")
    #         f.write(f"Triangle vertices:\n")
    #         for v in item['triangle_vertices']:
    #             f.write(f"  {v}\n")
    #         f.write("\n")
    return output

def save_result2csv(results_list, save_path):
    rows = []
    for item in results_list:
        name = item['name']
        for v in item['triangle_vertices']:
            rows.append({
                'points_name': name,
                'x': v[0],
                'y': v[1],
                'z': v[2]
            })

    df = pd.DataFrame(rows)
    df.to_csv(save_path, index=False)

def merge_csv(result_csv, ref_csv, save_csv):
    # Reading CSV
    A = pd.read_csv(result_csv)  # Contains points_name, x, y, z
    B = pd.read_csv(ref_csv)  # Contains points_name and other data


    # Iterate over each row in A
    for _, row in A.iterrows():
        name = row['points_name'].split('.')[0]
        x, y, z = row['x'], row['y'], row['z']

        # Find the corresponding row number i in B
        # matches = B.index[B['points_name'] == name].tolist()
        match = B[B['points_name'] == name]
        if not match.empty:
            i = match.index[0]
            # Find the column number of the 'points_name' column in that row j
            j = B.columns.get_loc('points_name')

            # Write x, y, z to row i, column j+1, j+2, j+3 in B
            if j + 3 >= len(B.columns):
                # If there are not enough columns, add empty columns first
                for k in range(len(B.columns), j + 4):
                    B.insert(k, f'col{k}', None)

            B.iat[i, j + 1] = x
            B.iat[i, j + 2] = y
            B.iat[i, j + 3] = z

    # Save the modified B
    B.to_csv(save_csv, index=False)

if __name__ == '__main__':

    blend_path = r"G:\Comet_67P\Bright_spot_location\67P_coord.blend"
    ply_model_path = r"G:\Comet_67P\Bright_spot_location\SPG1.0_SPC1.5_merged_shape_1M.ply"
    points_save_path = r'G:\Comet_67P\Bright_spot_location\reference_points.txt'
    result_save_path = r'G:\Comet_67P\Bright_spot_location\mesh_results.txt'
    final_save_path = r'G:\Comet_67P\Bright_spot_location\xyz_coor_results.csv'
    reference_csv_path = r"G:\Comet_67P\Bright_spot_location\record_long_lat coordinates.csv"
    merge_csv_path = r'G:\Comet_67P\Bright_spot_location\xyz_coor_results_merge.csv'
    # Open the specified blend-file (can only be called from the command line)
    # bpy.ops.wm.open_mainfile(filepath=blend_path)
    # get_all_points(points_save_path)
    # result_output = get_poits_tin(ply_model_path, points_save_path, result_save_path)
    # save_result2csv(result_output, final_save_path)
    merge_csv(final_save_path, reference_csv_path, merge_csv_path)

