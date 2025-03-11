# Program to show PC basic info.

from tkinter import *

# Setting the window and button appearance.
win = Tk()
win.title("Rock, Paper, Scissors")
win.geometry("700x600")

headline = Label(win, text = "Ahoj kámo!\nChceš si zahrát Kámen, Nůžky, Papír?\n", font = ("Arial Bold", 14))
headline.grid(column = 0, row = 0)

button1 = Button(win, text = "Hrát!", font = ("Arial Bold", 16), bg = "green", fg = "blue", command = f_button1)
button1.grid(column = 0, row = 1)

label1 = Label(win, font = ("Arial Bold", 14))
label1.grid(column = 0, row = 2)

label2 = Label(win, font = ("Arial Bold", 14))
label2.grid(column = 0, row = 3)

win.mainloop()