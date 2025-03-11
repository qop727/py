# Program to train libraries.

import math

def circle_area(r):
    return math.pi * math.pow(r, 2)

radius = 5
area = circle_area(radius)
print(f"Obsah kruhu s poloměrem {radius} je: {area}")