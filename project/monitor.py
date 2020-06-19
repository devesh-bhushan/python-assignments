"""
this is the monitor module
"""
import mainpage as mp
import mqry
import qry
import ploting as pl


def monitormenu(username):
    print(f"        Welcome {username}")
    con = 1
    while con == 1:
        print("""       
                        Press 1: To add new prospects
                        Press 2: To View All prospects
                        Press 3: Update prospects
                                 a) Phone b) Model c) Color d) Priority
                        Press 4: To Search Prospect
                                  a)By Priority    b)Prospect Id
                        Press 5: To Change own password
                        Press 6: To Insert car sale details
                        Press 7: TO See the Available Models
                        Press 8: For Data Visualization
                        Press 9: To Logout """)

        choice = int(input("Please enter your choice :-"))

        if choice == 1:
            mqry.createprospacc()
            input("Press any key to continue :-")

        elif choice == 2:
            qry.viewprosp()
            input("Press any key to continue :-")

        elif choice == 3:
            prospid = int(input("Enter the Prospect id :-"))
            mqry.updateprosp(prospid)
            input("Press any key to continue :-")

        elif choice == 4:
            qry.searchprospect()
            input("Press any key to continue :-")

        elif choice == 5:
            qry.changepass(username)
            input("Press any key to continue :-")

        elif choice == 6:
            mqry.insertdetail()
            input("Press any key to continue :-")

        elif choice == 7:
            mqry.viewmodel()

        elif choice == 8:
            pl.visualization()
            input("Press any key to continue :-")

        elif choice == 9:
            mp.main()
            input("Press any key to continue :-")

        else:
            print("Invalid choice made")
            input("Press any key to continue :-")

        con = int(input(""" 
                            Press 1: To continue in Monitor Menu 
                            Press 2: To exit from Monitor Menu\n"""))
