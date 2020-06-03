"""
Program to find the maximum and minimum between two numbers
"""
nu1 = int(input("enter the first number"))
nu2 = int(input("enter the second number"))


def maximum(a, b):
    if a > b:
        print("maximum number is", a)
        print("minimum number is", b)
    else:
        print("maximum number is", b)
        print("minimum number is", a)


maximum(nu1, nu2)
