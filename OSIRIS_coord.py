import math

A = [0.089647, 1.52644, 0.8639]


def rect2sph(A):

    projlen = math.sqrt(A[0]**2 + A[1]**2)

    lat = math.atan(A[2]/projlen) * 180/math.pi

    if A[1] >= 0:
        lon = math.acos(A[0]/projlen) * 180/math.pi
    else:
        lon = - math.acos(A[0]/projlen) * 180/math.pi
    if projlen == 0:
        lon = 0.0
    if lon < 0:
        lon += 360

    rad = math.sqrt(A[0]**2 + A[1]**2 + A[2]**2)
    return [lat, lon, rad]

print(rect2sph(A))