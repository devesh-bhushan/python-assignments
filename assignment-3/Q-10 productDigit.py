"""
program to find the product of digits of a number
"""
nu1 = int(input("enter the number"))


def count(n):                    # function to do the product the digit of number
    s = 1
    while n > 0:
        rem = n % 10
        s = s * rem
        n //= 10
    return s


pr = count(nu1)                 # function calling
print("the product of digit in number", nu1, "is", pr)


