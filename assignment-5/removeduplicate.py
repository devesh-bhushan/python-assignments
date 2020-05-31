"""
program to remove duplicate elements from the list
"""
lst = []
lst2 = []
element = int(input("enter the no of elements in the list"))
for i in range(element):
    data = int(input("enter the data in the list"))
    lst.append(data)
for num in lst:
    if num not in lst2:
        lst2.append(num)
print("after removing the duplicate value from list", lst2)