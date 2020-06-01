"""
program to count string whose length is greater than 3
 and first and last elements are same
"""
lst = list([])
element = int(input("enter the no of elements in the list - "))
subelement = int(input("enter the number of elements in sub list - "))
for i in range(element):
    sublst = list([])
    for j in range(subelement):
        data = eval(input("enter the data in the list - "))
        sublst.append(data)
    lst.append(sublst)
print(lst)

res = list([])
for i in lst:
    sm = 0
    for j in i:
        sm = sm + j
    res.append(sm)
res.sort()
#  print(res)  for checking purpose whether the sum stored in the list is right or not
print("the highest sum of list is", res[-1])