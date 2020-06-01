"""
program to print the star pattern
"""
row = int(input("enter the number of rows in a TRIANGLE"))
for i in range(row+1):
    for j in range(i):
        print("*", sep=" ", end=" ")

    print(end="\n")
