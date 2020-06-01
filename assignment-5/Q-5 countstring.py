"""
program to count string whose length is greater than 3
 and first and last elements are same
"""
lst = list([])
element = int(input("enter the no of elements in the list"))
for i in range(element):
    data = eval(input("enter the data in the list"))
    lst.append(data)
count = 0
for i in range(element):
    if (len(lst[i]) > 3) and (lst[i][0] == lst[i][-1]):
        count += 1
print("the number of string with given condition is", count)