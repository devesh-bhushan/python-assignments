"""
program to check whether the number is palindrome or not
"""
nu1 = int(input("enter the number"))


def palindrome(n):                    # function ot check number
    r = 0
    nu = n
    while n > 0:
        rem = n % 10
        r = (r * 10) + rem
        n //= 10
    if nu == r:
        print("given number is palindrome")
    else:
        print("given number is not palindrome")


palindrome(nu1)                      # function calling



