import pandas as pd


df = pd.read_csv("train.csv")
df.drop(columns=['targetName'])



def ex3():
   
    
    real_df = df[df['class'].isin([1,16])]

    """
    a
    Create new table with only 1 and 16 class rockets
    (1900 is 80% of the rows in real_df).
    """
    tranning_set = real_df.iloc[:1900,:]
    test_set = real_df.iloc[1900:,:]
    """
    b
    Create new table with only 1 and 16 class rockets
    """
    vektor_test = test_set.iloc[:,-1]
    del test_set['class']
