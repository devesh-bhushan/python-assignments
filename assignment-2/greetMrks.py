"""
program to greet according to the marks obtained by the student
"""
mk = eval(input("enter the marks obtained"))


def greeter(a):                                # function to greet student
    if 100 >= a >= 90:
        print("GRADE A")
    elif 90 > a >= 80:
        print("GRADE B")
    elif 80> a >= 70:
        print("GRADE C")
    elif 70 > a >= 60:
        print("GRADE D")
    else:
        print("better next time")


greeter(mk)                             # function calling