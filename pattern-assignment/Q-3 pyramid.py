"""
program to print the pyramid

"""
row = int(input("enter the number of rows in a pyramid"))
for i in range(row + 1):
    for k in range(row - (i)):
        print(" ", end="")
    for j in range(i):
        print("* ", end="")
    print(end="\n")


