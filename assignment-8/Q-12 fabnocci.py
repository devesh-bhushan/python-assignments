"""
function to find factorial of any number
"""
nu = int(input("enter the number upto which fibonacci series is to be calculated"))


def fibonacci(n):                                 # function to calculate the fibonacci series
    print("the fibonacci series upto nth number is")
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a+b


fibonacci(nu)
