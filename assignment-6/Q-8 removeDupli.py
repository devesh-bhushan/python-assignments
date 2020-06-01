"""
program to remove duplicate values from dictionary
"""
import null as null

dic = {}
dic2 = {}
nu = int(input("enter the number of keys you want to add"))
for i in range(nu):
    key = eval(input("enter the key of the dictionary"))
    value = eval(input("enter the data corresponding to the value of key"))
    dic[key] = value
print("the entered dictionary is", dic)
print("the dictionary after the removal of duplicate value is")
for key, value in dic.items():
    if value not in dic2.values():
        dic2[key] = value
print(dic2)