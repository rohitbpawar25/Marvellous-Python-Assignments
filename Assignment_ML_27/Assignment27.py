# Case Study On Advertisement

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def LoadData(FilePath):
    print("-" * 90)
    df = pd.read_csv(FilePath)
    print("Data Loaded Successfully.")
    return df

def DisplayData(df):
    print("-" * 90)
    print("First 5 Rows:\n", df.head())
    print("-" * 90)
    print("Last 5 Rows:\n", df.tail())
    print("-" * 90)
    print("Shape:", df.shape)
    print("-" * 90)
    print("Info:")
    print(df.info())
    print("-" * 90)
    print("Description:\n", df.describe())
    print("-" * 90)
    print("Null Values:\n", df.isnull().sum())
    print("-" * 90)
    print("NA Values:\n", df.isna().sum())
    print("-" * 90)

def PreprocessData(df):
    print("Before Drop:\n", df.head())
    print("-"*90)

    df = df.drop(columns=['Unnamed: 0'], errors='ignore')
    print("After Drop:\n", df.head())
    print("-"*90)

    X = df[['TV', 'radio', 'newspaper']]
    Y = df['sales']

    return df, X, Y

def TrainModel(X, Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42)
    model = LinearRegression()
    model.fit(X_train, Y_train)
    print("Model Trained Successfully.")
    print("-"*90)
    return model, X_test, Y_test

def TestModel(model, X_test, Y_test):
    Y_pred = model.predict(X_test)
    print("Model Test Results:\n")
    print("Expected (Y_test):\n", Y_test.to_numpy())
    print("Predicted (Y_pred):\n", Y_pred)
    print("-" * 90)


    mse = mean_squared_error(Y_test, Y_pred)
    rmse = np.sqrt(mse)
    r2 = model.score(X_test, Y_test)

    print(f"Mean Squared Error (MSE): {mse:.4f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
    print(f"R-Squared Value: {r2:.4f}")
    print("-"*90)
    return Y_pred

def PredictFromUserInput(model):
    print("Enter advertisement spending to predict sales:\n")
    
    tv = float(input("TV Budget: "))
    radio = float(input("Radio Budget: "))
    newspaper = float(input("Newspaper Budget: "))

    user_input_df = pd.DataFrame([[tv, radio, newspaper]], columns=['TV', 'radio', 'newspaper'])
    prediction = model.predict(user_input_df)

    print(f"Predicted Sales: {prediction[0]:.2f} units")
    print("-" * 90)


def main():

    Filepath = "Advertising.csv"
    df = LoadData(Filepath)

    DisplayData(df)

    df, X, Y = PreprocessData(df)

    model, X_test, Y_test = TrainModel(X, Y)

    TestModel(model, X_test, Y_test)

    PredictFromUserInput(model)

if __name__ == "__main__":
    main()
