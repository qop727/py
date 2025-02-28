# Program to print list of Star Wars characters.

print("\nProgram vypíše vyfiltrovaný seznam postav ze Star Wars.\n")                    # Printing what does the program do.

sw_names1 = ["Yoda", "Vader", "Luke", "Padmé", "Sheev"]                                 # Creating lists of characters.
sw_names2 = ["Yoda", "Vader", "Sheev", "Padmé", "Leai", "Rey", "Obi-wan"]
sw_names3 = ["Sheev", "Yoda", "Vader", "Padmé", "Leai", "Rey", "Obi-wan"]
sw_names4 = ["Yoda", "Han", "Vader", "Chewbacca", "Padmé", "Leai", "Rey", "Luke", "Obi-wan", "Anakin", "Sheev"]
sw_names5 = ["Yoda", "Vader", "Chewbacca", "Padmé", "Leai", "Rey", "Obi-wan"]           # Creating list of characters witnout "Sheev".


i = 0
print("Character list 1:")
while sw_names1[i] != "Sheev":                      # Seeking Sheev.
    print(sw_names1[i])                             # Printing names of characters until Sheev is found.
    i+=1
print("Pozor Sheev je imperátor!\n")

###########################################
i = 0
print("Character list 2:")
while sw_names2[i] != "Sheev":                      # Seeking Sheev.
    print(sw_names2[i])                             # Printing names of characters until Sheev is found.
    i+=1
print("Pozor Sheev je imperátor!\n")

###########################################
i = 0
print("Character list 3:")
while sw_names3[i] != "Sheev":                      # Seeking Sheev.
    print(sw_names3[i])                             # Printing names of characters until Sheev is found.
    i+=1
print("Pozor Sheev je imperátor!\n")

###########################################
i = 0
print("Character list 4:")
while sw_names4[i] != "Sheev":                      # Seeking Sheev.
    print(sw_names4[i])                             # Printing names of characters until Sheev is found.
    i+=1
print("Pozor Sheev je imperátor!\n")

###########################################
i = 0
print("Character list 5:")
for index in range(0, len(sw_names5), 1):           # This is necessary if Sheev is not in the lists.
    if sw_names5[index] == "Sheev":
        sheev_is = True
        break
    else:
        sheev_is = False

while sw_names5[i] != "Sheev" and sheev_is == True:     # Seeking Sheev.
    print(sw_names5[i])                                 # Printing names of characters until Sheev is found.
    i+=1
if sheev_is == True:
    print("Pozor Sheev je imperátor!\n")
elif sheev_is == False:
    print("Sheev není doma.\n")