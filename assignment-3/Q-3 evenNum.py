"""
Program to print all even number between 1 to 100
"""
n = 100
a = 1
while n != 0:
    if a % 2 == 0:
        print(a, end="-")
    a += 1
    n -= 1