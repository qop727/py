#Determine variables.
seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100

#Determine discount.
overstockRisk = seasonal and (current_stock > high_stock_threshold)
discountEligible = not selling_well and not on_sale
makeDiscount = overstockRisk or discountEligible

print("Should the item be discounted?", makeDiscount)