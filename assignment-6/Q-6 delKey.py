"""
program to delete key  of dictionary
"""
dic = {}
nu = int(input("enter the number of keys you want in dictionary"))
for i in range(nu):
    key = eval(input("enter the key of the dictionary - "))
    data = eval(input("enter the data corresponding to the value of key - "))
    dic[key] = data
print("the entered dictionary is", dic)
item = eval(input("enter the key to be removed - "))
dic.pop(item)
print("dictionary after removal key is - ", dic)

