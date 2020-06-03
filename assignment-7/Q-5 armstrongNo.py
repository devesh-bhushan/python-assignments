"""
program to create a list of armstrong number upto n number
"""
no_of_elem = int(input("enter the nth element"))


def armst_no(a):
    lst2 = [num for num in range(1, a+1) if num == sum(int(j) ** len(str(num)) for j in str(num))]
    print("All armstrong number upto n are", lst2)


armst_no(no_of_elem)