# Program to print a selection of months.

# Creating a list of months.
month_list = ["Leden", "Únor", "Březen", "Duben", "Květen", "Červen", "Červenec", "Srpen", "Září", "Říjen", "Listopad", "Prosinec"]

# Printing 3., 6. and 12. month.
print("Třetí měsíc je: ", month_list[2])
print("Šestý měsíc je: ", month_list[5])
print(f"Poslední měsíc je: ", month_list[-1])

# Printing what does the program do.
print("""
Dále program vypíše Vámi zadaný měsíc.""")

try:
    # Ask witch month to print.
    month = int(input("Zadejte číslo měsíce, který chcete vypsat: "))
except (ValueError, ZeroDivisionError):
    # Warn if the input is wrong.
    print("Chyba: Při příštím spuštění programu zadejte, prosím, celé číslo.")
else:
    # Print a month if the input is OK.
    print("Vámi vybraný měsíc je: ", month_list[month - 1])