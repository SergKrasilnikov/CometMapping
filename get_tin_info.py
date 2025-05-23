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
    # 收集场景中所有参考点的位置（假设是 Empty 或某一对象集合）
    reference_points = []
    for obj in bpy.data.objects:
        reference_points.append((obj.name, obj.location[:]))

    # 写入名称 + xyz 到文件
    with open(points_save_path, "w") as f:
        for name, loc in reference_points:
            f.write(f"{name} {loc[0]} {loc[1]} {loc[2]}\n")

def get_poits_tin(ply_model_path, points_info_path, result_save_path):
    # 1. 加载PLY模型
    mesh = trimesh.load(ply_model_path)
    pq = trimesh.proximity.ProximityQuery(mesh)
    # 2. 加载参考点
    reference_points = np.genfromtxt(points_info_path, dtype=None, encoding=None)

    # 用于存储结果
    output = []

    # 为每个点找最近面（triangle）
    for name, x, y, z in reference_points:

        pt = (x, y, z)

        # 找最近面
        location, distance, face_index = pq.on_surface([pt])
        # face_index = mesh.nearest.faces(pt)

        # 找该面的三个顶点索引
        vertex_indices = mesh.faces[face_index[0]]

        # 取出三个顶点的坐标
        triangle_vertices = mesh.vertices[vertex_indices]

        # 保存：参考点 + 对应三角形的三个顶点
        output.append({
            'name': name,
            'point': list(pt),
            'triangle_vertices': triangle_vertices.tolist()
        })

    # # 写入文件
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
    # 读取CSV
    A = pd.read_csv(result_csv)  # 包含 points_name, x, y, z
    B = pd.read_csv(ref_csv)  # 包含 points_name 和其他数据


    # 遍历 A 中的每一行
    for _, row in A.iterrows():
        name = row['points_name'].split('.')[0]
        x, y, z = row['x'], row['y'], row['z']

        # 查找 B 中对应行号 i
        # matches = B.index[B['points_name'] == name].tolist()
        match = B[B['points_name'] == name]
        if not match.empty:
            i = match.index[0]
            # 找到该行中 'points_name' 列的列号 j
            j = B.columns.get_loc('points_name')

            # 写入 x, y, z 到 B 中的 i 行 j+1, j+2, j+3 列
            if j + 3 >= len(B.columns):
                # 如果列不够，先添加空列
                for k in range(len(B.columns), j + 4):
                    B.insert(k, f'col{k}', None)

            B.iat[i, j + 1] = x
            B.iat[i, j + 2] = y
            B.iat[i, j + 3] = z

    # 保存修改后的B
    B.to_csv(save_csv, index=False)

if __name__ == '__main__':

    blend_path = r"G:\Comet_67P\Bright_spot_location\67P_coord.blend"
    ply_model_path = r"G:\Comet_67P\Bright_spot_location\SPG1.0_SPC1.5_merged_shape_1M.ply"
    points_save_path = r'G:\Comet_67P\Bright_spot_location\reference_points.txt'
    result_save_path = r'G:\Comet_67P\Bright_spot_location\mesh_results.txt'
    final_save_path = r'G:\Comet_67P\Bright_spot_location\xyz_coor_results.csv'
    reference_csv_path = r"G:\Comet_67P\Bright_spot_location\record_long_lat coordinates.csv"
    merge_csv_path = r'G:\Comet_67P\Bright_spot_location\xyz_coor_results_merge.csv'
    # 打开指定blend文件（只能用命令行调用）
    # bpy.ops.wm.open_mainfile(filepath=blend_path)
    # get_all_points(points_save_path)
    # result_output = get_poits_tin(ply_model_path, points_save_path, result_save_path)
    # save_result2csv(result_output, final_save_path)
    merge_csv(final_save_path, reference_csv_path, merge_csv_path)

