# Program to make average rating. v1.1

# Printing what does the program do.
print("""Program vypočítá průměrnou hodnotu tří zadaných hodnocení.
      """)

while True:
    try:
        # First input.
        rating1 = int(input("Zadejte, prosím, první hodnocení v rozsahu 1 až 5: "))
        
        # Making sure the first input is between 1 and 5.
        if 1 <= rating1 <= 5:
            break
        else:
            # Warn if the first input is not between 1 and 5.
            print("Chyba: Zadejte, prosím, první hodnocení v rozsahu 1 až 5.")
    
    except ValueError:
        # Warn if the first input is wrong.
        print("Chyba: Zadejte, prosím, první hodnocení jako celé číslo v rozsahu 1 až 5.")

while True:
    try:
        # Second input.
        rating2 = int(input("Zadejte, prosím, druhé hodnocení v rozsahu 1 až 5: "))
        
        # Making sure the second input is between 1 and 5.
        if 1 <= rating2 <= 5:
            break
        else:
            # Warn if the second input is not between 1 and 5.
            print("Chyba: Zadejte, prosím, druhé hodnocení v rozsahu 1 až 5.")
    
    except ValueError:
        # Warn if the second input is wrong.
        print("Chyba: Zadejte, prosím, druhé hodnocení jako celé číslo v rozsahu 1 až 5.")

while True:
    try:
        # Third input.
        rating3 = int(input("Zadejte, prosím, třetí hodnocení v rozsahu 1 až 5: "))
        
        # Making sure the third input is between 1 and 5.
        if 1 <= rating3 <= 5:
            break
        else:
            # Warn if the third input is not between 1 and 5.
            print("Chyba: Zadejte, prosím, třetí hodnocení v rozsahu 1 až 5.")
    
    except ValueError:
        # Warn if the third input is wrong.
        print("Chyba: Zadejte, prosím, třetí hodnocení jako celé číslo v rozsahu 1 až 5.")


# Printing the average rating.
average_rating = float((rating1 + rating2 + rating3) / 3)
print(f"Průměrné hodnocení je: {average_rating}")