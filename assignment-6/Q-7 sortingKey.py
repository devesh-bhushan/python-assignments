"""
program to sort the keys of dictionary
"""
dic = {}
nu = int(input("enter the number of keys you want to add"))
for i in range(nu):
    key = eval(input("enter the key of the dictionary"))
    data = eval(input("enter the data corresponding to the value of key"))
    dic[key] = data
print("the entered dictionary is", dic)
print("the dictionary in sorted order is")
for i in sorted(dic):
    print(f"{i} - {dic[i]}", end="\n")
