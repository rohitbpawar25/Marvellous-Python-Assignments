# Detect column data types and convert 'Age' from float to int.
"""
Data = {'Name': ['A', 'B', 'C'], 'Age': [21.0, 22.0, 23.0]}


"""

import pandas as pd

def Convert(Data):

    df = pd.DataFrame(Data)
    
    print("Before Conversion")
    print(df.dtypes)

    df['Age'] = df['Age'].astype(int)
    print("\nAfter Conversion")
    print(df.dtypes)

def main():
    Data = {'Name': ['A', 'B', 'C'], 'Age': [21.0, 22.0, 23.0]}

    
    Convert(Data)
if __name__ == "__main__":
    main()
