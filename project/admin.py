"""
this is the admin module
"""
import qry
import mainpage as mp


def adminmenu(username):
    print(f"                Welcome {username}")
    con = 1
    while con == 1:
        print("""                              
                            Press 1: To Create User Account
                                      a)Monitor  b)Admin
                            Press 2: To View All Users(Employees)
                            Press 3: To View All Prospects
                            Press 4: To Change Password
                                      a)Self     b)Others
                            Press 5: To Search Prospect
                                      a)By Priority    b)Prospect Id
                            Press 6: To Activiate / Deacticate Account 
                            Press 7 : To add New Carmodal
                            Press 8: To Signout """)

        choice = int(input("Please enter your choice :-"))

        if choice == 1:
            input("Press any key to continue :-")
            opt = int(input("""                             
                               Press 1: To create user account :-
                               Press 2: To create a admin account :-"""))
            if opt == 1:
                dsgn = "monitor"
                qry.createuseracc(dsgn)
            elif opt == 2:
                dsgn = "admin"
                qry.createuseracc(dsgn)
            else:
                print("Invalid option")

        elif choice == 2:
            qry.viewuser()
            input("Press any key to continue :-")

        elif choice == 3:
            qry.viewprospect()
            input("Press any key to continue :-")

        elif choice == 4:
            opt = int(input("""                           
                               Press 1: To Change Own Account Password :-
                               Press 2: To Change Other Account Password :-"""))
            if opt == 1:
                qry.changepass(username)
            elif opt == 2:
                usrnme = input("enter the Username whose password to be changed :-")
                qry.changepass(usrnme)
            else:
                print("Invalid Option")
            input("Press any key to continue :-")
            pass

        elif choice == 5:
            qry.searchprospect()
            input("Press any key to continue :-")

        elif choice == 6:
            opt = int(input("""
                    Press 1 : To activate account :- 
                    Press 2 : To deactivate account :-"""))
            usrnme = input("Enter the user name whose status is to be changed :-")
            if opt == 1:
                stat = "activated"
                qry.accountupdate(usrnme, stat)
            elif opt == 2:
                stat = "deactivated"
                qry.accountupdate(usrnme, stat)
            else:
                print("Invalid option")
            input("Press any key to continue :-")
            pass

        elif choice == 7:
            qry .addmodal()

        elif choice == 8:
            mp.main()

        else:
            print("Invalid choice")
            input("Press any key to continue :-")

        con = int(input(""" 
                            Press 1: To Continue in Admin Menu :-
                            Press 2: To Exit from Admin Menu :-\n"""))


if __name__ == "__main__":
    adminmenu("E001")
