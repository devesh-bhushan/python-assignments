"""
program to calculate the DA and HRA of employee
"""
sal = eval(input("enter the salary of employee"))

if sal <= 2000:
    da = (10*sal)/100
    hra = (20*sal)/100
elif (sal > 2000) and (sal <= 5000):
    da = (20*sal)/100
    hra = (30*sal)/100
elif (sal > 5000) and (sal <= 10000):
    da = (30*sal)/100
    hra = (40*sal)/100
else:
    da = (50*sal)/100
    hra = (50*sal)/100

print("DA of employee is", da, "HRA of employee is", hra, sep="\n")