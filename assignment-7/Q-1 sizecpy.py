"""
program to create a list that store length of elements of another list
"""
lst = []
no_of_elem = int(input("enter the no of elements you want in list"))
for i in range(no_of_elem):
    data = input("enter the data in the list")
    lst.append(data)
lst2 =[len(i) for i in lst]
print("length  of each element is", lst2)
print("the length of element corresponding to the element are")
lst3 = list(zip(lst2, lst))
print(lst3)