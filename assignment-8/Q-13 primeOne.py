"""
program to print all twin prime number between 1 to n

"""
num1 = int(input("enter the number upto which twin prime no is to be calculated"))


def twinprime(n):                # function to calculate the twin prime
    lst = []
    for num in range(2, n+1):
        k = 0
        for i in range(2, num//2 + 1):
            if num % i == 0:
                k = k + 1
        if k <= 0:
            lst.append(num)
    for i in range(len(lst)-1):
        if (lst[i + 1] - lst[i] == 1) or (lst[i + 1] - lst[i] == 2):
            print(lst[i], lst[i+1], sep="-")


twinprime(num1)