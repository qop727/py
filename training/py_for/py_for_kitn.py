for i in range(5,0,-1):
    print(i)

print("######################################")
# Program to print every even number in range from 2 - 20.
for i in range(2, 21, 2):           # (start, end+1, step)
    print(i)

print("######################################")
# Program to print every even number in range from 20 - 2.
for i in range(20, 0, -2):           # (start, end+1, step)
    print(i)

print("######################################")
# Program to print the list of planets.
list1 = ["Merkur", "Venuše", "Země", "Mars", "Jupiter", "Saturn", "Uran", "Neptun"] # Creating a list of planets.

for i in list1:                                              # Printing a list. 
    print(i)

print("######################################")
# Program to print specified number of planets in the list.
list2 = ["Merkur", "Venuše", "Země", "Mars", "Jupiter", "Saturn", "Uran", "Neptun"]     # Creating a list of planets.

for i in range(8):                                          # Printing a list. 
    print(list2[i])

print("######################################")
# Program to print a string.
string = "Hello World"

for x in string:
    print(x, end='')
print("")
print("Něco dalšího...")

print("######################################")
# Program to print numbers.
for i in range(12):
    print("*",  end="")
print("*")
print("Počítání po 3")

for i in range(12):
    print("*",  end="")
print("*")

for i in range(0, 22, 3):
    print(i)