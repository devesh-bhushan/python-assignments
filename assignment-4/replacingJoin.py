"""
 program to join two string by replacing some specific words
"""
st_1 = "hello"
st_2 = "world"
st_3 = st_1.replace('h', 'w')
st_4 = st_3.replace('e', 'o')
st_5 = st_2.replace('w', 'h')
st_6 = st_5.replace('o', 'e')
st_7 = st_4 + st_6
print(st_7)
