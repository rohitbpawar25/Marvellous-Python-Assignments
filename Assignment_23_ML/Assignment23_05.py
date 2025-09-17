# Replace 'Pooja' with 'Puja' in the 'Name' column of the DataFrame.

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
    
    df['Name'] = df['Name'].replace('Pooja','Puja')
    print("Repaced Name :")
    print(df)
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