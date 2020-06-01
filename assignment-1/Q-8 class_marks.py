"""
program to calculate average marks and pecentage

"""
sub_1 = eval(input("enter the marks obtained in subject 1"))
sub_2 = eval(input("enter the marks obtained in subject 2"))
sub_3 = eval(input("enter the marks obtained in subject 3"))
sub_4 = eval(input("enter the marks obtained in subject 4"))
sub_5 = eval(input("enter the marks obtained in subject 5"))
totMks = sub_1+sub_2+sub_3+sub_4+sub_5
avg = totMks/5                              # calculating the average of marks
per = totMks/5                             # calculating the percentage
print("total marks are", totMks)
print("average of marks is", avg)
print("percentage of marks is", per)