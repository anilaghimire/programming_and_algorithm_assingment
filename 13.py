# Write a Python script to concatenate following dictionaries to create a new one.
dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}
dict4 = {}

for i in (dict1, dict2, dict3):
    dict4.update(i)

print(f"The New Dictionary after concatenate {dict1} , {dict2} & {dict3} is: {dict4}")