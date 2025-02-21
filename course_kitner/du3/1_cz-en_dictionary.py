# Czech - english dictionary.

print("Program přeloží zadané české slovo do angličtiny.\n")            # Printing what does the program do.

dictionary = {                                                          # Creating database of translations.
    "ahoj": "hi",
    "nashledanou": "goodbye",
    "děkuji": "thank you",
    "dobrý večer": "good evening",
    "kolik": "how many",
    "čas": "time",
    "prosím": "please",
    "pomoc": "help",
    "dobrý": "good",
    "špatný": "bad",
}

print("Vybrat si můžete z následující databáze:")                       # Printing options to translate.
for word in dictionary:
    print(word)

while True:                                                                             # Making the program to ask again if error occurs.
    word = input("\nZadejte, prosím, české slovo z databáze, které chcete přeložit: ")  # Input a word to translate.
    if word in dictionary:                                                              # Input validation and translation.
        print(f"České slovo {word} se anglicky řekne {dictionary[word]}.")
        break    
    else:
        print("Takové slovo ve slovníku nemám!")