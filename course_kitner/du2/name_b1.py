# Program to concatenate a full name.

# Printing what does the program do.
print("Program spojí Vaše jméno a príjmení.")

try:
    # Name input.
    name = input("Zadejte, prosím, Vaše jméno: ")
except ValueError:
    # Warn if the first input is wrong.
    print("Chyba: Při příštím spuštění programu zadejte, prosím, jméno správně.")
else:
    try:
        # Surname input.
        surname = input("Zadejte, prosím, Vaše příjmení: ")
    except ValueError:
        # Warn if the second input is wrong.
        print("Chyba: Při příštím spuštění programu zadejte, prosím, jméno správně.")
    else:
        # Printing a full name if the inputs are OK.
        full_name = name + " " + surname
        print("Vaše celé jméno je", full_name, ".")
        # Other method of printing.
        # print(f"Vaše celé jméno je {name} {surname}.")