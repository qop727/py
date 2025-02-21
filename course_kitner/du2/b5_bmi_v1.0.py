# Program to calculate BMI. v1.0

# Printing what does the program do.
print("Program provede výpočet Vašeho BMI.")

try:
    # Weight input.
    weight = float(input("Zadejte, prosím, Vaši váhu v kilogramech: "))
except (ValueError, ZeroDivisionError):
    # Warn if the first input is wrong.
    print("Chyba: Při příštím spuštění programu zadejte, prosím, váhu správně.")
else:
    try:
        # Hight input.
        hight = float(input("Zadejte, prosím, Vaši výšku v metrech: "))
    except (ValueError, ZeroDivisionError):
        # Warn if the second input is wrong.
        print("Chyba: Při příštím spuštění programu zadejte, prosím, výšku správně.")
    else:
        # Printing the BMI if inputs are OK.
        bmi = weight / (hight ** 2)
        print(f"Váš Body Mass Index je: {bmi}.")