# Improve the code not to print the last ",".

#print("Násobky")
#for i in range(1,11):
#   print(i*2, end=", ")
#print("\n")

print("\nNásobky")                  # Improvement #1.
for i in range(1, 11):
    if i != 10:
        print(i * 2, end=", ")
    else:
        print(i * 2, end=" ")
print("\n")

#####################################################
print("\nNásobky")                  # Improvement #2.
i = 1
while i != 10:
        print(i * 2, end=", ")
        i += 1
print(i * 2, "\n")

#####################################################
print("\nNásobky")                  # Improvement #3.
násobky = [str(i * 2) for i in range(1, 11)]
print(", ".join(násobky))
print("\n")