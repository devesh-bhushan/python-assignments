"""
program to check whether the number is prime or not
"""
nu1 = int(input("enter the number "))


def prime(n):
    k = 0
    for i in range(2, n//2+1):
        if n % i == 0:
            k = k + 1
    if k <= 0:
        print(n, "is prime number")
    else:
        print("number is not prime number")


prime(nu1)