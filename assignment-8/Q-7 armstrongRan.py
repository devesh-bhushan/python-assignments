"""
program to print all armstrong number between 1 to n

"""
num1 = int(input("enter the number upto which armstrong no is to be calculated"))


def armstrong(n):                              # function to calculate armstrong number
    for num in range(1, n+1):
        k = 0
        temp = num
        pwr = count(num)
        while num != 0:
            rem = num % 10
            k = k + rem ** pwr
            num = num // 10
        if temp == k:
            print(k)


def count(n):                               # function to count the no of digit of number
    counter = 0
    while n > 0:
        counter += 1
        n //= 10
    return counter


armstrong(num1)


