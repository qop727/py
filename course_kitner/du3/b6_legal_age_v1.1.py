# Program to calculate if you are of legal age or not. v1.1

print("Program vyhodnotí podle zadaného věku, zda jste, nebo nejste plnoletý.\n")   # Printing what does the program do.

while True:                                                             # Making the program to ask again if error occurs.
    try:
        age = int(input("Zadejte, prosím, kolik Vám je let: "))         # Age input.
        if 0 < age <= 150 and age >= 18:                                # Calculating the conditions.
            print("Jste plnoletý.")
            break
        elif 0 < age <= 150 and age < 18:
            print("Nejste plnoletý.")
            break
        else:
            print("Chyba: Zadejte, prosím, číslo od 1 do 150.")         # Warn if the input is wrong.
    except ValueError:
        print("Chyba: Zadejte, prosím, celé číslo.")                    # Warn if the input is wrong.