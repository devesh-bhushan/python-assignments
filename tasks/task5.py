"""
this a menu driven  python program to add ,display
search ,delete ,update a employee management system storing data in a database
"""

import pymysql


def create():                       # function to create the table
    cur = obj.cursor()
    qry = """create table  if not exists employees(
                                    emp_id int primary key,
                                    emp_name varchar(20),
                                    email varchar(30),
                                    contact varchar(10),
                                    salary int,
                                    hire_date date,
                                    address varchar(50))
    """
    cur.execute(qry)
    cur.close()


def insert(n):                        # function to insert record
    cur = obj.cursor()
    for j in range(n):
        lst = ["emp_id", "emp_name", "email", "contact", "salary", "hire_date", "address"]
        val = []
        for i in lst:
            v = input("enter the "+i)
            val.append(v)
        qry = "insert into employees values({},'{}','{}','{}',{},'{}','{}')".format(*val)
        cur.execute(qry)
        obj.commit()
    cur.close()


def display():                            # function to display record
    cur = obj.cursor()
    qry = "select* from employees"
    cur.execute(qry)
    res = cur.fetchall()
    print("employee_id\temployee_name\temail\tcontact\tsalary\thiredate\taddress".expandtabs(5))
    for row in res:
        for j in row:
            print(j, end="   ")
        print()
    cur.close()


def delete(e_id):                            # function to delete record
    cur = obj.cursor()
    co = search(e_id)
    if co == 1:
        qry = "delete from employees where emp_id = %s"
        cur.execute(qry, (e_id,))
        obj.commit()
        print("record successfully deleted")
    else:
        print("no such employee record found")
    cur.close()


def update():                                 # function to update record
    cur = obj.cursor()
    emp = input("enter the employee id to be updated")
    co = search(emp)
    if co == 0:
        print("no such record found ")
    else:
        name = input("enter the new name")
        emai = input("enter the new email")
        con = input("enter the contact")
        sal = input("enter the new salary")
        date = input("enter the hire date in yy-mm-dd format")
        add = input("enter the address")
        qry = f"""update employees 
                            set emp_name = %s,email = %s,contact = %s, salary = %s, hire_date = %s, address = %s
                            where emp_id = %s"""
        cur.execute(qry, (name, emai, con, sal, date, add, emp))
        obj.commit()
        print("record successfully updated")
    cur.close()


def search(e_id):                                   # function to search record
    cur = obj.cursor()
    qry = "select * from employees where emp_id = %s"
    cur.execute(qry, (e_id,))
    res = cur.fetchall()
    counter = 0
    for row in res:
        for j in row:
            print(j, end="  ")
        print()
        counter = 1
    cur.close()
    return counter


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
    obj = pymysql.connect("localhost", "root", "", "ems")

    if choice == 1:
        num = int(input("enter the number of employees you want to add"))
        insert(num)
        obj.close()

    elif choice == 2:
        display()
        obj.close()

    elif choice == 3:
        eid = input("enter eid to be deleted")
        delete(eid)
        obj.close()

    elif choice == 4:
        update()
        obj.close()

    elif choice == 5:
        eid = input("enter the employee id to be searched")
        flag = search(eid)
        if flag == 1:
            print("employee record exists")
        else:
            print("employee record does not exists")
        obj.close()

    else:
        print("Invalid choice")
    ch = int(input("""   \n     Do You Want To Continue
                                   Press 1: To Main Menu
                                   Press 2: To Exit"""))
