"""
program using memonic techique and decorator function
"""
def deco(fibo):
    d = {}
    def logic(n):
        if n not in d:
            d[n] = fibo(n)
        return d[n]
    return logic

@ deco
def fibo(n):
    if n == 1 or n == 0:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

res = fibo

n = int(input("enter the number whose factorial is to be calculated"))
for i in range(n):
    print(res(i), end="\n")