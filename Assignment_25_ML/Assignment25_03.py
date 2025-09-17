# Apply Label Encoding to a 'City' column
"""
Data = {'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi']}

"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def Encoder(Data):
    df = pd.DataFrame(Data)

    le = LabelEncoder()
    df['City_encoded'] = le.fit_transform(df['City'])

    print(df)

def main():
    Data = {'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi']}

    
    Encoder(Data)
if __name__ == "__main__":
    main()
