# Program to play Rock, Paper, Scissors.

import random
import sys

options = ["Kámen", "Nůžky", "Papír"]

def graphical_headline(headline):                                                   # Creating function for graphical headline.
    for i in range(0,len(headline)+4):
        print("*",end="")
    print(f"\n* {headline} *")
    for i in range(0,len(headline)+4):
        print("*",end="")
    print("")

def f_players_turn():
    players_turn = random.choice(options)
    return players_turn

def f_pcs_turn():
    pcs_turn = random.choice(options)
    return pcs_turn

def f_player_wins():
    players_turn = f_players_turn()
    pcs_turn = f_pcs_turn()
    if players_turn == "Kámen" and pcs_turn == "Nůžky":
        print(f"\nMáš: {players_turn}")
        print(f"Já mám: {pcs_turn}")
        return True
    elif players_turn == "Kámen" and pcs_turn == "Papír":
        print(f"\nMáš: {players_turn}")
        print(f"Já mám: {pcs_turn}")
        return False
    elif players_turn == "Kámen" and pcs_turn == "Kámen":
        print(f"\nMáš: {players_turn}")
        print(f"Já mám: {pcs_turn}")
        return None
    elif players_turn == "Nůžky" and pcs_turn == "Nůžky":
        print(f"\nMáš: {players_turn}")
        print(f"Já mám: {pcs_turn}")
        return None
    elif players_turn == "Nůžky" and pcs_turn == "Papír":
        print(f"\nMáš: {players_turn}")
        print(f"Já mám: {pcs_turn}")
        return True
    elif players_turn == "Nůžky" and pcs_turn == "Kámen":
        print(f"\nMáš: {players_turn}")
        print(f"Já mám: {pcs_turn}")
        return False
    elif players_turn == "Papír" and pcs_turn == "Nůžky":
        print(f"\nMáš: {players_turn}")
        print(f"Já mám: {pcs_turn}")
        return False
    elif players_turn == "Papír" and pcs_turn == "Papír":
        print(f"\nMáš: {players_turn}")
        print(f"Já mám: {pcs_turn}")
        return None
    elif players_turn == "Papír" and pcs_turn == "Kámen":
        print(f"\nMáš: {players_turn}")
        print(f"Já mám: {pcs_turn}")
        return True

def output():
    player_wins = f_player_wins()
    if player_wins == True:
        print("\nNoo... Vyhrál jsi... Ale to bylo jen štěstí!")
    elif player_wins == False:
        print("\nSmůůůůla!!! Jsi lůůůůser!!!")
    elif player_wins == None:
        print("\nNerozhodně, musíme hrát znovu.\n")
        output()

graphical_headline("Kámen, Nůžky, Papír")
print("\nAhoj kámo!")
print("Chceš si zahrát Kámen, Nůžky, Papír?\n")

while True:                                                                         # Asking for input until it is correct.
    start = input("Zadej \"s\" pro START, nebo \"k\" pro KONEC: ").strip().lower()
    if start == "k" and len(start) == 1:                                            # Exit the program.
        sys.exit()
    elif start == "s" and len(start) == 1:
        break

output()
print("")