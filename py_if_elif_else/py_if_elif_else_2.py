# Input variables
days_until_expiration = 5
stock_level = 60
product_type = "Perishable"

# Setting conditions for discout.
if product_type == "Perishable":

    if days_until_expiration <= 3 and stock_level > 50:
        print("30% discount applied!")

    elif days_until_expiration > 3 and days_until_expiration <= 6 and stock_level > 50:
        print("20% discount applied!")

    elif days_until_expiration > 6 and stock_level <= 50:
        print("10% discount applied!")

else:
    print("No discount available for non-perishable items.")
