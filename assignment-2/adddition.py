"""
program to perform addition of two number
"""
num1 = eval(input("enter the first number "))
num2 = eval(input("enter the second number"))


def add(a, b):                      # function to perform addition of 2 number
    su = a+b
    return su


su_1 = add(num1, num2)               # calling of function
print("addition of two number is", su_1)
