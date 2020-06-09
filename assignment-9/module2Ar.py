"""
this is the module to commute the area of
circle,cube,triangle,cylinder
"""


def cube(a):  # function to calculate the area of cube

    res = (a ** 2) * 6
    print("area is - ", res)


def circle(r):  # function to calculate the area of circle

    res = 3.14 * r ** 2
    print("area is - ", res)


def cylinder(r, h):  # function to calculate the area of cylinder

    lst = []
    cu_su_ar = 3.14 * (r ** 2) * h
    su_ar = 2 * 3.14 * (r ** 2)
    lst.append("curved surface area is - ")
    lst.append(cu_su_ar)

    lst.append(" - face area is")
    lst.append(su_ar)
    print(lst)


def triangle(base, height):  # function to calculate the area of triangle

    res = .5 * (base * height)
    print("area is - ", res)

