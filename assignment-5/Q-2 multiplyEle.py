"""
program to Multiply all the elements in a list
"""
lst = []
element = int(input("enter the no of elements in the list"))
for i in range(element):
    data = int(input("enter the data in the list"))
    lst.append(data)
multi = 1
for i in lst:
    multi = multi * i
print("multiplication of all element of the list is", multi)