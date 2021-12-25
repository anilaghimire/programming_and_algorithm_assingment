# Write a Python program to remove an item from a set if it is present in the set.
data = {1, 2, 3, 4, 5, 6}
a = int(input("Enter a number to remove from set if present: "))
b = 0

for item in data:
    if item == a:
        data.remove(a)
        print("The Modified set is :", data)
        break
    else:
        b = b + 1

if b == len(data):
    print(a, " is Not found in Set : ", data)