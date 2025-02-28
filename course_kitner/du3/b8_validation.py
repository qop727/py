# Program to decide weather you have right to enter or not.

print("Program posoudí, zda máte právo vejít, či nikoli.\n")            # Printing what does the program do.

credentials = {                                                         # Creating database of credentials.
    "username": "user001",
    "password": "Python123"
}

for i in range(2, -1, -1):
    username_inp = input("Zadejte, prosím, přihlašovací jméno: ")       # Username input.
    password_inp = input("Zadejte, prosím, přihlašovací heslo: ")       # Password input.
    
    if username_inp in credentials["username"] and password_inp in credentials["password"]:     # Calculating if the credentials are correct.
        print("Vstup povolen.")
        break
    elif i > 0:
        print(f"Chyba: Zadali jste špatné přihlašovací údaje. Máte ještě {i} pokusy.")          # Printing and calculating number of attempts.
    else:
        print(f"Chyba: Zadali jste špatné přihlašovací údaje. Nemáte už žádné pokusy.")         # Zero attempts end of program.
        print(f"Program se zablokoval. Zkuste to později.")