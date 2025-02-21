# Program to calculate BMI and decide your condition. v1.1

print("""Program provede výpočet Vašeho BMI a zařazení do skupiny.
    """)                                                                        # Printing what does the program do.

while True:                                                                     # Making the program to ask again if error occurs.
    try:
        weight = float(input("Zadejte, prosím, Vaši váhu v kilogramech: "))     # Weight input.
        if 0 < weight <= 700:                                                   # Calculating the conditions.
            break
        else:
            print("Chyba: Zadejte, prosím, číslo od 1 do 700.")                 # Warn if the input is wrong.
    except ValueError:
        print("Chyba: Zadejte, prosím, číslo.")                                 # Warn if the input is wrong.

while True:                                                                     # Making the program to ask again if error occurs.
    try:
        hight = float(input("Zadejte, prosím, Vaši výšku v metrech: "))         # Hight input.
        if 0 < hight <= 3:                                                      # Calculating the conditions.
            break
        else:
            print("Chyba: Zadejte, prosím, číslo od 1 do 3.")                   # Warn if the input is wrong.
    except ValueError:
        print("Chyba: Zadejte, prosím, číslo.")                                 # Warn if the input is wrong.

bmi = weight / (hight ** 2)                                                     # Printing the BMI if inputs are OK.
print(f"Váš Body Mass Index je: {bmi}.")

if bmi < 18.5:                                                                  # Printing the notification of your condition.
    print("Máte tedy podváhu.")
elif 18.5 <= bmi < 25:
    print("Máte tedy normální váhu.")
elif 25 <= bmi < 30:
    print("Máte tedy Nadváhu.")
elif 30 <= bmi <= 35:
    print("Máte tedy obezitu I.stupně.")
elif 35 <= bmi <= 40:
    print("Máte tedy obezitu II.stupně.")
elif bmi >= 40:
    print("Máte tedy obezitu III.stupně. Dle WHO morbidní obezitu.")