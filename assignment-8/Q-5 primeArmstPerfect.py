"""
program to calculate whether the given number is prime,armstrong,perfect using function

"""
num = int(input("enter the number"))


def prime(n):
    k = 0
    for i in range(2, n//2+1):
        if n % i == 0:
            k = k + 1
    if k <= 0:
        print(n, "is prime number")
    else:
        print("number is not prime number")


def armstrong(n):
    if n == sum(int(i) ** len(str(n)) for i in str(n)):
        print("number is armstrong")
    else:
        print("number is not armstrong")


def perfect(n):
    k = 0
    for i in range(1, n):
        if n % i == 0:
            k = k + i
    if k == n:
        print(n, "is perfect number")
    else:
        print(n, "is not perfect number")


prime(num)
armstrong(num)
perfect(num)