"""
program to print the star pattern
"""
for i in range(8):
    for k in range(i):
        print(" ", end="")
    for j in range(8-(i+1)):
        print("*", end="")
    print(end="\n")