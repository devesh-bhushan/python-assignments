"""
program to print pattern number
"""
k = 1
for i in range(5):
    for j in range(i):
        print(k, sep=" ", end=" ")
        k += 1
    print(end="\n")






