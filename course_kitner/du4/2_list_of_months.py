# Program to print filtered list of moths.

print("\nProgram vypíše vyfiltrovaný seznam měsíců.\n")         # Printing what does the program do.

months = ["leden", "únor", "březen", "duben", "květen", "červen",           # Creating list of months.
          "červenec", "srpen", "září", "říjen", "listopad", "prosinec"]

print("Každý druhý měsíc:")                                     # Printing even months.
for i in range(1, len(months), 2):                              # (start, end=lenght of list, step)
    print(months[i])

even_months = [months[i] for i in range(1, len(months), 2)]     # Creating list of even months with for cycle inside.

print("\nReverzní seznam sudých měsíců:")
for rev_month in reversed(even_months):                         # Printing reversed list of even months.
    print(rev_month)

print("\nReverzní seznam měsíců:")
for rev_month in reversed(months):                              # Printing reversed list of months.
    print(rev_month)
print("")