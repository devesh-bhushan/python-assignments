"""
program to swap two numbers using bitwise operator

"""
num1 = eval(input("enter the number 1"))
num2 = eval(input("enter the number 2"))
num1 = num1 ^ num2                               # swapping using two variable
num2 = num1 ^ num2
num1 = num1 ^ num2
print("value of number 1 after swapping is", num1)
print("value of number 2 after swapping is", num2)