"""
this is the monitor qry module
"""
import pymysql

obj = pymysql.connect("localhost", "root", "", "pencore")


def createprospacc():                                   # function to add p new rospect
    cur = obj.cursor()
    try:
        prospid = 0
        prospnme = input("Enter the Prospect Name :-")
        prospphone = input("enter the Prospect contact number :-")
        prospadd = input("Enter the Prospect Address :-")
        inmod = input("Enter the Model interested in :-")
        incol = input("Enter the Model Color :-")
        dov = input("Enter the Date of Visit In Format yy-mm-dd :-")
        dayvisit = input("Enter the Day of Visit :-")
        ba = int(input("Enter the Booking Amount :-"))
        gen = input("Enter the Gender as :m for Male / f for Female :-")
        ig = input("Enter the Income Group as : l for Low / m For Medium / h For High :-")
        prior = input("Enter the Priority as : low / medium / high :-")
        purmod = input("Enter the Purchase Mode :-")
        qry = """insert into prospect
                  values( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
             """
        cur.execute(qry, (prospid, prospnme, prospphone, prospadd, inmod, incol, dov,
                          dayvisit, ba, gen, ig, prior, purmod))
        obj.commit()
        cur.close()
    except pymysql.err.IntegrityError as ob:
        print(ob)


def updateprosp(prospid):                                     # function to update the prospect account
    cur = obj.cursor()
    phone = input("enter the New prospect's contact number :-")
    im = input("Enter the New Interested Model in :-")
    ic = input("Enter the New Interested Color in :-")
    pri = input("Enter the Priority :-")
    qry = """update prospect
             set prospPhone = %s,interestedModel = %s, interestedColor = %s,priority = %s where prospId = %s
             """
    cur.execute(qry, (phone, im, ic, pri, prospid))
    obj.commit()
    cur.close()


def insertdetail():                                  # function to insert the  sold car details
    cur = obj.cursor()
    try:
        proid = int(input('Enter the Prospect id :-'))
        regid = input("Enter the Registration id :-")
        sd = input("Enter the Sale Date in yy-mm-dd format :-")
        modelid = input("enter the Model Name")
        qry = """insert into carsale
                 values(%s, %s, %s, %s)"""
        cur.execute(qry, (proid, regid, sd, modelid))
        obj.commit()
        cur.close()
    except pymysql.err.IntegrityError as ob:
        print(ob)


def viewmodel():                                             # function to view available car model
    cur = obj.cursor()
    qry = "select * from carModels"
    cur.execute(qry)
    res = cur.fetchall()
    print("Model Id        Model Name         Price")
    if cur.rowcount > 0:
        for row in res:
            for element in row:
                print(element, end="               ")
            print()
    else:
        print("No Model Inserted in database")
    cur.close()


if __name__ == "__main__":
    createprospacc()
