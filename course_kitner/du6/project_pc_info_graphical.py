# Graphical program to show PC basic info.

import tkinter as tk
import platform
import psutil

# Function to get PC info.
def get_system_info():
    os_info = f"OS:     {platform.system()} {platform.release()}"   # Getting OS info.
    
    cpu_name = platform.processor() or platform.uname().machine     # Getting CPU info.
    freq = psutil.cpu_freq()
    if freq:
        cpu_freq = f"{freq.current:.2f} MHz"
    else:
        cpu_freq = "    N/A"
    cores = psutil.cpu_count(logical=False)
    logical_cores = psutil.cpu_count(logical=True)
    cpu_info = f"CPU:     {cpu_name}\nFrequency:     {cpu_freq}\nCores:     {cores} physical, {logical_cores} logical"
    
    ram_total = psutil.virtual_memory().total / (1024**3)           # Getting RAM info.
    ram_info = f"RAM:     {ram_total:.2f} GB"
    
    return f"{os_info}\n{cpu_info}\n{ram_info}"                     # Concatenating info into one string.

# Function of the button to get system info and put it into the label.
def button_show_info():
    info = get_system_info()
    info_label.config(text=info)

# Setting up the window.
win = tk.Tk()
win.title("System Info")
win.geometry("650x350")

# Button creation.
button = tk.Button(win, text="Show System Info", command=button_show_info, font=("Helvetica", 14))
button.pack(pady=20)

# Label creation.
info_label = tk.Label(win, text="", font=("Helvetica", 12), justify="left")
info_label.pack(pady=20)

win.mainloop()                                                      # Starting the main loop.