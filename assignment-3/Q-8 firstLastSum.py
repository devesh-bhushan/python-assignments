"""
program to add first and the last digit of a number

"""
nu1 = int(input("enter the number"))


def digfst(n):                    # function to add the digit of number
    while n > 2:
        n //= 10
    return n


def diglst(n):                    # function to add the digit of number
    rem = n % 10
    return rem


sum = digfst(nu1) + diglst(nu1)
print("sum of first and last digit is", sum)