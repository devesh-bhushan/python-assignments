"""
this is the program to to give you
random mathematical problem to solve
"""
import random
score = 0
total = 0
ch = 1
while ch == 1:
    print("""
    welcome to the problem giver
    Press 1: for easy level problem
    Press 2: FOr medium level problem
    Press 3 : For hard level problem
        """)
    choice = int(input("please enter your choice"))
    if choice == 1:
        for i in range(5):
            j = random.randint(1, 100)
            k = random.randint(1, 100)
            lst = ["+", "-", "//", "*"]
            random.shuffle(lst)
            pro = str(j) + lst[0] + str(k)
            print(pro, " = ?")
            ans = int(input("enter the answer"))
            if ans == eval(pro):
                score += 1
                total += 1
            else:
                total += 1
        print("your result is {} out of {}".format(score, total))
    elif choice == 2:
        for i in range(5):
            j = random.randint(100, 1000)
            k = random.randint(100, 1000)
            lst = ["+", "-", "//", "*"]
            random.shuffle(lst)
            pro = str(j) + lst[0] + str(k)
            print(pro, " = ?")
            ans = int(input("enter the answer"))
            if ans == eval(pro):
                score += 1
                total += 1
            else:
                total += 1
        print("your result is {} out of {}".format(score, total))
    elif choice == 3:
        for i in range(5):
            j = random.randint(100, 1000)
            k = random.randint(100, 1000)
            l = random.randint(100, 1000)
            lst = ["+", "-", "//", "*"]
            random.shuffle(lst)
            pro = str(j) + lst[0] + str(k) + lst[1] + str(l)
            print(pro, " = ?")
            ans = int(input("enter the answer"))
            if ans == eval(pro):
                score += 1
                total += 1
            else:
                total += 1
        print("your result is {} out of {}".format(score, total))

    else:
        print("Invalid choice")
    ch = int(input("do you want to continue press 1 to yes and 0 to no"))
