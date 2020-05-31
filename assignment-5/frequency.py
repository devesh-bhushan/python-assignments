"""
program to count the frequency of number in a list
"""
lst = list([])
element = int(input("enter the no of elements in the list"))
for i in range(element):
    data = eval(input("enter the data in the list"))
    lst.append(data)
freq = eval(input("enter the number whose frequency is to be calculated"))
count = lst.count(freq)
print("the frequency of the number is", count)