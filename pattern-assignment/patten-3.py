"""
program to print pattern number
"""
for i in range(5):
    k = 0
    for j in range(i):
        print(j * k, sep=" ", end=" ")
        k += 1
    print(end="\n")






