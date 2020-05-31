"""
program to find the greatest among two number
"""
nu1 = eval(input("enter the first number"))
nu2 = eval(input("enter the second number"))
nu3 = eval(input("enter the third number"))


def greater(a, b, c):                                  # function to find greatest among three number
    if (a > b) and (a > c):
        print("greatest number is", a)
    elif(b > a) and (b > c):
        print("greatest number is", b)
    elif(c > a) and (c > b):
        print("greatest number is", c)
    elif(a == b) and (b == c):
        print("all numbers are equal")


greater(nu1, nu2, nu3)                               # calling of function



