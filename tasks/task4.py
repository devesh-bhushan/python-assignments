"""
this a menu driven  python program to add ,display
search ,delete ,update a employee management system using file handling
"""


def insert(n):                             # function to insert record
    fp = open("emp.txt", "a+")
    for i in range(n):
        empid = str(input("enter the EmployeeId "))
        fn = str(input("enter the firstName "))
        ln = str(input("enter the lastName "))
        ema = str(input("enter the email "))
        pho = str(input("enter the phone "))
        hire_date = str(input("enter the hire_date "))
        jd = str(input("enter the job_id "))
        sal = str(input("enter the salary "))
        commi = str(input("enter the commission_Pct "))
        manag = str(input("enter the Manager_Id "))
        depart = str(input("enter the Department_ID "))
        st = ","
        st1 = ""
        st2 = "\n"
        fp.write(st1 + empid + st)
        fp.write(fn + st)
        fp.write(ln + st)
        fp.write(ema + st)
        fp.write(pho + st)
        fp.write(hire_date + st)
        fp.write(jd + st)
        fp.write(sal + st)
        fp.write(commi + st)
        fp.write(manag + st)
        fp.write(depart + st2)
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
