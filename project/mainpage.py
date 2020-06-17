"""
first or entry point of the program
"""
import qry
import pymysql as py


def main():
    con = 1
    while con == 1:
        print("""*************** Welcome to Prospect Encore Analysis ***************""")
        st = "Do You want to login"
        choice = input(st + "(yes/no) :-")
        if choice in ["y", "Y", "yes", "YES", "Yes"]:
            qry.login()
        elif choice in ["n", "N", "no", "NO", "No"]:
            exit(0)
        else:
            print("Invalid choice")
        con = int(input("""
                         Press 1: To Main Menu :-
                         Press 2: To Exit :-"""))


if __name__ == "__main__":
    obj = py.connect("localhost", "root", "", "pencore")
    main()
    obj.close()