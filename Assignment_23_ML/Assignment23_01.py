# Create a DataFrame for student marks and print basic information like shape, columns, and data types.
"""
data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

"""

import pandas as pd

def BasicInfo(DataPath):
    
    Line = "-"*90
    df = pd.DataFrame(DataPath)
    print(Line)

    print("Shape of DataFrame :")
    print(df.shape)
    print(Line)

    print("Column names :")
    print(df.columns)
    print(Line) 

    print("Data types :")
    print(df.dtypes)
    print(Line)

def main():

    Data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]}

    BasicInfo(Data)


if __name__ == "__main__":
    main()