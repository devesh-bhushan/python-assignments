"""
program to use lambda function
"""
lambda n : n**3              # using lambda function type 1
res = lambda n: n**3
print(res(3))


def lamda(n):                                   # using lambda function type 12
    return lambda n: n**4


re = lamda(5)
print(re(5))
