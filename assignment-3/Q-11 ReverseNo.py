"""
program to reverse a number
"""
nu1 = int(input("enter the number"))


def reverse(n):                    # function ot reverse a number
    r = 0
    while n > 0:
        rem = n % 10
        r = (r * 10) + rem
        n //= 10
    return r


rev = count(nu1)                      # function calling
print("the sum of digit in number", nu1, "is", rev)


