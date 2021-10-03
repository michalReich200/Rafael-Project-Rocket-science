import math
from audioop import avg

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("train.csv")
df = df[(df['class'] == 1) | (df['class'] == 4) |(df['class'] == 7) | (df['class'] == 10) ]


def calculate_energy(height, velocity, mass=1, g=10):
    kinetic_energy = 0.5 * mass * velocity * velocity
    potential_energy = mass * g * height
    return kinetic_energy + potential_energy


def get_columns():
    energy_list = []
    for i in df.index:
        v = math.sqrt((df.loc[i, 'velX_0'] ** 2) + (df.loc[i, 'velY_0'] ** 2) + (df.loc[i, 'velZ_0'] ** 2))
        energy = (v ** 2 * 0.5) + (10 * (df.loc[i, 'posZ_0']))
        energy_list.append(energy)
    df['energy'] = energy_list
    print(df)
    return df['class','energy']



def divide_data():
    shuffled = df.sample(frac=1)
    x_train = shuffled.sample(frac=0.8)
    x_test = df.drop(x_train.index)
    y_train = x_train['class']
    y_test = x_test['class']
    del x_train['class']
    del x_test['class']
    x_train = x_train.fillna(2500)
    x_test = x_test.fillna(2500)
    return x_train, x_test, y_train, y_test


def machine_learning():

    del df['targetName']
    y = df["class"]
    x = df
    x.drop(columns=['class'])
    x_train, x_test, y_train, y_test = divide_data()
    n_estimators=[30,70,100,100,90,90,20,20,500,500]
    C=[0.00001,0.9,3,10,20,50,200,1000,2000,0.1]
    avrage=[]
    for i in range(len(n_estimators)):
        l=[]
        for j in range(len(C)):
            logreg = LogisticRegression(C=C[j],n_estimators=n_estimators[i],max_iter=10000,dual=True,solver='liblinear')
            logreg.fit(x_train, y_train)
            l.append(logreg.score(x_test,y_test))
            print(logreg.predict_proba(x_test))
        avrage.append(sum(l)/len(l))
    print(avrage)
