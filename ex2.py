import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

df = pd.read_csv("train.csv")
df.drop(columns=['targetName'])

"""
ex2_a
"""	
def drawing_first_rocket_track():
    """
    draw the first rocket.
    """
    plt.plot(df.iloc[0, 2:-2:7], df.iloc[0, 4:-2:7])
    plt.show()

"""
ex2_b
"""	
def drawing_rocket_tracks():
    """
    draw the 50 first rockets of type 1 or 16.
    """
    colors = ["red", "green"]
    print(df.groupby("class").size())
    for index in range(50):
        x = []
        z = []
        i = 0
        while True:
            try:
                val_x = df._get_value(index, 'posX_{}'.format(i))
                x.append(val_x)
                val_z = df._get_value(index, 'posZ_{}'.format(i))
                z.append(val_z)
                i += 1
            except:
                break
        if df._get_value(index, 'class') == 1:
            color = colors[0]
            plt.plot(x, z, color=color)
        if df._get_value(index, 'class') == 16:
            color = colors[1]
            plt.plot(x, z, color=color)

    plt.show()
    
    
	
"""
ex2_c
"""	
def drawing_15_sec_long_rocket_tracks():
    """
    draw the 50 first rockets of type 1 or 16 , only if the time more then 15 sec.
    """
    rockets = df[((df["class"] == 16) | (df["class"] == 1)) & (df["Time_29"] == 14.5)].iloc[:50, :]
    print(rockets.iloc[1, :])
    for i in range(50):
        color = "red" if rockets.iloc[i, -1] == 1 else "green"
        plt.plot(rockets.iloc[i, 2:-2:7], rockets.iloc[i, 4:-2:7], color=color)
    plt.show()

"""
Do ex2_c on another types of rockets.
"""	
def test_func():
    """
    Draw the 50 first rockets of type 1,4,7 or 10 , only if the time more then 15 sec.
    """
    colors = ["red", "green", "blue", "black"]
    print(df.groupby("class").size())
    for index in range(5000):
        x = []
        z = []
        i = 0
        while True:
            try:
                val_x = df._get_value(index, 'posX_{}'.format(i))
                if pd.isnull(df.iloc[index, 107]) == False:
                    x.append(val_x)
                val_z = df._get_value(index, 'posZ_{}'.format(i))
                if pd.isnull(df.iloc[index, 107]) == False:
                    z.append(val_z)
                i += 1
            except:
                break
        if df._get_value(index, 'class') == 1:
            color = colors[0]
            plt.plot(x, z, color=color)
        if df._get_value(index, 'class') == 4:
            color = colors[1]
            plt.plot(x, z, color=color)
        if df._get_value(index, 'class') == 7:
            color = colors[2]
            plt.plot(x, z, color=color)
        if df._get_value(index, 'class') == 10:
            color = colors[3]
            plt.plot(x, z, color=color)

    plt.show()


	
"""
ex2_d
"""
def drawing_rocket_tracks_4():
    """
    draw the 50 first rockets of type 1 or 16 , only if the time more then 15 sec and they both up and down.
    """
    rockets = df[((df["class"] == 16) | (df["class"] == 1)) & (df["Time_29"] == 14.5)].iloc[:50, :]
    for i in range(50):
        up = False
        down = False
        for j in range(7, 213, 7):
            if rockets.iloc[i, j] > 0:
                up = True
            elif rockets.iloc[i, j] < 0:
                down = True
            if up and down:
                color = "red" if rockets.iloc[i, -1] == 1 else "green"
                plt.plot(rockets.iloc[i, 2:-2:7], rockets.iloc[i, 4:-2:7], color=color)
                break
        if not up or not down:
            print(rockets.iloc[i, 0])

    plt.show()

"""

"""
def test_func_drawing_energy():
    """
    Drawing energy of 3 and 9 class rockets.
    rockets = df[((df["class"] == 3) | (df["class"] == 9))][:100]
    for index, row in rockets.iterrows():
        x = []
        y = []
        for j in range(0, 207, 7):
            x.append(j)
            y.append(calculate_energy(row[j + 5], row[j + 4]))
        color = "red" if row[-1] == 3 else "green"
        plt.plot(x, y, color=color)
    plt.show()

