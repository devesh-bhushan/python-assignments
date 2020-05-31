"""
program to find the  Second Largest value in a list
"""
lst = []
element = int(input("enter the no of elements in the list"))
for i in range(element):
    data = int(input("enter the data in the list"))
    lst.append(data)
lst.sort()
print("The second Largest element in the list is", lst[-2])