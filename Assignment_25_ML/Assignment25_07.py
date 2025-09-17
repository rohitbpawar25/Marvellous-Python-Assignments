# Normalize 'Age' column using Min-Max Scaling
"""
Data = {'Age': [18, 22, 25, 30, 35]}

"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def  Dictionary(Data):

    df = pd.DataFrame(Data)

    scaler = MinMaxScaler()
    df['Age_Normalized'] = scaler.fit_transform(df[['Age']])

    print(df)


def main():

    Data = {'Age': [18, 22, 25, 30, 35]}
    Dictionary(Data)

if __name__ == "__main__":
    main()
