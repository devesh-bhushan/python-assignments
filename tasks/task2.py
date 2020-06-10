"""
this is a menu driven ticket booking system
"""
dic = {}
for key in range(1, 51):
    dic[key] = key
ch = 1
while ch == 1:
    print("""
    **********************               Welcome To The Ticket Centre          **********************
                          Press : 1 To See Available Seats
                          Press 2 : To Book Seats
                          Press 3 : To Cancel Seat""")
    choice = int(input("Please Enter Your Choice"))
    if choice == 1:
        key = 1                                           # function to see available seats
        for i in range(5):
            for j in range(10):
                if key <= 10:                              # applied formatting
                    print(dic[key], end="                ")
                    key = key + 1
                elif dic[key] == "B":
                    print(dic[key], end="                ")
                    key = key + 1
                else:
                    print(dic[key], end="               ")
                    key = key + 1
            print()

    elif choice == 2:
        lst = []
        no_seat = int(input("enter the number of seats you want to book"))
        for i in range(no_seat):
            seat = int(input("Enter the seat number you want to book"))
            lst.append(seat)
        for i in lst:
            if (i <= 50) and (dic[i] != "B"):
                dic[i] = "B"                                                   # function to book seats
                print(f"Your Seat number-{i}- Has Been Booked")
            elif (i <= 50) and (dic[i] == "B"):
                print("seat already occupied")
            else:
                print("Invalid Seat Number")
    elif choice == 3:
        lst2 = []
        no_seatdel = int(input("Enter the number of seat you want to delete"))
        for i in range(no_seatdel):
            seatdel = int(input("Enter the seat number you want to delete book"))
            lst2.append(seatdel)
        for i in lst2:
            if (i <= 50) and (dic[i] == "B"):
                dic[i] = i                                                     # to delete seats
                print("Your Seat Has Been deleted")
            elif (i <= 50) and (dic[i] != "B"):
                print("seat is not initially booked")
            else:
                print("Invalid Seat Number")
    else:
        print("Invalid choice")
    print()
    ch = int(input("""                 Do You Want To Continue
                                Press 1: To Main Menu
                                Press 2: To Exit"""))