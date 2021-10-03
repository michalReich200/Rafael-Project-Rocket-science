import math
from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.ensemble import RandomForestClassifier 

df = pd.read_csv("train.csv")
del df['targetName']


def logistic_regression_1_16():
    df_1_16 = df[((df["class"] == 1) | (df["class"] == 16))]
    y = df_1_16["class"]
    x = df_1_16
    x.drop(columns=['class'])
    x_train, x_test, y_train, y_test = divide_data(df_1_16)
    logreg = LogisticRegression()
    logreg.fit(x_train, y_train)
    print("logistic_regression_1_16:",logreg.score(x_test, y_test))
    
def random_forest_classifier_1_16():
    df_1_16 = df[((df["class"] == 1) | (df["class"] == 16))]
    y = df_1_16["class"]
    x = df_1_16
    x.drop(columns=['class'])
    x_train, x_test, y_train, y_test = divide_data(df_1_16)
    logreg = RandomForestClassifier()
    logreg.fit(x_train, y_train)
    print("random_forest_classifier_1_16:",logreg.score(x_test, y_test))


    

def calculate_energy(height, velocity, mass=1, g=10):
    kinetic_energy = 0.5 * mass * velocity * velocity
    potential_energy = mass * g * height
    return kinetic_energy + potential_energy


def divide_data(df):
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


def get_columns(df):
    energy_list = []
    for i in df.index:
        v = math.sqrt((df.loc[i, 'velX_0'] ** 2) + (df.loc[i, 'velY_0'] ** 2) + (df.loc[i, 'velZ_0'] ** 2))
        energy = calculate_energy(df.loc[i, 'posZ_0'],v)
        energy_list.append(energy)
    df['energy'] = energy_list



"""
ex_6
"""
def random_forest_classifier_12_15():
    df_12_15 = df[((df["class"] == 12) | (df["class"] == 15))]
    y = df_12_15["class"]
    x = df_12_15
    x.drop(columns=['class'])
    x_train, x_test, y_train, y_test = divide_data(df_12_15)
    logreg = RandomForestClassifier()
    logreg.fit(x_train, y_train)
    print("random_forest_classifier_12_15:",logreg.score(x_test, y_test))
    
    
def logistic_regression_12_15():
    df_12_15 = df[((df["class"] == 12) | (df["class"] == 15))]
    y = df_12_15["class"]
    x = df_12_15
    x.drop(columns=['class'])
    x_train, x_test, y_train, y_test = divide_data(df_12_15)
    logreg = LogisticRegression()
    logreg.fit(x_train, y_train)
    print("logistic_regression_12_15: ",logreg.score(x_test, y_test))
    

def random_forest_classifier_3_9():
    df_3_9 = df[((df["class"] == 3) | (df["class"] == 9))]
    y = df_3_9["class"]
    x = df_3_9
    x.drop(columns=['class'])
    x_train, x_test, y_train, y_test = divide_data(df_3_9)
    logreg = RandomForestClassifier()
    logreg.fit(x_train, y_train)
    print("random_forest_classifier_3_9: ",logreg.score(x_test, y_test))
    
    
def logistic_regression_3_9():
    df_3_9 = df[((df["class"] == 3) | (df["class"] == 9))]
    y = df_3_9["class"]
    x = df_3_9
    x.drop(columns=['class'])
    x_train, x_test, y_train, y_test = divide_data(df_3_9)
    logreg = LogisticRegression()
    logreg.fit(x_train, y_train)
    print("logistic_regression_3_9: ",logreg.score(x_test, y_test))
    
def random_forest_classifier_5_6():
    df_5_6 = df[((df["class"] == 5) | (df["class"] == 6))]
    y = df_5_6["class"]
    x = df_5_6
    x.drop(columns=['class'])
    x_train, x_test, y_train, y_test = divide_data(df_5_6)
    logreg = RandomForestClassifier()
    logreg.fit(x_train, y_train)
    print("random_forest_classifier_5_6: ",logreg.score(x_test, y_test))
    
    
def logistic_regression_5_6():
    df_5_6 = df[((df["class"] == 5) | (df["class"] == 6))]
    y = df_5_6["class"]
    x = df_5_6
    x.drop(columns=['class'])
    x_train, x_test, y_train, y_test = divide_data(df_5_6)
    logreg = LogisticRegression()
    logreg.fit(x_train, y_train)
    print("logistic_regression_5_6: ",logreg.score(x_test, y_test))

# def machine_learning_rule_based():



if __name__ == '__main__':
    random_forest_classifier_1_16()
    logistic_regression_1_16()
    
    random_forest_classifier_12_15()
    logistic_regression_12_15()
    
    random_forest_classifier_3_9()
    logistic_regression_3_9()
    
    random_forest_classifier_5_6()
    logistic_regression_5_6()
    
