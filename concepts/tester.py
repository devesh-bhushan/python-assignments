"""
using decorator function in factorial
"""

def decorator(facto):
    d= {}

    def logic(n):
        if n not in d:
            d[n] = facto(n)
        return d[n]
    return logic


@ decorator
def facto(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * facto(n-1)


res = facto
num = int(input("enter the number upto factorial to be calculated"))
for n in range(num):
    print(res(n), end="\n")

