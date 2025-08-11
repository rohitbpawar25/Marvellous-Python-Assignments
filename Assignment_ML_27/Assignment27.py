########################################################
# Required Python Packages
########################################################

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

########################################################
# File Paths
########################################################

INPUT_PATH = "Advertising.csv"  # Ensure this file is in the same folder as this script

########################################################
# Load Data
# Input: Filepath (str): Path to CSV file
# Output: df (DataFrame): Loaded dataset
########################################################
def Load_Data(Filepath):
    df = pd.read_csv(Filepath)
    return df

########################################################
# Display Data
# Input: df (DataFrame): Dataset
# Output: None (prints dataset summary to console)
########################################################
def Display_Data(df):
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

########################################################
# Preprocess Data
# Input: df (DataFrame): Raw dataset
# Output:
#   df (DataFrame): Cleaned dataset
#   X (DataFrame): Features
#   Y (Series): Target variable (sales)
########################################################

def Preprocess_Data(df):
    print("Before dropping unnecessary columns:\n\n", df.head())
    print("-" * 90)

    # Drop index column if exists
    df = df.drop(columns=['Unnamed: 0'], errors='ignore')

    print("After dropping unnecessary columns:\n\n", df.head())

    X = df[['TV', 'radio', 'newspaper']]
    Y = df['sales']

    return df, X, Y

########################################################
# Train Model
# Input:
#   X (DataFrame): Features
#   Y (Series): Target variable
# Output:
#   model (LinearRegression): Trained Linear Regression model
#   X_test (DataFrame): Test features
#   Y_test (Series): Test target
########################################################

def Train_Model(X, Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42)

    model = LinearRegression()
    model.fit(X_train, Y_train)

    return model, X_test, Y_test

########################################################
# Evaluate Model and Predict From User Input
# Input:
#   model (LinearRegression): Trained model
#   X_test (DataFrame): Test features
#   Y_test (Series): Test targets
# Output: None (prints evaluation and prediction results)
########################################################

def Predict_From_User_Input(model, X_test, Y_test):
    # Evaluate model on test data
    Y_pred_test = model.predict(X_test)
    mse = mean_squared_error(Y_test, Y_pred_test)
    rmse = np.sqrt(mse)
    r2 = model.score(X_test, Y_test)

    print(f"Mean Squared Error (MSE) on Test Set: {mse:.4f}")
    print(f"Root Mean Squared Error (RMSE) on Test Set: {rmse:.4f}")
    print(f"R-Squared Value on Test Set: {r2:.4f}")
    print("-" * 90)

    # Get user input to predict sales
    tv = float(input("Enter TV Budget: "))
    radio = float(input("Enter Radio Budget: "))
    newspaper = float(input("Enter Newspaper Budget: "))

    user_input_df = pd.DataFrame([[tv, radio, newspaper]], columns=['TV', 'radio', 'newspaper'])
    prediction = model.predict(user_input_df)

    print(f"Predicted Sales: {prediction[0]:.2f} units")

########################################################
# Main Execution
# Case Study : 
# Author name : Rohit Pawar
# Date : 26-07-2025
########################################################
def main():
    print("-" * 90)
    print("Case Study: Advertising Sales Prediction Using Linear Regression".center(90))
    print("-" * 90)

    # Step 1: Load Data
    print("Loading data from CSV file...".center(90))
    df = Load_Data(INPUT_PATH)
    print("Data loaded successfully.".center(90))
    print("-" * 90)

    # Step 2: Display Data Summary
    print("Displaying data summary...".center(90))
    Display_Data(df)
    print("-" * 90)

    # Step 3: Preprocess Data
    print("Data preprocessed successfully.\n".center(90))
    df, X, Y = Preprocess_Data(df)
    print("-" * 90)

    # Step 4: Train Model
    print("Training Linear Regression model...".center(90))
    model, X_test, Y_test = Train_Model(X, Y)
    print("-"*90)

    # Step 5: Evaluate model and predict sales from user input
    print("Evaluating model on test set and predicting sales from user input...".center(90))
    Predict_From_User_Input(model, X_test, Y_test)
    print("-" * 90)

########################################################
# Run the main function
########################################################
if __name__ == "__main__":
    main()
