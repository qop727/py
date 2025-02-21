# Dictionary
numbers = {773774889:"cislo na milana"}   # Cisla ukladat takto, pokud chceme hledat podle cisla.

dict = {"jablka": 10, "banany": 20}

dict["jablka"] = 1      # Zmena hodnoty.
dict["ořechy"] = 30     # Pridani hodnoty.
del dict["jablka"]      # Mazani hodnoty.

dict["jablko"] = dict["jablka"] # Prejmenovani hodnoty
del dict["jablka"]  

# Creating an inventory.
zbozi = {
    "Susenka": 50,
    "Mleko": 67,
    "Jogurt": 88,
    "Jahoda": 345,
    "Sirka": 778
}

# Printing one item.
print("Mleka na sklade:", zbozi["Mleko"])