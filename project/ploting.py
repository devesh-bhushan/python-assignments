import saleanalysis
import numpy as np
from matplotlib import pyplot as plt
import random


def visualization():
    years, cars = saleanalysis.test()
    arr_cars = {}
    for k, v in cars.items():
        if k is not None:
            arr_cars[k] = np.array(v)
    years = np.array(years, dtype=int)
    print("""
                Press 1: To See Individual CarSale In Particular Year
                Press 2: To Check The Comparision Of Car For A Particular Year
                Press 3: To Check The Total Car Sale For A Given Year
                Press 4 : To Check The Percentage Of CarSale With Other Car In  All Previous Years""")
    choice = int(input("Enter the choice :-"))
    if choice == 2:
        count = 0
        na = {}
        for y in years:
            c = 0
            for i, j in cars.items():
                plt.bar(int(y) + c, j[count], label=i if i not in na else '', width=.05)
                na[i] = i
                c += .05
            count += 1
        plt.xticks(years)
        plt.xlabel("YEARS")
        plt.ylabel("UNITS SOLD")
        plt.legend()
        plt.show()

    elif choice == 1:
        c = 1
        for i in arr_cars.keys():
            plt.subplot(2, 3, c)
            for j in range(0, 1):
                colour = ["red", "green", "blue", "brown", "yellow"]
                random.shuffle(colour)
                plt.bar(years, arr_cars[i], label=i, width=.5, color=colour[0], edgecolor=colour[2])
                plt.xticks(years)
                plt.xlabel("YEARS")
                plt.ylabel("UNITS SOLD")
                plt.legend()
                c += 1
        plt.show()

    elif choice == 3:
        c = 1
        for i in arr_cars.keys():
            plt.bar(years, arr_cars[i], label=i, width=.5, bottom=c, edgecolor="black")
            c += arr_cars[i]
            plt.xticks(years)
            plt.xlabel("YEARS")
            plt.ylabel(" TOTAL UNITS SOLD")
            plt.legend()
        plt.show()

    elif choice == 4:
        nme = arr_cars.keys()
        no_cars = []
        for j in arr_cars.values():
            no_cars.append(sum(j))
        plt.subplot(1, 2, 1)
        plt.pie(no_cars, labels=nme, shadow=True, autopct="%3.2f%%")
        plt.subplot(1, 2, 2)
        plt.pie(no_cars, labels=nme, shadow=True,)
        plt.show()


if __name__ == "__main__":
    visualization()
