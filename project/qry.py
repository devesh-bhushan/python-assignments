"""
this is the admin qry module
"""
import pymysql
import admin
import monitor
import mainpage as mp
import pandas as pd

obj = pymysql.connect("localhost", "root", "", "pencore")


def login():                                                         # function for login
    cur = obj.cursor()
    username = input("Enter the Username :-")
    password = input("Enter the Password :-")
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
        print("Invalid Username or Password")
        return mp.main()


def createuseracc(dsgn):                                       # function to create employee or admin account
    cur = obj.cursor()
    usrnme = input("Enter the UserName of the Employee :-")
    usrpass = input("Enter the User Password of Employee :-")
    usrtype = dsgn
    name = input("Enter the Employee Name :-")
    gndr = input("Enter the Employee Gender as : m or f :-")
    pho = input("Enter the Contact Number of Employee :-")
    emal = input("Enter the Email Address of the Employee :-")
    status = input("Enter the Status of Employee as : activated or deactivated :-")
    qry = """insert into employee
             values( %s, %s, %s, %s, %s, %s, %s, %s)
          """
    cur.execute(qry, (usrnme, usrpass, usrtype, name, gndr, pho, emal, status))
    obj.commit()
    cur.close()


def viewusr():                                      # function to view all employees
    obj = pymysql.connect("localhost", "root", "", "pencore")
    pd.set_option("display.max_row", 1000)
    pd.set_option("display.max_column", 1000)
    pd.set_option("display.max_colwidth", 1000)
    pd.set_option("display.width", 1000)
    emp = pd.read_sql_query("select* from employee", obj)
    print(emp)
    obj.close()


def changepass(usrnme):                            # function to change password of user account
    cur = obj.cursor()
    flag = search(usrnme)
    if flag == 1:
        passwd = input("Enter the new password :-")
        qry = """update employee
                 set userPass = %s where userName = %s"""
        cur.execute(qry, (passwd, usrnme))
        print("Password Successfully Updated")
        obj.commit()
        cur.close()
    else:
        print("No such Employee Exists In Database")


def searchprospect():                           # function to search prospect record by priority or prospect id
    obj = pymysql.connect("localhost", "root", "", "pencore")
    pd.set_option("display.max_row", 1000)
    pd.set_option("display.max_column", 1000)
    pd.set_option("display.max_colwidth", 1000)
    pd.set_option("display.width", 1000)
    opt = int(input("""                         
                        Press 1: To Search Prospect by Priority
                        Press 2:  To Search Prospect by Prospect Id"""))
    if opt == 1:
        tpe = input("Enter the Prospect Priority as : low  medium high")
        prosp = pd.read_sql_query("select* from prospect", obj)
        print(prosp[prosp.priority == tpe])
    elif opt == 2:
        tpe = int(input("Enter THe Prospect Id :-"))
        prosp = pd.read_sql_query("select* from prospect", obj)
        print(prosp[prosp.prospId == tpe])
    obj.close()


def accountupdate(usrnme, stat):                         # function to activate or deactivate record
    cur = obj.cursor()
    flag = search(usrnme)
    if flag == 1:
        qry = f"""update employee
                   set status = %s where userName = %s"""
        cur.execute(qry, (stat, usrnme))
        obj.commit()
        print("Changes Successfully Uploaded to Database")
    else:
        print("No Such Username Exists in Database")
    cur.close()


def search(usrnme):                                       # function to search record
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
    modid = input("Enter the Model Id:-")
    modnme = input("Enter the Model Name:-")
    pric = int(input("Enter the Model Price:-"))
    qry = """insert into carModels
             values(%s,%s,%s )"""
    cur.execute(qry, (modid, modnme, pric))
    obj.commit()
    cur.close()


def viewprosp():                                     # function to view all prospect
    obj = pymysql.connect("localhost", "root", "", "pencore")
    pd.set_option("display.max_row", 1000)
    pd.set_option("display.max_column", 1000)
    pd.set_option("display.max_colwidth", 1000)
    pd.set_option("display.width", 1000)
    prosp = pd.read_sql_query("select* from prospect", obj)
    print(prosp)
    obj.close()


if __name__ == "__main__":
    searchprospect()