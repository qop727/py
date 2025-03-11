# Program to train libraries.

import py_lib_geometry

radius = 7
print("Kruh:")
print("  Obsah:", py_lib_geometry.area_circle(radius))
print("  Obvod:", py_lib_geometry.perimeter_circle(radius))
    
side = 3
print("\nČtverec:")
print("  Obsah:", py_lib_geometry.area_square(side))
print("  Obvod:", py_lib_geometry.perimeter_square(side))
    
length = 6
width = 3
print("\nObdélník:")
print("  Obsah:", py_lib_geometry.area_rectangle(length, width))
print("  Obvod:", py_lib_geometry.perimeter_rectangle(length, width))
    
base = 5
height = 4
side3 = 6
print("\nTrojúhelník:")
print("  Obsah:", py_lib_geometry.area_triangle(base, height))
print("  Obvod:", py_lib_geometry.perimeter_triangle(base, height, side3))