# Program to train libraries.

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def nasob(a, b):
    return a*b

def vydel(a, b):
    if b == 0:
        raise ValueError("Dělení nulou není povoleno.")
    return a/b


