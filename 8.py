#write a python program to convert a tuple to a string

tup = ('a','n','l','a')
# using for loop
'''
#Here every items of tuples keeps on adding to stri string 
#later forming a string
string = ""
for items in tup:
    string = string + items
'''
#using str.join
#.join allows to add items of Tuples to a empty string converting its
#data type to string.
string = "".join(tup)
print (string)
print(type(string))

