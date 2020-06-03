"""
program to calculate whether the given number is prime,armstrong,perfect using function

"""
num = int(input("enter the number upto which perfect no is to be calculated"))


def perfect(nu):                                  # function to calculate the perfect number
    for n in range(1, nu + 1):
        k = 0
        for i in range(1, n):
            if n % i == 0:
                k = k + i
        if k == n:
            print(n, end=" ")


perfect(num)