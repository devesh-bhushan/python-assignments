"""
program to count the common elements in the string
"""
lst = list([])
element = int(input("enter the no of elements in the list 1 - "))
for i in range(element):
    data = eval(input("enter the data in the list 1 - "))
    lst.append(data)
lst2 = list([])
element2 = int(input("enter the no of elements in the list 2 - "))
for i in range(element2):
    data2 = eval(input("enter the data in the list 2 - "))
    lst2.append(data2)
count = 0
for i in range(element):
    for j in range(element2):
        if lst[i] == lst2[j]:
            count += 1
print("the number of similar elements in the list are", count)