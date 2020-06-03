"""
program to check whether the given number is even or odd using function

"""
nu = int(input("enter the number which is to be checked"))


def even(n):
    if n % 2 == 0:
        print("given number is even")
    else:
        print("number is odd")


even(nu)
