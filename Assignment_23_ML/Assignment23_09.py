#  Create a DataFrame with missing values and fill them with the mean

"""
Data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [np.nan, 76, 88],
    'Science': [91, np.nan, 85]
}

"""

import pandas as pd
import numpy as np


def BasicInfo(DataPath):
    Line = "-"*90
    df = pd.DataFrame(DataPath) 
    print(Line)
    
    df['Math'].fillna(df['Math'].mean(), inplace=True)
    df['Science'].fillna(df['Science'].mean(), inplace=True)

    print("DataFrame after filling missing values:\n")
    print(df) 
    print(Line) 

def main():
    
    Data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [np.nan, 76, 88],
    'Science': [91, np.nan, 85]}

    BasicInfo(Data)


if __name__ == "__main__":
    main()