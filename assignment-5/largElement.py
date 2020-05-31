"""
program to find the largest value in a list
"""
lst = []
element = int(input("enter the no of elements in the list"))
for i in range(element):
    data = int(input("enter the data in the list"))
    lst.append(data)
grstvalue = lst[0]
for i in lst:
    if i > grstvalue:
        grstvalue = i
print("greatest element in the list is",grstvalue)