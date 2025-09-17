# Display students who scored more than 85 in Science.

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
    
    Score = df[df['Science']>85][['Science']]
    print("Students with Science marks > 85:")
    print(Score)


def main():

    Data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]}

    BasicInfo(Data)


if __name__ == "__main__":
    main()