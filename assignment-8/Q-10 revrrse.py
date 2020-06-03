"""
function to reverse any number
"""
nu = int(input("enter the number"))


def reverse(n):                            # function to calculate the reverse of any number
    num1 = 0
    while n > 0:
        rem = n % 10
        num1 = (num1 * 10) + rem
        n //= 10
    return num1


reverse_nu = reverse(nu)
print("the reverse of the number is", reverse_nu)