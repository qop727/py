# setting dictionary
grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}

# eggs price correction
eggs_price = grocery_inventory["Eggs"][1]
if eggs_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"] = (grocery_inventory["Eggs"][0], eggs_price - 1, grocery_inventory["Eggs"][2])
else:
    print("The price of Eggs is reasonable.")

# adding tomatoes to dictionary
grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes:", grocery_inventory)

# stock of milk
milk_stock = grocery_inventory["Milk"][2]
if milk_stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory["Milk"] = (grocery_inventory["Milk"][0], grocery_inventory["Milk"][1], milk_stock + 20)
else:
    print("Milk has sufficient stock.")

# removing apples
apples_price = grocery_inventory["Apples"][1]
if apples_price > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

# final state of dictionary
print("Updated inventory:", grocery_inventory)
