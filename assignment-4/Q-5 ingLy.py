
"""
program to add -ing -ly at the end of string

"""
st1 = input("enter the string")
le = len(st1)
if le > 3:
    st_2 = st1[-3:]
    if st_2 == "ing":
        st3 = st1 + 'ly'
        print(st3)
    else:
        st4 = st1 + 'ing'
        print(st4)
else:
    print(st1)

