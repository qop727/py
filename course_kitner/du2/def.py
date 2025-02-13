# Program to train def function.

print("--------------------------------------")
print("Printing powers of number.")
def powers(n):
    print(n, "na druhou je", n ** 2)
    print(n, "na treti je", n ** 3)
    print(n, "na ctvrtou je", n ** 4)

powers(5)
###############################################

print("--------------------------------------")
print("Printing rest of chocolate.")
def chocolate(rows, columns, x):
    rest = rows * columns - x
    print("Zbytek:", rest)

chocolate(5, 8, 12)
###############################################

print("--------------------------------------")
print("Printing math operations.")
def sum_dif(a, b):
    print(f"{a} + {b} =", a + b)
    print(f"{a} - {b} =", a - b)

sum_dif(5, 8)
###############################################

print("--------------------------------------")
print("Printing days, hours and minutes of defined number of weeks.")
def weeks(n):
    print("Pocet dnu:", n * 7)
    print("Pocet hodin:", n * 168)
    print("Pocet minut:", n * 10080)

weeks(6)
###############################################

print("--------------------------------------")
print("Printing tuples with informations.")
def information(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

information(name="Petr", age=30, city="Praha", saa="ahoj")
information(name="Jan", age=38, city="Brno")
information(name="Ondrej", age=34, city="Pardubice")
print("--------------------------------------")
