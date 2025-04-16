# Graphical program to play Rock, Paper, Scissors.

from tkinter import *
from tkinter import messagebox
import random
import time

options = ["Kámen", "Nůžky", "Papír"]               # Setting list of options to random.
results = {                                         # Setting dictionary to compare results.
    "Kámen": {"Kámen": None, "Nůžky": True, "Papír": False},
    "Nůžky": {"Kámen": False, "Nůžky": None, "Papír": True},
    "Papír": {"Kámen": True, "Nůžky": False, "Papír": None},
}

# Function to random option.
def f_random():
    turn = []
    turn = random.choice(options)
    return turn

# Function of the button.
def f_button1():
    players_turn = f_random()
    pcs_turn = f_random()
    button1.configure(text="Hrát znovu!")
    label1.configure(text=f"\nMáš: {players_turn}\nJá mám: {pcs_turn}")
    player_wins = results[players_turn][pcs_turn]

    if player_wins == True:                         # Deciding whos the winner.
        label2.configure(text="\nNoo...Vyhrál jsi...\nAle to bylo jen štěstí!", fg="green")
        time.sleep(2)
        messagebox.showinfo("Vyhrál jsi.", "Noo...\nVyhrál jsi...\nAle to bylo jen štěstí!   ")
    elif player_wins == False:
        label2.configure(text="\nSmůůůůla!!!\nJsi lůůůůser!!!", fg="red")
        time.sleep(2)
        messagebox.showerror("Prohrál jsi.", "Smůůůůla!!!\nJsi lůůůůser!!!   ")
    elif player_wins == None:
        label2.configure(text="\nNerozhodně.\nMusíme hrát znovu.", fg="orange")
        time.sleep(2)
        messagebox.showwarning("Nerozhodně.", "Musíme hrát znovu.")


# Setting the window and button appearance.
win = Tk()
win.title("Rock, Paper, Scissors")
win.geometry("700x600")

headline = Label(win, text="Ahoj kámo!\nChceš si zahrát Kámen, Nůžky, Papír?\n", font=("Arial Bold", 14))
headline.grid(column=0, row=0)

button1 = Button(win, text="Hrát!", font=("Arial Bold", 16), bg="green", fg="blue", command=f_button1)
button1.grid(column=0, row=1)

label1 = Label(win, font=("Arial Bold", 14))
label1.grid(column=0, row=2)

label2 = Label(win, font=("Arial Bold", 14))
label2.grid(column=0, row=3)

win.mainloop()