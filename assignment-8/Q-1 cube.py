"""
program to find the cube of any number using function

"""
nu = int(input("enter the number whose  cube is to be calculated"))


def cube(n):
    a = n ** 3
    return a


cu = cube(nu)
print("the cube of entered number is", cu)