"""
lst = list([])


for i in range(2):
    suls = list([])
    for j in range(2):
        data = eval(input("Enter The Employee ID and Name"))
        suls.append(data)
    lst.append(suls)

size=0
lst1 = []
lst =["james","anna","king","smith","kimberlee"]
for i in lst:
    size = len(i)
    lst1.append(size)
print(lst1)
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