"""
program to convert days into week year and days

"""
ds = int(input("enter the days"))
wk = int(ds/7)
yrs = int(ds/365)
ds1 = int(ds%7)
print("the number of years_weeks and days are", yrs, "_", wk, "and", ds1)
