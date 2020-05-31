st = "welcome\tto\tthe\tworld"
st
print(st)
print(st.expandtabs(tabsize=6))
arr = ["red", "black", "green", "white"]
res = '-'.join(arr)
print(res)
vow = "aeiou"
dig = "12345"
transtab = str.maketrans(vow,dig)
print(transtab)
res = st.translate(transtab)
print(res)
num = 12
num2 = 13
print("sum of {1} and {0} = {2}".format(num,num2,num+num2))
print("sum of {num1} and {num} = {2}".format(num,num2,num+num2))
