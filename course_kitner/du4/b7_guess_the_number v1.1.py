# Program guess the number. v1.1
import random

number = random.randint(1, 100)
guesses = 0

print("")
for i in range(27):
    print("$",  end="")
print("\nVítejte v hře Uhodni číslo!")                                                      # Printing what does the program do.
for i in range(27):
    print("$",  end="")
print("\n\n!!! Máte obrovskou šanci na výhru v hodnotě 100 000 Kč !!!")
print("!!! Stačí pouze napoprvé uhodnout jedo jediné číslo !!!")
print("!!! Držím Vám palce, pojďme na to !!!")

while True:                                                                                 # Making the program to ask repeatedly or in case of an error.
    try:
        guessed_number = int(input("\nUhodněte, jaké číslo od 1 do 100 si myslím: "))       # Number input.
        if not(0 < guessed_number <= 100):                                                  # Checking the limits of input.
            print("Chyba: Zadejte, prosím, číslo od 1 do 100.")                             
        elif guessed_number == number:                                                      # Checking the conditions of winning input.
            guesses += 1
            break
        elif guesses == 0:                                                                  # Checking the conditions of input and first try.
            print("\n!!! NEEE !!!")
            print("Bohužel jste to napoprvé neuhodl...")
            print("...ale můžete se pokusit to číslo uhodnout alespoň jako cenu útěchy.")
            if guessed_number > number:
                print("Číslo, které si myslím je MENŠÍ.")
            elif guessed_number < number:
                print("Číslo, které si myslím je VĚTŠÍ.")
            guesses += 1
        elif guessed_number > number:                                                       # Checking the conditions of input.
            print("\nČíslo, které si myslím je MENŠÍ.")
            guesses += 1
        elif guessed_number < number:                                                       # Checking the conditions of input.
            print("\nČíslo, které si myslím je VĚTŠÍ.")
            guesses += 1                            
    except ValueError:
        print("Chyba: Zadejte, prosím, celé číslo.")                                        # Warn if the input is wrong.

if guesses == 1:                                                                            # Deciding the winning.
    print("\n")
    for i in range(48):
        print("$",  end="")
    print("\n!!! ANOOO !!!")
    print(f"!!! GRATULUJI UHODL/A JSTE ČÍSLO {number} NAPOPRVÉ !!!")
    print("!!! JSTE BOHÁČ, VYHRÁVÁTE 100 000 Kč !!!")
    for i in range(48):
        print("$",  end="")
    print("\n\nreconnecting...\n...connection lost\n" )
else:
    print(f"\nGratuluji, uhodl/a jste číslo {number} na {guesses} pokusů.\n")