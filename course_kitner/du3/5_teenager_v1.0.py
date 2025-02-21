# Program to calculate if you are teenager of not. v1.0

# Age input.
age = int(input("Zadejte, prosím, kolik Vám je let: "))

# One way of calculating conditions.
if 13 <= age <= 19:
    print("Jsi teenager.")
else:
    print("Nejsi teenager.")

# Second way of calculating conditions.
if age >= 13 and age <= 19 :
    print("Jsi teenager.")
else:
    print("Nejsi teenager.")