""""
program to add new key to the dictionary
"""
dic = {}
nu = int(input("enter the number of keys you want to add"))
for i in range(nu):
    key = eval(input("enter the key of the dictionary"))
    data = eval(input("enter the data corresponding to the value of key"))
    dic[key] = data
print(dic)