"""
program to print all prime number between 1 to n

"""
num1 = int(input("enter the number upto which prime no is to be calculated"))


def prime(n):
    for num in range(2, n+1):
        k = 0
        for i in range(2, num//2 + 1):
            if num % i == 0:
                k = k + 1
        if k <= 0:
            print(num)


prime(num1)

