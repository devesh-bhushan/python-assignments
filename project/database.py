"""
this is the file which contains all database information
"""
import pymysql


def create_emplo():                        # function to create the table
    cur = obj.cursor()
    qry = """create table employee(
                                     userName varchar(45) primary key,
                                     userPass varchar(20),
                                     userType varchar(10),
                                     fullName varchar(50),
                                     gender varchar(1),
                                     phone varchar(10),
                                     email varchar(50),
                                     status varchar(12)
                                     ) engine = Innodb;
     """
    cur.execute(qry)
    cur.close()


def create_custo():
    cur = obj.cursor()
    qry = """create table prospect(
                                     prospId int 		primary key auto_increment,
                                     prospName varchar(45),
                                     prospPhone	varchar(45),
                                     prospAddress varchar(45),
                                     modelName varchar(45),
                                     interestedColor varchar(45),
                                     dateOfVisit varchar(20),
                                     dayOfVisit varchar(10),
                                     bookingAmount decimal(8,2),
                                     gender varchar(1),
                                     incomeGroup varchar(1),
                                     priority varchar(45),
                                     purchaseMode varchar(20),
                                    foreign key(modelName) references carModels(modelName)
                                      )engine = Innodb;

    """
    cur.execute(qry)
    cur.close()


def create_carmod():                          # function to create the table
    cur = obj.cursor()
    qry = """create table carModels(
                                     modelid varchar(45) ,
                                     modelName varchar(45),
                                     price decimal(10,2),
                                     primary key(modelName, modelid)
                                    )engine = Innodb;
            """
    cur.execute(qry)
    cur.close()


def create_carsale():                       # function to create the table carsale
    cur = obj.cursor()
    qry = """create table carsale(
                                prospId int(11),
                                regid varchar(20),
                                saledate date,
                                price decimal(12,2),
                                feedback varchar(20),
                                primary key(regid),
                                foreign key(prospId) references prospect(prospId)
                                )engine = Innodb;
            """
    cur.execute(qry)
    cur.close()


if __name__ == "__main__":
    obj = pymysql.connect("localhost", "root", "", "pencore")

    create_custo()
    create_carsale()
