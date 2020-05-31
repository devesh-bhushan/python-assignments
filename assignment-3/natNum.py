"""
Program to print all natural number upto n
"""
num = int(input("enter the  nth natural number "))


def printer(n):
    a = 1
    while n != 0:
        print( a, end="--")
        a += 1
        n -= 1


printer(num)