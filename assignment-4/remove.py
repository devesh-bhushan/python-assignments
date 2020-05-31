
"""
program to remove element from  nth index
"""
st2 = ""
st1 = input("enter the string")
ind = int(input("enter the index to be removed"))
for i in range(len(st1)):
    if i != ind:
        st2 = st2 + st1[i]
print(st2)
