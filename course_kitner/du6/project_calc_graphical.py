# Graphical calculator.

import tkinter as tk

# Function to show the text of pressed button inside the widget.
def on_click(item):
    current_exp = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_exp + str(item))

# Function to evaluate the input inside of the widget.
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Chyba v zadání.")

# C button function to clear the widget.
def clear_entry():
    entry.delete(0, tk.END)

# Create the main window.
win = tk.Tk()
win.title("Kalkulačka")

# Create an entry widget for the calculator display.
entry = tk.Entry(win, width=30, borderwidth=5, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define the calculator buttons and their grid positions (label, row, column).
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 5, 2), ("+", 4, 3),
]

# Create and place the buttons in the grid.
for (text, row, col) in buttons:
    if text == "=":                                                 # Defining "=" button.
        btn = tk.Button(win, text=text, padx=40, pady=20, font=("Arial", 16), fg="green", command=calculate)
    else:                                                           # Other buttons append their text to the display.
        btn = tk.Button(win, text=text, padx=40, pady=20, font=("Arial", 14),
                        command=lambda txt=text: on_click(txt))
    btn.grid(row=row, column=col)

# Create a C button to reset the display.
clear_button = tk.Button(win, text="   C   ", padx=79, pady=20, font=("Arial", 14), fg="red", command=clear_entry)
clear_button.grid(row=5, column=0, columnspan=2)

win.mainloop()                                                     # Starting the main loop.