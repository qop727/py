# Program to say hello.

# Printing what does the program do.
print("Program Vás nadšeně pozdraví.")

try:
    # Name input.
    name = input("Zadejte, prosím, Vaše jméno: ")
except ValueError:
    # Warn if the input is wrong.
    print("Chyba: Při příštím spuštění programu zadejte, prosím, jméno správně.")
else:
    # Printing a hello if the inputs are OK.
    print(f"Nazdaaar {name}!!!")