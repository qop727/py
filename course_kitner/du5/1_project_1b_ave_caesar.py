# Program to encrypt and decrypt text with Caesars cipher.

def graphical_headline(headline):                                       # Creating function for graphical headline.
    for i in range(0,len(headline)+4):
        print("-",end="")
    print(f"\n| {headline} |")
    for i in range(0,len(headline)+4):
        print("-",end="")
    print("")

def encrypt(text, shift):                                               # Encrypt text using Caesar cipher with the given shift.
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
            else:
                result += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
        else:
            result += char
    return result

def decrypt(text, shift):                                               # Decrypt text using Caesar cipher with the given shift.
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord("A") - shift) % 26 + ord("A"))
            else:
                result += chr((ord(char) - ord("a") - shift) % 26 + ord("a"))
        else:
            result += char
    return result

graphical_headline("Ave Caesar!")

while True:
    mode = input("Zadejte, prosím, funkci \"s\" pro šifruj, nebo \"d\" pro dešifruj: ").strip().lower()    # Choosing the mode of the program.
    if mode == "s" or mode == "d" and len(mode) == 1:
        break

while True:                                                             # Making the program to ask again if an error occurs.
    try:
        shift = int(input("Zadejte, prosím, posun šifry: ").strip())    # Shift input.
        if 0 < shift <= 25:                                             # Calculating the conditions.
            break
        else:
            print("Chyba: Zadejte, prosím, posun šifry od 1 do 25.")    # Warn if the input is wrong.
    except ValueError:
        print("Chyba: Zadejte, prosím, celé číslo.")                    # Warn if the input is wrong.

while True:
    text = input("Zadejte, prosím, text, který chcete zpracovat: ")     # Input text to process.
    if len(text) > 0 and not(any(char.isdigit() for char in text)):
        break
    else:
        print("Chyba: Text nesmí obsahovat číslice.")

if mode == "s":                                                         # Text processing.
    output_text = encrypt(text, shift)
    print(f"Zašifrovaný text: {output_text}")
elif mode == "d":
    output_text = decrypt(text, shift)
    print(f"Dešifrovaný text: {output_text}")
else:
    print("Objevila se nespecifikovaná chyba.")
print("")