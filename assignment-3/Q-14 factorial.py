"""
program to print factorial of a given number
"""
nu1 = int(input("enter the number"))


def factorial(n):                          # function to calculate factorial
    if n > 0:
        fact = 1
        while n != 0:
            fact = fact * n
            n = n-1
        print("the value of factorial of given number is", fact)
    elif n < 0:
       print("no factorial")
    else:
       print("factorial is 1")


factorial(nu1)                      # calling of function
