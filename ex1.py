import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math


"""
ex1_a
"""
df = pd.read_csv("train.csv")
df.drop(columns=['targetName'])


"""
ex1_b
"""
def get_rout_num():
    print(df.groupby("class").size())


"""
ex1_c
"""
def histogram_view():
    len_per_class = {}
    for i in range(len(df)):
        x1 = 0
        y1 = 0
        z1 = df.loc[i, 'posZ_0']
        x2 = df.iloc[i, 205 - (np.count_nonzero(df.loc[i].isnull()))]
        y2 = df.iloc[i, 206 - (np.count_nonzero(df.loc[i].isnull()))]
        z2 = df.iloc[i, 207 - (np.count_nonzero(df.loc[i].isnull()))]
        distance = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) + (z1 - z2) * (z1 - z2))
        cls = (df.loc[i, 'class'])
        if cls not in len_per_class.keys():
            len_per_class[cls] = [distance]
        else:
            len_per_class[cls].append(distance)
    for key, value in len_per_class.items():
        plt.hist(value, bins=100)
        plt.show()
    return
