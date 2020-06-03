"""
program to create a list of even number upto n number
"""
no_of_elem = int(input("enter the nth element"))


def even_no(a):
    lst2 =[i for i in range(1, a+1) if i % 2 == 0]
    print("All even number upto n are", lst2)


even_no(no_of_elem)