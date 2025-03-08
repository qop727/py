# Program to train def function.
print("--------------------------------------")
print("Printing ----------.")
def undercut1():
    N = 10
    for i in range(0,N):
       print("-", end="")
    print("")

undercut1()
###############################################

print("--------------------------------------")
print("Printing ----------.")
def undercut2(undercut_lenght):
    for i in range(undercut_lenght):
        print("-", end="")
    print("")

undercut2(10)
###############################################

print("--------------------------------------")
print("Function to calculate area of triangle.")
def area_of_triangle(hight_c, side_c):
    return hight_c * side_c / 2

print(area_of_triangle(10, 4))
###############################################

print("--------------------------------------")
print("Graphical headline.")
def headline(text):
    for i in range(0,len(text)+4):
        print("*",end="")
    print(f"\n* {text} *")
    for i in range(0,len(text)+4):
        print("*",end="")
    print("")

headline("Sluneční soustava")
headline("Slunce")
headline("Planety")
headline("Planetky")
headline("Měsíce")
headline("Komety")
headline("Asteroidy")
headline("Galaxie")
headline("Černé Díry")
###############################################

print("--------------------------------------")
print("Multiplication.")
def multiply1(a, b):
    result = a * b
    return(result)

x = multiply1(2, 5)
print(x)

# Same function siplyfied.
def multiply2(a, b):
    return(a * b)

print(multiply2(2, 5))