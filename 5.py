# Write a Python program to print a specified list after removing the 4th elements
alpha = ["abc" , "138" , "741", "wcw" , " k " , "ap"]
alpha_new = []

for i in range (len(alpha)):
    if i == 4 :
        continue
    else:
        alpha_new.append(alpha[i])
print("after remvoing 4th element is :",alpha_new)