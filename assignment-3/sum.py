"""
Program to print sum of all the natural number upto n
"""
num = int(input("enter the last natural number"))


def addition(n):                              # function to add natural numbers
    sm = 0
    for i in range(1, n + 1):
        sm = sm + i
    return sm


sum1 = addition(num)                         # calling of function
print("sum of the natural n1umber are", sum1)