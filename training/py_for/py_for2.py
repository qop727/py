# Program to manage stock.

# Creating the inventory with items, current stock and minimal stock.
inventory = {
    "Milk": [25, 20],
    "Eggs": [250, 200],
    "Bread": [30, 50],
    "Apples": [50, 45]
}

# Promotions dictionary
promotions = {
    "Eggs": "20% off",
    "Apples": "Buy one, get one free"
}

# Processing the inventory
for item in inventory:
	print(f"--- Processing: {item} ---")
    
    # Conditions for restocking.
	if inventory[item][0] <= inventory[item][1]:
		print(f"{item} needs restocking. Current stock: {inventory[item][0]}. Minimum required: {inventory[item][1]}")
		inventory[item][0] += 20
		print(f"Updated stock for {item}: {inventory[item][0]}")
	if item in promotions:
		print(f"Promotion for {item}: {promotions[item]}")
	else:
		print(f"No promotions for {item}")