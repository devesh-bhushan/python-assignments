"""
Program to print all natural number upto n in reverse order
"""
num = int(input("enter the  nth natural number "))


def printer(n):                      # function to print n natural number in reverse order
    while n != 0:
        print(n, sep=" ", end="--")
        n -= 1


printer(num)                       # function calling