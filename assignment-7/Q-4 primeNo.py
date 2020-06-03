"""
program to create a list of prime number upto n number
"""
no_of_elem = int(input("enter the nth element"))


def prime_no(a):
    lst2 = [num for num in range(2, a+1) if 0 not in[num % i for i in range(2,  int(num//2) + 1)]]
    print("All prime number upto n are", lst2)


prime_no(no_of_elem)