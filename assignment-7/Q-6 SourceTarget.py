"""
program to print the output as
[0,1,2,3] -> [1,3,5,7]
[3,5,9,8] -> [true,false,true,false]
["apple","orange","pear"] -> ["A","O","P"]
["apple","orange","pear"] -> ["apple","pear"]
["apple","orange","pear"] ->[('apple',5),('orange',6),('pear',4))
"""
lst = [0, 1, 2, 3]
lst2 = [3, 5, 9, 8]
lst3 = ["apple", "orange", "pear"]
lst4 = [i+(i+1) for i in lst]
print(lst4)


lst5 = [True if i % 3 == 0 else False for i in lst2]
print(lst5)

lst6 = [name[0].upper() for name in lst3]
print(lst6)

lst7 = [name for name in lst3 if name.count('p') > 0]
print(lst7)

lst6 = [(name, len(name)) for name in lst3]
print(lst6)