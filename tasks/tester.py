"""
lst = list([])


for i in range(2):
    suls = list([])
    for j in range(2):
        data = eval(input("Enter The Employee ID and Name"))
        suls.append(data)
    lst.append(suls)

size=0
lst1 = []
lst =["james","anna","king","smith","kimberlee"]
for i in lst:
    size = len(i)
    lst1.append(size)
print(lst1)
import area
area.triangle(2,2)
area.circle(34)
area.cube(32)
area.cylinder(34,56)
import strutility as st
st.concat("devesf","bhushan")
st.length("devesf","bhushan")
st.upperlowerpro("devesf","bhushan")




import packages
import packages.mdiv as md
md.division(12,8)
"""

while True:
    try:
        fp = open("C:\\Python38\\prog\\msg.txt", 'a')
        num1 = int(input("enter the first number "))
        num2 = int(input("enter the second number "))
        res = num1//num2
        fp.write(f"{num1}//{num2} = {res}" + "\n")
    except ZeroDivisionError as ob:
        fp.write(str(ob) + "\n")
    except ValueError as ob1:
        fp.write(str(ob1) + "\n")
    else:
        break
    finally:
        fp.close()
print("values stored in the file are")
fp = open("C:\\Python38\\prog\\msg.txt", 'r')
for i in fp:
    print(i, end="\n")
fp.close()

