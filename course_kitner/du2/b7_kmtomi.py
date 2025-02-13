# Program to transfe kilometers to miles.

# Printing what does the program do.
print("""Program převede zadaný počet kilometrů na míle.
      """)

while True:
    try:
        # Kilometers input.
        km = float(input("Zadejte, prosím, počet kilometrů: "))
        
        # Making sure the input is above 0.
        if km > 0:
            break
        else:
            # Warn if the input is not above 0.
            print("Chyba: Zadejte, prosím, hodnotu větší než 0.")
    
    except ValueError:
        # Warn if the input is wrong.
        print("Chyba: Zadejte, prosím, číselnou hodnotu.")

# Printing the transfered kilometers to miles.
mi = float(km * 0.621371)
print(f"{km} km je {mi} mi.")