"""
lst = list([])


for i in range(2):
    suls = list([])
    for j in range(2):
        data = eval(input("Enter The Employee ID and Name"))
        suls.append(data)
    lst.append(suls)
"""
size=0
lst1 = []
lst =["james","anna","king","smith","kimberlee"]
for i in lst:
    size = len(i)
    lst1.append(size)
print(lst1)
