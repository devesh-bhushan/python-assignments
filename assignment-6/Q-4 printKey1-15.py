"""
program to print the keys of dictionary
 between 1-15 and whose value is square of ket
"""
lst = []
dic = {}
nu = int(input("enter the number of keys you want to add"))
for i in range(nu):
    key = int(input("enter the key of the dictionary"))
    data = int(input("enter the data corresponding to the value of key"))
    dic[key] = data
print("the entered dictionary is", dic)
for i, j in dic.items():
    if (1 <= i <= 15) and (i**2 == j):
        print(f"condition satisfied key and value are {i} - {j}")
else:
    print("key and value to satisfy the condition does not exists in dictionary")
