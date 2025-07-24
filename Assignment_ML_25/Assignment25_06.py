# Replace multiple values in a column using a dictionary
"""
Data = {'Grade': ['A+', 'B', 'A', 'C', 'B+']} 

Replace as:
'A+': 'Excellent'
'A': 'Very Good'
'B+': 'Good'
'B': 'Average'
'C': 'Poor'

"""

import pandas as pd

def  Dictionary(Data):
    df = pd.DataFrame(Data)

    grade_map = {
    'A+': 'Excellent',
    'A': 'Very Good',
    'B+': 'Good',
    'B': 'Average',
    'C': 'Poor'}

    df['Grade'] = df['Grade'].map(grade_map)
    print(df)

def main():

    Data = {'Grade': ['A+', 'B', 'A', 'C', 'B+']}
    Dictionary(Data)

if __name__ == "__main__":
    main()
