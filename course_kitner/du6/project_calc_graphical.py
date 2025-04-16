# Graphical calculator.

import tkinter as tk

# Function to show the text of pressed button inside the display.
def on_click(item):
    current_exp = entry.get()                   # Saves what is inside the entry display (Keyboard input).
    entry.delete(0, tk.END)                     # Deletes the entry from the display.
    entry.insert(tk.END, current_exp + str(item))   # Inserts new text to end of actual text.

# Function to evaluate the input inside of the display.
def calculate():
    try:
        result = eval(entry.get())              # Evaluates the input inside the display and saves the result.
        entry.delete(0, tk.END)                 # Deletes the entry from the display after succesful evaluation.
        entry.insert(tk.END, str(result))       # Puts the result into the display.
    except Exception:                           # Shows error if input is wrong.
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Chyba v zadání.")

# C button function to resset the display.
def clear_entry():
    entry.delete(0, tk.END)

# Create the main window.
win = tk.Tk()
win.title("Kalkulačka")

# Create an entry display for the calculator display.
entry = tk.Entry(win, width=30, borderwidth=5, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define the calculator buttons and their grid positions (label, row, column).
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
                 ("0", 4, 1), (".", 4, 2), ("+", 4, 3),
]

# Create and place the buttons in the grid and locking the text of button into lambda function.
for (text, row, col) in buttons:
    btn = tk.Button(win, text=text, padx=40, pady=20, font=("Arial", 14), command=lambda txt=text: on_click(txt))
    btn.grid(row=row, column=col)

# Create a = button.
clear_button = tk.Button(win, text="   =   ", padx=79, pady=20, font=("Arial", 14), fg="green", command=calculate)
clear_button.grid(row=5, column=2, columnspan=2)

# Create a C button for display resetting.
clear_button = tk.Button(win, text="   C   ", padx=79, pady=20, font=("Arial", 14), fg="red", command=clear_entry)
clear_button.grid(row=5, column=0, columnspan=2)

win.mainloop()                                  # Starting the main loop.