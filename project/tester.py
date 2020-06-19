from matplotlib import pyplot as plt
import seaborn as sns
import statsmodels
import pandas as pd
import numpy as np

tips = sns.load_dataset('tips')
print(tips.tail(9))
print(tips.values)
print(tips.columns)
print(tips.describe())
sns.barplot(x="day", y="total_bill", data=tips)
