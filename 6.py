#Write a Python program to select an item randomly from a list.

import random
alpha = ["rty", "456", "sde","765"]

a = random.randint (0,len(alpha))
print(f" the randomly selected item is :" , alpha [a])
