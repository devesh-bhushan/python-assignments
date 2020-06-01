"""
program to replace the specific letter of the string

"""
st = input("enter the string")
st_1 = st[::-1]
st_2 = st_1.replace('a', '$', 4)
st_3 = st_2[::-1]
print("string after the change in letter is", st_3)