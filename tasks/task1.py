"""
this a menu driven  python program to add ,display
search ,delete ,update a employee management system
"""
ch = 1
lst = list([])
while ch == 1:
    print("""
    welcome to the portal
    Press 1: insert record
    Press 2: Display record
    Press 3 : delete record 
    Press 4: Update record
    Press 5: Search record """)
    choice = int(input("please enter your choice"))
    if choice == 1:
        for i in range(2):
            suls = list([])
            for j in range(2):
                data = eval(input("Enter The Employee ID and Name"))
                suls.append(data)
            lst.append(suls)
    elif choice == 2:
        for i in lst:
            print("Name and Employee ID of Employee Entered are", i)
    elif choice == 3:
        delval = int(input("enter the Employee id whose record to be deleted"))
        for i in lst:
            for j in i:
                if delval == j:
                    ind = lst.index(i)
                    del lst[ind]
                    break
    elif choice == 4:
        up = list([])
        update = int(input("enter the Employee id whose record to be updated"))
        for i in range(2):
            data = eval(input("enter the new employee ID and Name"))
            up.append(data)
        for i in lst:
            for j in i:
                if update == j:
                    ind = lst.index(i)
                    lst.insert(ind, up)
                    del lst[ind + 1]
                    break
    elif choice == 5:
        search = int(input("enter the Employee id whose record to be searched"))
        for i in lst:
            for j in i:
                if search == j:
                    ind = lst.index(i)
                    print("Employee ", lst[ind], f"found at {ind} index")
                    break
        else:
            print("Employee not found")
    else:
        print("Invalid choice")
    ch = int(input("do you want to continue press 1 to yes and 0 to no"))
