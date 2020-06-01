"""
program to print sum of items of dictionary
"""
lst = []
dic = {}
nu = int(input("enter the number of keys you want in dictionary"))
for i in range(nu):
    key = int(input("enter the key of the dictionary - "))
    data = int(input("enter the data corresponding to the value of key - "))
    dic[key] = data
print("the entered dictionary is", dic)
sm = 0
for i, j in dic.items():
    sm = sm + i + j
print("the sum of items of list is", sm)

