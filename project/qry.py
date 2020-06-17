"""
this is the admin qry module
"""
import pymysql
import admin
import monitor
import mainpage as mp

obj = pymysql.connect("localhost", "root", "", "pencore")


def login():  # function for login
    cur = obj.cursor()
    username = input("enter the username")
    password = input("enter the password")
    qry = f"""select usertype,fullname
             from employee
             where userName='{username}' and userPass ='{password}' and status='activated'"""
    cur.execute(qry)
    res = cur.fetchall()
    if cur.rowcount == 1:
        if res[0][0] == "admin":
            admin.adminmenu(username)

        elif res[0][0] == "monitor":
            monitor.monitormenu(username)

    else:
        print("invalid username or password")
        return mp.main()


def createuseracc(dsgn):  # function to create employee or admin account
    cur = obj.cursor()
    usrnme = input("enter the UserNAme of the employee")
    usrpass = input("Enter the user password of employee")
    usrtype = dsgn
    name = input("enter the employee name")
    gndr = input("enter the employee gender as : m or f ")
    pho = input("enter the contact number of employee ")
    emal = input("enter the email address of the employee")
    status = input("enter the status of employee as : activated or deactivated")
    qry = """insert into employee
             values( %s, %s, %s, %s, %s, %s, %s, %s)
          """
    cur.execute(qry, (usrnme, usrpass, usrtype, name, gndr, pho, emal, status))
    obj.commit()
    cur.close()


def viewuser():                                              # function to view all employees
    cur = obj.cursor()
    print("userName   userPass      userType   fullName     gender       phone            email                 status")
    qry = "select * from employee"
    cur.execute(qry)
    res = cur.fetchall()
    if cur.rowcount > 0:
        for row in res:
            for element in row:
                print(element, end="       ")
            print()
    else:
        print("no Record inserted in the database")
    cur.close()


def viewprospect():                              # function to view all prospect
    cur = obj.cursor()
    print("ProspId ProspName  ProspPhone ProspAddress InterestedModel InterestedColor DateOfVisit DayOfVisit  "
          "BookingAmount Gender IncomeGroup Priority PurchaseMode")
    qry = "select * from prospect"
    cur.execute(qry)
    res = cur.fetchall()
    if cur.rowcount > 0:
        for row in res:
            for element in row:
                print(element, end="   ")
            print()
    else:
        print("no Record inserted in the database")
    cur.close()


def changepass(usrnme):                              # function to change password of user account
    cur = obj.cursor()
    flag = search(usrnme)
    if flag == 1:
        passwd = input("enter the new password")
        qry = """update employee
                 set userPass = %s where userName = %s"""
        cur.execute(qry, (passwd, usrnme))
        print("Password successfully Updated")
        obj.commit()
        cur.close()
    else:
        print("No such Employee Exists In Database")


def searchprospect():                      # function to search prospect record by priority or prospect id
    cur = obj.cursor()
    opt = int(input("""                          Press 1: To Search Prospect by Priority
                        Press 2:  To Search Prospect by Prospect Id"""))
    if opt == 1:
        tpe = input("Enter the Prospect Priority as : low  medium high")
        qry = """select * from prospect
                      where priority = %s"""
        cur.execute(qry, (tpe,))
    elif opt == 2:
        tpe = int(input("Enter THe Prospect Id"))
        qry = """select * from prospect
                              where prospId= %s"""
        cur.execute(qry, (tpe,))
    else:
        print("Invalid Option")
    print("ProspId ProspName  ProspPhone ProspAddress InterestedModel InterestedColor DateOfVisit DayOfVisit "
          " BookingAmount Gender IncomeGroup Priority PurchaseMode")
    res = cur.fetchall()
    if cur.rowcount > 0:
        for row in res:
            for element in row:
                print(element, end="   ")
            print()
    else:
        print("no Record inserted in the database")
    cur.close()


def accountupdate(usrnme, stat):                                     # function to activate or deactivate record
    cur = obj.cursor()
    flag = search(usrnme)
    if flag == 1:
        qry = f"""update employee
                   set status = '{stat}' where userName = '{usrnme}'"""
        cur.execute(qry)
        obj.commit()
        cur.close()
    else:
        print("No Such Username Exists in Database")


def search(usrnme):  # function to search record
    cur = obj.cursor()
    qry = "select * from employee where userName = %s"
    cur.execute(qry, (usrnme,))
    counter = 0
    if cur.rowcount > 0:
        counter = 1
    cur.close()
    return counter


def addmodal():
    cur = obj.cursor()
    modid = input("Enter the model id")
    modnme = input("Enter the model name")
    pric = int(input("enter the model price"))
    qry = """insert into carModels
             values(%s,%s,%s )"""
    cur.execute(qry, (modid, modnme, pric))
    obj.commit()
    cur.close()


if __name__ == "__main__":
    addmodal()
