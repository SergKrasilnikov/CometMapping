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
Transform Cartesian coordinates to Spherical coordinates. The program `CartToSpher_coord.py` uses manually typed
Cartesian coordinates and returns Original, Cartesian-to-Spherical and Spherical-to-Cartesian (for comparison)
coordinates. `CartToSpher_coord_file.py` uses an Excel file with ‘x’, ‘y’, and ‘z’ columns of Cartesian coordinates.
The program returns the original Excel file with two added columns: ‘Longitude’ and ‘Latitude’.

```
ray_surf_intersec.py & ray_surf_intersec_file.py
```
Transform Spherical coordinates to Cartesian coordinates using the ray tracing approach. Program `ray_surf_intersec.py`
uses manually typed Spherical coordinates, defines the ray origin  [0.0, 0.0, 0.0] and returns a list of valid
intersections of the ray with the shape model of the object. In case of more than one intersection, the program chooses
the farthest intersection within a 3.5 km radius. Typing the Spherical coordinates program returns Cartesian
coordinates. `ray_surf_intersec_file.py` as input, uses an Excel file with ‘Longitude’ and ‘Latitude’ columns of
Spherical coordinates. The program returns the original Excel file, adding three ‘x’, ‘y’, and ‘z’ columns of Cartesian
coordinates.

```
Comet67P_mapping.py
```
Using matplotlib libraries to map features in Equirectangular projection. The program `Comet67P_mapping.py` uses an
Excel file with the Longitude and Latitude coordinates of features and a preloaded base map. As the base map, the
hillshade map of Comet 67P was used in Equirectangular projection.

---

### Data
- Our mapping results [Zenodo](https://doi.org/10.5281/zenodo.16401875)
- Fornasier water exposure dataset - the dataset published by Fornasier et al.,
[(2023)](https://doi.org/10.1051/0004-6361/202245614) used for comparison with our results.
- The latest comet 67P/Churyumov–Gerasimenko shape model is SHAP8 relised by Jorda et al., [(2016)](https://www.sciencedirect.com/science/article/pii/S0019103516301385?via%3Dihub#metrics).

---

### How to cite:
These programs used in a scientific project will be published in 2025-2026:

>Krasilnikov, S., Wu, B., Skorov, Y., Xin, Y., Li, H., Xun, W., Zhao, Y., Jia, R. and Küppers, M., 2026. Water ice 
> exposure mechanism on the surface of comet 67P/Churyumov–Gerasimenko. Monthly Notices of the Royal Astronomical 
> Society, 548(3), p.stag716.