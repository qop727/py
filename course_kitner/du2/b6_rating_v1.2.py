# Program to make an average rating. v1.2

# Printing what does the program do.
print("""Program vypočítá průměrnou hodnotu zadaných hodnocení.
Maximální počet hodnocení je 50.      
      """)

while True:
    try:
        # Number of ratings.
        number_of_ratings = int(input("Zadejte, prosím, počet hodnocení, ze kterých se bude průměr počítat: "))
        
        # Making sure the input is between 1 and 50.
        if 0 < number_of_ratings < 50:
            break
        else:
            # Warn if the input is not between 1 and 50.
            print("Chyba: Zadejte, prosím, hodnotu v rozmezí 1 až 50.")
    
    except ValueError:
        # Warn if the input is wrong.
        print("Chyba: Zadejte, prosím, celočíselnou hodnotu.")


list_of_ratings = []
# Repeating ratings input number of times defined above.
for i in range(number_of_ratings):
    while True:
        try:
            # Input.
            input_to_save = int(input(f"Zadejte, prosím, {i + 1}. hodnocení v rozsahu 1 až 5: "))
            
            # Making sure the input is between 1 and 5.
            if 1 <= input_to_save <= 5:
                break
            else:
                # Warn if the input is not between 1 and 5.
                print(f"Chyba: Zadejte, prosím, {i + 1}. hodnocení v rozsahu 1 až 5.")
        
        except ValueError:
            # Warn if the input is wrong.
            print(f"Chyba: Zadejte, prosím, {i + 1}. hodnocení jako celé číslo v rozsahu 1 až 5.")
    list_of_ratings.append(input_to_save)
    

# Calculating and printing the average rating.
average_rating = 0

for j in range(number_of_ratings):
    average_rating = float(average_rating + list_of_ratings[j])

average_rating = average_rating / number_of_ratings
print(f"Průměrné hodnocení je: {average_rating}")