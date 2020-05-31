"""
program to add  the  of digits of a number
"""
nu1 = int(input("enter the number"))


def count(n):                    # function to add the digit of number
    s = 0
    while n > 0:
        rem = n % 10
        s = s + rem
        n //= 10
    return s


sum1 = count(nu1)
print("the sum of digit in number", nu1, "is", sum1)


