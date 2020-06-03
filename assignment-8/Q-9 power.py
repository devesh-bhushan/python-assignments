"""
program to calculate the power of any number
"""
base = int(input("enter the base of the number"))
exponent = int(input("enter the exponent on the base"))


def power(a, b):             # function to calculate the power of number
    print("power of the number is", a ** b)


power(base, exponent)