# Conditions

cislo = 10

# if cislo != 0:     # Nerovna se.
# if cislo == 0:     # True / False.

if cislo > 0:
   print("Jedna se o kladne cislo.")

else:
    print("Jedna se o zaporne cislo.")

print("Toto se provede vzdy.")

# Zadani x a y.
print("Zadejte hodnoty k porovnani.")
x = int(input("x:"))
y = int(input("y:"))

# Porovnavani z a y.
if x > y:
   print("x je vetsi nez y.")

if x < y:
  print("x je mensi nez y.")

if x == y:
   print("x je rovno y.")

# Zadani poctu kusu.
x = int(input("Zadejte pocet objednanych kusu: "))

# Vypocet slevy
if x >= 50:
   print("Vyse slevy je 10%.")
elif 19 < x < 50:
   print("Vyse slevy je 5%.")
elif 3 < x < 20:
   print("Vyse slevy je 3%.")
elif -1 < x < 4:
   print("Vyse slevy je 0%.")

barva = "cervena"
tvar = "kolecko"

if barva == "cervena" and tvar == "kolecko":    # Obe plati.
    print("Cervene kolecko.")

if barva == "cervena" or tvar == "kolecko":     # Jedno plati.
    print("Cervene nebo kolecko.")


