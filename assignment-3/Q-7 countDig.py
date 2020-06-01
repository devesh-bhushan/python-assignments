"""
program to count the number of digits in a number
"""
nu1 = int(input("enter the number"))


def count(n):                               # function to count the no of digit of number
    counter = 0
    while n > 0:
        counter += 1
        n //= 10
    return counter


dig = count(nu1)                             # function calling
print("the number of digit in number", nu1, "is", dig)


