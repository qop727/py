# Program to save and print the shopping list.

print("Program uloží a vypíše nákupní seznam, který zadáte.\n")         # Printing what does the program do.
print("Maximální počet položek je 30.")
print("Maximální délka názvu položky je 20 znaků.\n")

shopping_list = []                                                      # Creating empty shopping list.
i = 0
while True:                                                             # Making the program to ask repeatedly to save all items or in case of an error.
    item = input(f"Zadejte, prosím, {i+1}. položku seznamu: ")          # Item input.
    if 0 < len(item) <= 20 and i < 29 and item != "konec":              # Checking right name lenght of item, maximum number of items in the list and an input "konec".
        print("Položka uložena. Pro ukončení vkládání položek zadejte \"konec\".")
        shopping_list.append(item)                                      # Saving an item into the list.
        i += 1
    elif len(item) > 20:                                                # Checking right name lenght of item.
        print("Maximální délka názvu položky je 20 znaků.")
    elif item == "konec":                                               # Checking an input "konec".
        break
    elif i > 28:
        print("Dosáhli jste maximálního počtu položek v seznamu.")      # Checking maximum number of items in the list.
        break
    else:
        print("Vyplňte, prosím, pole pro uložení položky, nebo zadejte \"konec\" pro ukončení vkládání.")

if i == 0:
    print("\nSeznam je prázdný.\n")
else:
    print("\nVypisuji uložený seznam:")
    for item in shopping_list:                                           # Printing the shopping list.
        print(item)
    print("")