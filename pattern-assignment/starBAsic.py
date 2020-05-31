"""
program to print the star pattern
"""
for i in range(5):
    for j in range(i):
        print("*", sep=" ", end=" ")

    print(end="\n")
