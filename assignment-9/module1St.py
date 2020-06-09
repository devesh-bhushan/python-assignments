"""
this is the module created to find out the length of the string ,
to perform the concation of the string and
to return the string in proer , uppper and lower case
"""


def length(*argument):  # function to find the length of string
    d = {}
    for i in argument:
        d[i] = len(i)
    print("length of each element is")
    print(d)


def concat(*argument):  # function to concatinate n strings
    st = ""
    for i in argument:
        st = st + i
    print("concationation of string is")
    print(st)


def upperlowerpro(*string):  # function to convert string in upper ,lower and proper case
    lst = []
    for i in string:
        st3 = str.title(i)
        st1 = str.upper(i)
        st2 = str.lower(i)
        lst.append(st1)
        lst.append(st2)
        lst.append(st3)
    print("string in upper,lower and proper case is")
    print(lst)


