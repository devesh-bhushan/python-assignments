"""
function to find factorial of any number
"""
nu = int(input("enter the number"))


def factorial(n):                            # function to calculate the factorial of any number
    if n == 0:
        print("factorial is 1")
    elif n >= 1:
        num1 = 1
        while n > 0:
            num1 = num1 * n
            n -= 1
        print("the factorial of the number is", num1)


factorial(nu)
