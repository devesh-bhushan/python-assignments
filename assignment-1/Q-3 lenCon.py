"""
program to convert the length into meter anf kilometer

"""
len = eval(input("enter the length in centimeter"))
len_me = len/100        # length to meter
len_km = len/(10**5)    # length to kilometer
print("length in meter is", len_me)
print("length in kilometer is", len_km)
