import math

#Cartesian coordinates
A = [1.16249001, 0.363859236, 1.223576546]

#Convert Cartesian to Spherical coordinates
def rect2sph(A):

    projlen = math.sqrt(A[0]**2 + A[1]**2)

    lat = math.atan(A[2]/projlen) * 180/math.pi

    if A[1] >= 0:
        lon = math.acos(A[0]/projlen) * 180/math.pi
    else:
        lon = - math.acos(A[0]/projlen) * 180/math.pi
    if projlen == 0:
        lon = 0.0
    # current longitudes from -180 to +180. Switch strings bellow ON if you need longitudes from 0 to 360.
    # if lon < 0:
    #     lon += 360

    rad = math.sqrt(A[0]**2 + A[1]**2 + A[2]**2)
    return [round(lon,2), round(lat,2), round(rad,2)]

#Convert Spherical to Cartesian coordinates
def sph2rect(lon, lat, rad):
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)

    x = rad * math.cos(lat_rad) * math.cos(lon_rad)
    y = rad * math.cos(lat_rad) * math.sin(lon_rad)
    z = rad * math.sin(lat_rad)

    return [round(x,6), round(y,6), round(z,6)]

# Original Cartesian coordinates
print("Original Cartesian (X, Y, Z):", A)

# Convert to spherical
sph_coords = rect2sph(A)
print("Converted to Spherical (lon, lat, rad):", sph_coords)

# Convert back to Cartesian
rect_coords = sph2rect(*sph_coords)
print("Converted back to Cartesian (X, Y, Z):", rect_coords)