"""
Program to print multiplication table of any number
"""
nm1 = int(input("enter the number whose table is to be printed"))


def table(n):                              # calculating table of the number
    print("table of the number is")
    for i in range(1,11):
        mul = n * i
        print(n, "*", i, "=", mul, sep="")


table(nm1)         # function calling