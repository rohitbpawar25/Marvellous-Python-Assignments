# Q2: Create a gender column and perform one-hot encoding

"""
data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

"""

import pandas as pd

def AddGenderColumn(Datapath):
    df = pd.DataFrame(Datapath)
    df['Gender'] = ['Male', 'Male', 'Female']
    df_encoded = pd.get_dummies(df, columns=['Gender'])
    print(df_encoded)

def main():
    Data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    AddGenderColumn(Data)

if __name__ == "__main__":
    main()
