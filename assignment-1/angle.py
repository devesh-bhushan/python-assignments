"""
program to find the third angle of a triangle

"""
ang_1 = eval(input("enter the first angle of triangle"))
ang_2 = eval(input("enter the second angle of triangle"))
ang_3 = 180-(ang_1+ang_2)                                       # calaculating third angle
print("third angle of the triangle is", ang_3)