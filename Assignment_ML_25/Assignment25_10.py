# Split a DataFrame with multiple features into train-test for supervised learning
"""
 Data = {
    'Age': [25, 30, 45, 35, 22],
    'Salary': [50000, 60000, 80000, 65000, 45000],
    'Purchased': [1, 0, 1, 0, 1]}

"""

import pandas as pd
from sklearn.model_selection import train_test_split


def DataFrame(Data):
    df = pd.DataFrame(Data)

    X = df[['Age', 'Salary']]
    y = df['Purchased']

   
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("X_train:\n", X_train)
    print("y_train:\n", y_train)

def main():
    Data = {
    'Age': [25, 30, 45, 35, 22],
    'Salary': [50000, 60000, 80000, 65000, 45000],
    'Purchased': [1, 0, 1, 0, 1]}


    DataFrame(Data)

if __name__ == "__main__":
    main()
