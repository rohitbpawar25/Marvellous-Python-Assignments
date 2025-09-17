# Create a DataFrame with 'Age' and 'Purchased' columns and split into train/test sets
"""
Data = {'Age': [22, 25, 47, 52, 46, 56], 'Purchased': [0, 1, 1, 0, 1, 0]}


"""

import pandas as pd
from sklearn.model_selection import train_test_split

def  TrainTest(Data):
    df = pd.DataFrame(Data)

    X = df[['Age']]
    y = df['Purchased']


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


    print("X_train:\n", X_train)
    print("\nX_test:\n", X_test)
    print("\ny_train:\n", y_train)
    print("\ny_test:\n", y_test)

def main():
    Data = {'Age': [22, 25, 47, 52, 46, 56], 'Purchased': [0, 1, 1, 0, 1, 0]}
    
    TrainTest(Data)
if __name__ == "__main__":
    main()
