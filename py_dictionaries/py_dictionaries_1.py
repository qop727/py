# defining dictionary
grocery_inventory = {
	"Milk": (113, "Dairy"),
	"Eggs": (116, "Dairy"),
	"Bread": (117, "Bakery"),
	"Apples": (141, "Produce")
	}
# getting bread details
bread_details = grocery_inventory.get("Bread")
print("Details of Bread:", bread_details)
# updating dictionary
grocery_inventory.update({"Cookies": (143, "Bakery")})
print("Inventory after adding Cookies:", grocery_inventory)
# removing item
grocery_inventory.pop("Eggs")
print("Inventory after removing Eggs:", grocery_inventory)