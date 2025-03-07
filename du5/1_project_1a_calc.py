# Program to calculate basic mathematical operations of your choosing.

import math
import sys
list_of_operations = ["+", "-", "x", "/", "umocni", "odmocni", "UKONCI"]

def print_the_list():                                   # Creating function for printing the list of available operations.
    print(end="| ")
    for i in list_of_operations:
        print(i, end=" | ")
    print("")

def graphical_headline(headline):                       # Creating function for graphical headline.
    for i in range(0,len(headline)+4):
        print("-",end="")
    print(f"\n| {headline} |")
    for i in range(0,len(headline)+4):
        print("-",end="")
    print("")

def math_operation_choosing():                          # Creating function for choosing the math operation.
    while True:
        operation = input("Zadejte, prosím, jakou matematickou operaci chcete použít: ")
        if operation == list_of_operations[6]:          # Exit the program.
            sys.exit()
        elif operation == list_of_operations[0]:        # Operation 0.
            a, b = two_number_input()
            print(f"{a} + {b} = {add(a, b)}")
            break
        elif operation == list_of_operations[1]:        # Operation 1.
            a, b = two_number_input()
            print(f"{a} - {b} = {subtract(a, b)}")
            break
        elif operation == list_of_operations[2]:        # Operation 2.
            a, b = two_number_input()
            print(f"{a} x {b} = {multiply(a, b)}")
            break
        elif operation == list_of_operations[3]:        # Operation 3.
            a, b = two_number_input()
            while b == 0:                               # Taking care of no 0 dividion.
                print("Chyba: Nelze dělit 0.")
                a, b = two_number_input()
            print(f"{a} / {b} = {divide(a, b)}")
            break
        elif operation == list_of_operations[4]:        # Operation 4.
            a = one_number_input()
            print(f"{a} na druhou = {exponentiate(a)}")
            break
        elif operation == list_of_operations[5]:        # Operation 5.
            a = one_number_input()
            print(f"Odmocnina z {a} = {extract_the_root(a)}")
            break

def one_number_input():                                 # Creating function for one input.
    while True:
        try:
            a = float(input("Zadejte, prosím, číslo: "))
        except ValueError:
            print("Chyba: Zadejte, prosím, číslo správně.")
        break
    return(a)

def two_number_input():                                 # Creating function for two inputs.
    while True:
        try:
            a = float(input("Zadejte, prosím, první číslo: "))
        except ValueError:
            print("Chyba: Zadejte, prosím, první číslo správně.")
        else:
            try:
                b = float(input("Zadejte, prosím, druhé číslo: "))
            except ValueError:
                print("Chyba: Zadejte, prosím, druhé číslo správně.")
            break
    return(a, b)

def add(a, b):                                          # Creating function for adding.
    return a + b

def subtract(a, b):                                     # Creating function for subtracting.
    return a - b

def multiply(a, b):                                     # Creating function for multiplying.
    return a * b

def divide(a, b):                                       # Creating function for dividing.
    return a / b

def exponentiate(a):                                    # Creating function for exponentiation.
    return math.pow(a, 2)

def extract_the_root(a):                                # Creating function for extracting the root.
    return math.sqrt(a)

graphical_headline("Kalkulačka")
print("Zadáním jedné z možností aktivujete matematickou operaci, nebo program ukončíte:")
print_the_list()
math_operation_choosing()
print("")