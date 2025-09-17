# Apply One-Hot Encoding to a 'Department' column.
"""
Data = {'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']}


"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def  OneHotEncoder(Data):
    df = pd.DataFrame(Data)

    df_encoded = pd.get_dummies(df, columns=['Department'])

    print(df_encoded)

def main():
    Data = {'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']}

    
    OneHotEncoder(Data)
if __name__ == "__main__":
    main()
