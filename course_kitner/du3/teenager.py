# Program to calculate if you are teenager of not.

# Age input.
vek = int(input("Zadejte, prosím, kolik Vám je let: "))

# One way of calculating conditions.
if 13 <= vek <= 19:
    print("Jsi teenager.")
else:
    print("Nejsi teenager.")

# Second way of calculating conditions.
if vek >= 13 and vek <= 19 :
    print("Jsi teenager.")
else:
    print("Nejsi teenager.")