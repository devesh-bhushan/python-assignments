"""
program to print the pyramid

"""
row = int(input("enter the number of rows in a pyramid"))
for i in range(row):
    for k in range(i):
        print(" ", end="")
    for j in range(row - (i+1)):
        print("* ", end="")
    print(end="\n")


