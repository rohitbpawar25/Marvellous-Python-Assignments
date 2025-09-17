# Q1: Normalize the 'Math' scores using Min-Max scaling

import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def Normalize(DataPath):

    df = pd.DataFrame(DataPath)
    scaler = MinMaxScaler()
    df['Math_normalized'] = scaler.fit_transform(df[['Math']])
    print(df[['Name', 'Math', 'Math_normalized']])

def main():

    Data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]}

    Normalize(Data)


if __name__ == "__main__":
    main()