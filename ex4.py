import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

df = pd.read_csv("train.csv")
df.drop(columns=['targetName'])

def calculate_energy(height, velocity, mass=1, g=10):
    kinetic_energy = 0.5 * mass * velocity * velocity
    potential_energy = mass * g * height
    return kinetic_energy + potential_energy

"""
ex4_a on 1 and 16 class rockets.
"""
def ex4_1_16(rocket_index):
    cls16 = 100
    cls1 = 100
    """
    Calculate energy in time:0.
    """
    h_0 = df.loc[rocket_index, 'posZ_0']
    v_0 = df.loc[rocket_index, 'velX_0']
    energy_0 = calculate_energy(h_0,v_0)

    """
    Statistical Calculation of the chances for each type.
    Based on the results from ex2 and more actions.
    """
    if energy_0 < 215709:
        cls16 *= 0.01 / 600
    if energy_0 < 572998:
        cls16 *= 599 / 600
    if df.loc[rocket_index, 'velX_0'] < 200:
        cls16 *= 4 / 600
        cls1 *= 799 / 1300
    if df.loc[rocket_index, 'posZ_0'] < 790:
        cls16 *= 29 / 600
        cls1 *= 8 / 1300
    if df.loc[rocket_index, 'posZ_0'] > 3000:
        cls16 *= 558 / 600
        cls1 *= 768 / 1300
    if df.loc[rocket_index, 'posZ_0'] < 6000:
        cls16 *= 152 / 600
        cls1 *= 1217 / 1300
    if df.loc[rocket_index, 'velX_20'] > 300:
        cls16 *= 300 / 600
        cls1 *= 1 / 1300
    if df.loc[rocket_index, 'velX_20'] > 400:
        cls16 *= 234 / 600
        cls1 *= 0.01 / 1300
    if df.loc[rocket_index, 'posX_20'] > 4000:
        cls16 *= 239 / 600
        cls1 *= 0.01 / 1300

    if cls1 > cls16:
        return 1
    else:
        return 16


"""
ex4_a on 1,4,7,10 class rockets.
"""
def ex4_forth(rocket_index):
    cls10 = 100
    cls1 = 100
    cls7 = 100
    cls4 = 100
    """
    Statistical Calculation of the chances for each type.
    Based on the results from ex2 and more actions.
    """
    if df.loc[rocket_index, 'posZ_0'] > 7000:
        cls1 *= 0.01 / 1300
    if df.loc[rocket_index, 'posZ_0'] > 12000:
        cls1 *= 0.01 / 1300
        cls4 *= 0.01 / 1000
    if df.loc[rocket_index, 'posZ_0'] > 18500:
        cls1 *= 0.01 / 1300
        cls4 *= 0.01 / 1000
        cls7 *= 0.01 / 1000

    if cls1 >= max(cls7, cls4, cls10):
        return 1
    elif cls4 >= max(cls7, cls1, cls10):
        return 4
    elif cls7 >= max(cls4, cls1, cls10):
        return 7
    return 10


"""
ex4_a on 3 and 9 class rockets.
"""
def ex4_3_9(rocket_index, e_3, e_9):
    cls3 = 100
    cls9 = 100
    """
    Calculate energy in time:0.
    """
    h_0 = df.loc[rocket_index, 'posZ_0']
    v_0 = df.loc[rocket_index, 'velX_0']
    energy_0 = calculate_energy(h_0,v_0)
    
    if df.loc[rocket_index, 'class'] == 3:
        e_3.append(energy_0)
    if df.loc[rocket_index, 'class'] == 9:
        e_9.append(energy_0)
    """
    Statistical Calculation of the chances for each type.
    Based on the results from ex2 and more actions.
    """
    if energy_0 < 150000:
        cls3 *= 1129 / 1130
        cls9 *= 371 / 770
    if df.loc[rocket_index, 'velX_0'] < 200:
        cls3 *= 152 / 1130
        cls9 *= 3 / 770
    if df.loc[rocket_index, 'posZ_0'] < 4000:
        cls3 *= 400 / 1130
        cls9 *= 117 / 770
    if df.loc[rocket_index, 'posZ_0'] > 10000:
        cls3 *= 53 / 1130
        cls9 *= 226 / 770
    if df.loc[rocket_index, 'velX_20'] < 200:
        cls3 *= 765 / 1130
        cls9 *= 5 / 770
    if df.loc[rocket_index, 'velX_20'] > 350:
        cls3 *= 82 / 1130
        cls9 *= 143 / 770
    if df.loc[rocket_index, 'posX_20'] > 3500:
        cls3 *= 118 / 1130
        cls9 *= 160 / 770

    if cls3 > cls9:
        return 3
    else:
        return 9
    
    

"""
ex4_b on 1 and 16 class rockets.
"""
def checking_ML_1_16():
    """
    Create mutch data-trainning_set, test_set, vektor_test
    """
    real_df = df[df['class'].isin([1, 16])]
    tranning_set = real_df.iloc[:1900, :]
    test_set = real_df.iloc[1900:, :]
    vektor_test = test_set.iloc[:, -1]
    del test_set['class']
    """
    Checking result of the classify function-ex4_1_16.
    """
    confusion_matrix = [[0, 0], [0, 0]]
    y_pred = []
    for i in test_set.index:
        res = ex4_1_16(i)
        y_pred.append(res)
        if res == 1:
            if vektor_test[i] == 1:
                confusion_matrix[0][0] += 1
            else:
                confusion_matrix[0][1] += 1
        elif res == 16:
            if vektor_test[i] == 16:
                confusion_matrix[1][1] += 1
            else:
                confusion_matrix[1][0] += 1
    print(confusion_matrix)
    print(f1_score(vektor_test, y_pred, average=None, labels=[1, 4, 7, 10]))




"""
ex4_b on 3 and 9 class rockets.
"""
def checking_ML_3_9():
    """
    Create mutch data-trainning_set, test_set, vektor_test
    """
    real_df = df[df['class'].isin([3, 9])]
    tranning_set = real_df.iloc[:1900, :]
    test_set = real_df.iloc[1900:, :]
    vektor_test = test_set.iloc[:, -1]
    del test_set['class']
    """
    Checking result of the classify function-ex4_3_9.
    """
    e_3 = []
    e_9 = []
    y_pred = []
    confusion_matrix = [[0, 0], [0, 0]]
    for i in test_set.index:
        res = ex4_3_9(i, e_3, e_9)
        y_pred.append(res)
        if res == 3:
            if vektor_test[i] == 3:
                confusion_matrix[0][0] += 1
            else:
                confusion_matrix[0][1] += 1
        elif res == 9:
            if vektor_test[i] == 9:
                confusion_matrix[1][1] += 1
            else:
                confusion_matrix[1][0] += 1

    print(confusion_matrix)
    print(f1_score(vektor_test, y_pred, average=None, labels=[3,9]))

"""
ex4_b on 1,4,7,10 class rockets.
"""
def checking_ML_forth():
    """
    Create mutch data-trainning_set, test_set, vektor_test
    """
    real_df = df[df['class'].isin([1, 4, 7, 10])]
    tranning_set = real_df.iloc[:4200, :]
    test_set = real_df.iloc[4200:, :]
    vektor_test = test_set.iloc[:, -1]
    del test_set['class']
    """
    Checking result of the classify function-ex4_forth.
    """
    y_pred = []
    for i in test_set.index:
        res = ex4_forth(i)
        y_pred.append(res)
    Confusion_matrix = sklearn.metrics.confusion_matrix(vektor_test, y_pred, labels=[1, 4, 7, 10])
    print(Confusion_matrix)
    print(f1_score(vektor_test, y_pred, average=None, labels=[1, 4, 7, 10]))
