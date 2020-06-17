"""
this a menu driven  python program to add ,display
search ,delete ,update a employee management system using file handling
"""


def insert(n):                             # function to insert record
    for j in range(n):
        lst = ["EmployeeId", "firstName", "lastName", "email", "phone no",
               "hire_date", "commission_Pct", "Manager_Id", "Department_ID"]
        fp = open("emp.txt", "a+")
        res = []
        for i in lst:
            data = str(input("enter the " + i))
            res.append(data)
        ru = ",".join(res)
        ru = ru + "\n"
        fp.write(ru)
        fp.close()


def display():                                 # function to display record
    fp = open("emp.txt", "r")
    for i in fp.readlines():
        print(i)
        fp.close()


def delete(e):                                    # function to delete record
    ctr = search(e)
    if ctr == 1:
        fp = open("emp.txt", "r")
        fp.seek(0)
        output = []
        for line in fp:
            if e not in line:
                output.append(line)
        fp.close()
        fp = open("emp.txt", 'w+')
        fp.writelines(output)
        fp.close()
        print("employee id successfully deleted")
    else:
        print("no such employee exists")


def search(e):                                     # function to delete record
    fp = open("emp.txt", "r")
    track = 0
    for line in fp:
        if e in line[0:5]:
            print(line)
            track += 1
    return track


ch = 1
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
        num = int(input("enter the number of employees you want to add"))
        insert(num)

    elif choice == 2:
        display()

    elif choice == 3:
        eid = str(input("enter the emp id to be deleted"))
        delete(eid)

    elif choice == 4:
        emp = str(input("enter the employee id to be updated"))
        count = search(emp)
        if count == 1:
            delete(emp)
            print("enter the new details")
            insert(1)
        else:
            print("no such employee id exits")

    elif choice == 5:
        eid = str(input("enter the employee id to be searched"))
        count = search(eid)
        if count == 1:
            print("employee id found")
        else:
            print("employee id not found")

    else:
        print("Invalid choice")

    ch = int(input("""   \n     Do You Want To Continue
                                   Press 1: To Main Menu
                                   Press 2: To Exit"""))
