# Sort the DataFrame by 'Total' marks in descending order :

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
    
    df['Total'] = df[['Math','Science','English']].sum(axis=1)

    Sort = df.sort_values(by='Total',ascending=False)

    print("Sorted DataFrame by Total Marks :")
    print(Sort)


def main():

    Data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]}

    BasicInfo(Data)


if __name__ == "__main__":
    main()