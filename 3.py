# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character
# are same from a given list of strings.

data = ["abc", "138", "741", "wcw", "k", "ap"]

total = 0

for i in range(0, len(data)):
    a = data[i]

    if len(a) >= 2:
        first = a[0]
        last = a[len(a) - 1]

        if first == last:
            total = total + 1

print(f"The Number of string having first and last character same and string length 2 is : {total}")