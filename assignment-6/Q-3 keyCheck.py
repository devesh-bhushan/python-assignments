"""
program to check whether the given key exists in dictionary or not
"""
lst = []
dic = {}
nu = int(input("enter the number of keys you want to add"))
for i in range(nu):
    key = eval(input("enter the key of the dictionary"))
    data = eval(input("enter the data corresponding to the value of key"))
    dic[key] = data
print("the entered dictionary is", dic)
for i in dic.keys():
    lst.append(i)
print(lst)
search = eval(input("enter the key to be searched"))

for i in lst:
    if i == search:
        print("key exists in dictionary")
        break
else:
    print("key does not exiSts in dictionary")
