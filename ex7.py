import math
from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.ensemble import RandomForestClassifier 

df = pd.read_csv("train.csv")
del df['targetName']
    

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



    
def random_forest_classifier_forth():
    df_forth = df[((df["class"] == 1) | (df["class"] == 4) | (df["class"] == 7) | (df["class"] == 10))]
    y = df_forth["class"]
    x = df_forth
    x.drop(columns=['class'])
    x_train, x_test, y_train, y_test = divide_data(df_forth)
    logreg = RandomForestClassifier()
    logreg.fit(x_train, y_train)
    print("random_forest_classifier_forth: ",logreg.score(x_test, y_test))
    
    
def logistic_regression_forth():
    df_forth = df[((df["class"] == 1) | (df["class"] == 4) | (df["class"] == 7) | (df["class"] == 10))]
    y = df_forth["class"]
    x = df_forth
    x.drop(columns=['class'])
    x_train, x_test, y_train, y_test = divide_data(df_forth)
    logreg = LogisticRegression()
    logreg.fit(x_train, y_train)
    print("logistic_regression_forth: ",logreg.score(x_test, y_test))




if __name__ == '__main__':
    random_forest_classifier_forth()
    logistic_regression_forth()

    
