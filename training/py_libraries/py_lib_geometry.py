# Geometry library.

import math

def area_circle(r):
    return math.pi * math.pow(r, 2)

def perimeter_circle(r):
    return 2 * math.pi * r

def area_square(a):
    return math.pow(a, 2)

def perimeter_square(a):
    return 4 * a

def area_rectangle(a, b):
    return a * b

def perimeter_rectangle(a, b):
    return 2 * (a + b)

def area_triangle(a, h):
    return 0.5 * a * h

def perimeter_triangle(a, b, c):
    return a + b + c