# Program to calculate four basic mathematical operations.

# Printing what does the program do.
print("""Program provede čtyři základní matematické operace se zadanými hodnotami.
Můžete zadat i čísla necelá a záporná.""")

try:
    # First input of number.
    a = float(input("Zadejte, prosím, první číslo: "))
except ValueError:
    # Warn if the first input is wrong.
    print("Chyba: Při příštím spuštění programu zadejte, prosím, první číslo správně.")
else:
    try:
        # Second iput of number.
        b = float(input("Zadejte, prosím, druhé číslo: "))
    except ValueError:
        # Warn if the second input is wrong.
        print("Chyba: Při příštím spuštění programu zadejte, prosím, druhé číslo správně.")
    else:
        # Printing the operations if the inputs are OK.
        print(f"{a} + {b} =", a + b)
        print(f"{a} - {b} =", a - b)
        print(f"{a} x {b} =", a * b)
        print(f"{a} / {b} =", a / b)