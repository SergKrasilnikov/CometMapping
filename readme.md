# CometMapping

## CometMapping - Operating with comet coordinates and mapping

Planetary Remote Sensing Laboratory / The Hong Kong Polytechnic University

### Author
- [Sergey Krasilnikov](https://github.com/SergKrasilnikov)
### Contributor
- [XunWJ](https://github.com/Sustar2)

---

### Overview
The number of programs for operating with comet coordinates and mapping. The base dataset and model is Comet 
67P/Churyumov–Gerasimenko. These tools can be used for any other planetary bodies. Uses of programs:

- Transformation between Cartesian and Spherical coordinates, and vice versa (coordinates).

- The mapping tool utilises spherical coordinates to map features in an Equirectangular projection.

- Tools related to the shapefile of the comet work with the spatial position of objects (points) and create these
objects in OBJ format or get spatial information.

---

### The list of programs:
```
get_tin_info.py & create_shapefile.py
```
Operate with spatial information of objects. `get_tin_info.py` gets the information from the OBJ file created in
Blender. The OBJ file consists of points (spheres) in a 3D spatial environment, along with the locations of the
features. The location of these points can be described by Cartesian coordinates (X, Y, Z). The tool creates an Excel
file with coordinates for each point.
`create_shapefile.py` makes reconversion, transforming Cartesian coordinates (X, Y, Z) from an Excel file into a 3D OBJ
file that could be opened in 3D software.

```
CartToSpher_coord.py & CartToSpher_coord_file.py
```
Transform Cartesian coordinates to Spherical coordinates. Program `CartToSpher_coord.py` uses manually typed Cartesian 
coordinates and returns Original, Cartesian-to-Spherical and Spherical-to-Cartesian (for comparison) coordinates.
`CartToSpher_coord_file.py` as input uses an Excel file 'x', 'y' and 'z' columns of Cartesian coordinates. The program
returns the original Excel file adding two columns: 'Longitude' and 'Latitude'.

```
ray_surf_intersec.py & ray_surf_intersec_file.py
```
Transform Spherical coordinates to Cartesian coordinates using the ray tracing approach. Program `ray_surf_intersec.py`
uses manually typed Spherical coordinates, defines the ray origin  [0.0, 0.0, 0.0] and returns a list of valid
intersections of the ray with the shape model of the object. In case of more than one intersection, the program chooses
the farthest intersection in a 3.5 km radius. Typing the Spherical coordinates program returns Cartesian coordinates.
`ray_surf_intersec_file.py` as input uses an Excel file 'Longitude' and 'Latitude' columns of Spherical coordinates.
The program returns the original Excel file adding three 'x', 'y' and 'z' columns of Cartesian coordinates.

```
Comet67P_mapping.py
```
Using matplotlib libraries to map features in Equirectangular projection. Program `Comet67P_mapping.py` uses an Excel
file with the Longitude and Latitude coordinates of features and a preload base map. As the base map, the hillshade map
of Comet 67P was used in Equirectangular projection.

---

### Data (__CORRECT__)
- Our mapping results [Zenodo](https://)
- Fornasier water exposure dataset [____](https://) - the dataset published by Fornasier et al.,
[(2023)](https://) used for comparision with our results.
- Comet 67P/Churyumov–Gerasimenko shape models and based on it hilshade map [SHAP5](https://) and
[SHAP8](https://)

---

### How to cite:(__CORRECT__)
These programs used in a scientific project will be published in 2025-2026:

>Krasilnikov, S.S., Wu, B., Skorov, Yu., Xin, Y., Xun, W., Küppers, M., 2025. The mechanisms of water ice exposure on
> the surface of comet 67P/Churyumov-Gerasimenko