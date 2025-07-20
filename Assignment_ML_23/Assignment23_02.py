# Use the DataFrame from Q1 and print descriptive statistics using .describe()

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
    
    print("Descriptive Statistics: ")
    print(df.describe())
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