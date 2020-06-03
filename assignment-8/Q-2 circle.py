"""
program to find the area, diameter, circumference using function

"""
rad = int(input("enter the radius of the circle"))


def diameter(r):
    dia = 2 * r
    print("diameter of the circle is", dia)


def area(r):
    ar = 3.14 * r ** 2
    print("area of the circle is", ar)


def peri(r):
    per = 2 * 3.14 * r
    print("circumference of circle is", per)


print("""
        press 1: to view diameter
        Press 2 : TO view area
        Press 3 : TO view perimeter""")
ch = int(input("enter your choice"))
if ch == 1:
    diameter(rad)
elif ch == 2:
    area(rad)
elif ch == 3:
    peri(rad)
else:
    print("invalid choice")