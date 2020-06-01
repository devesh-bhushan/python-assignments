"""
program to print the RIGHT ANGLE TRIANGLE
"""
for i in range(8):
    for k in range(8-(i+1)):
        print(" ", end="")
    for j in range(i):
        print("*", end="")

    print(end="\n")
