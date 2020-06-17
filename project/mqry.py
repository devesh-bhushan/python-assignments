"""
this is the monitor qry module
"""
import pymysql

obj = pymysql.connect("localhost", "root", "", "pencore")


def createprospacc():
    cur = obj.cursor()
    try:
        prospid = 0
        prospnme = input("Enter the Prospect Name :-")
        prospphone = input("enter the Prospect contact number :-")
        prospadd = input("Enter the Prospect Address :-")
        inmod = input("Enter the Model interested in :-")
        incol = input("Enter the Model Color :-")
        dov = input("Enter the date of visit :-")
        dayvisit = input("Enter the day of visit :-")
        ba = int(input("Enter the booking amount :-"))
        gen = input("Enter the gender as :m for Male / f for Female :-")
        ig = input("Enter the income group as : l for Low / m For Medium / h For High :-")
        prior = input("Enter the priority as : low / medium / high :-")
        purmod = input("Enter the purchase mode :-")
        qry = """insert into prospect
             values( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
             """
        cur.execute(qry, (prospid, prospnme, prospphone, prospadd, inmod, incol, dov,
                          dayvisit, ba, gen, ig, prior, purmod))
        obj.commit()
        cur.close()
    except pymysql.err.IntegrityError as ob:
        print(ob)


def updateprosp(prospid):
    cur = obj.cursor()
    phone = input("enter the new prospect contact number")
    im = input("Enter the new interested model")
    ic = input("Enter the new interested color")
    pri = input("Enter the priority")
    qry = """update prospect
             set prospPhone = %s,interestedModel = %s, interestedColor = %s,priority = %s where prospId = %s
             """
    cur.execute(qry, (phone, im, ic, pri, prospid))
    obj.commit()
    cur.close()


def insertdetail():
    cur = obj.cursor()
    try:
        proid = int(input('Enter the nprospect id'))
        regid = input("ENter the registration id")
        sd = input("Enter the sale date in yy-mm-dd format")
        price = input("Enter the car price")
        feedbck = input("Enter the Feedback from customer")
        qry = """insert into carsale
                  values(%s, %s, %s, %s, %s)"""
        cur.execute(qry, (proid, regid, sd, price, feedbck))
        obj.commit()
        cur.close()
    except pymysql.err.IntegrityError as ob:
        print(ob)


def viewmodel():
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
        print("No Model inserted in database")
    cur.close()

if __name__ == "__main__":
    createprospacc()
