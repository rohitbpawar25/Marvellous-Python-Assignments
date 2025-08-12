########################################################
# Required Python Packages
########################################################
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

########################################################
# File Paths
########################################################

INPUT_PATH = "WinePredictor.csv"  # Ensure this file contains the wine dataset with 'Class' column

########################################################
# Load Data
# Input:
#   Filepath (str): Path to CSV file
# Output:
#   df (DataFrame): Loaded dataset
########################################################
def Load_Data(Filepath):
    df = pd.read_csv(Filepath)
    return df

########################################################
# Display Data 
# Input:
#   df (DataFrame): Dataset
# Output:
#   None (prints dataset summary to console)
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
    df.info()
    print("-" * 90)
    print("Description:\n", df.describe())
    print("-" * 90)
    print("Null Values:\n", df.isnull().sum())
    print("-" * 90)
    print("NA Values:\n", df.isna().sum())

########################################################
# Preprocess Data
# Input:
#   df (DataFrame): Raw dataset
# Output:
#   X_scaled (ndarray): Scaled feature matrix
#   Y (Series): Target variable
#   scaler (StandardScaler): Fitted scaler object
#   feature_names (list): List of feature column names
########################################################
def Preprocess_Data(df):
    X = df.drop(columns=['Class'])
    Y = df['Class']
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, Y, scaler, X.columns.tolist()

########################################################
# Train Model
# Input:
#   X_scaled (ndarray): Scaled features
#   Y (Series): Target variable
# Output:
#   model (LogisticRegression): Trained model
#   X_test (ndarray): Test features
#   Y_test (Series): Test target
########################################################
def Train_Model(X_scaled, Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, Y_train)
    return model, X_test, Y_test

########################################################
# Evaluate Model
# Input:
#   model (LogisticRegression): Trained model
#   X_test (ndarray): Test features
#   Y_test (Series): Test target
# Output:
#   None (prints classification report and metrics)
########################################################
def Evaluate_Model(model, X_test, Y_test):
    Y_pred = model.predict(X_test)
    print("Classification Report:")
    print(classification_report(Y_test, Y_pred))
    print(f"Accuracy: {accuracy_score(Y_test, Y_pred)*100:.2f}")
    print(f"Precision: {precision_score(Y_test, Y_pred, average='weighted')*100:.2f}")
    print(f"Recall: {recall_score(Y_test, Y_pred, average='weighted')*100:.2f}")
    print(f"F1 Score: {f1_score(Y_test, Y_pred, average='weighted')*100:.2f}")

########################################################
# Predict From User Input
# Input:
#   model (LogisticRegression): Trained model
#   scaler (StandardScaler): Fitted scaler object
#   feature_names (list): List of feature column names
# Output:
#   None (prints predicted class for user input)
########################################################
def Predict_User_Input(model, scaler, feature_names):
    print("Enter values for a new wine sample:")
    user_input = []
    for feature in feature_names:
        val = float(input(f"{feature}: "))
        user_input.append(val)
    user_df = pd.DataFrame([user_input], columns=feature_names)
    user_scaled = scaler.transform(user_df)
    prediction = model.predict(user_scaled)
    print(f"\nPredicted Wine Class: {prediction[0]}")

########################################################
# Main Execution
# Case Study : Wine Classification Using Logistic Regression
# Author name : Rohit Pawar
# Date : 19-07-2025
########################################################
def main():
    print("-" * 90)
    print("Case Study: Wine Classification Using Logistic Regression".center(90))
    print("Author: Rohit Pawar".center(90))
    print("Date: 19-07-2025".center(90))
    print("-" * 90)

    # Step 1: Load Data
    print("Loading data from CSV file...".center(90))
    df = Load_Data(INPUT_PATH)
    print("Data loaded Successfully.".center(90))
    print("-" * 90)

    # Step 2: Display Data Summary
    print("Displaying data Summary...".center(90))
    Display_Data(df)
    print("-" * 90)

    # Step 3: Preprocess Data
    print("Preprocessing data Successfully...".center(90))
    X, Y, scaler, feature_names = Preprocess_Data(df)
    print("-" * 90)

    # Step 4: Train Model
    print("Training Logistic Regression model...".center(90))
    model, X_test, Y_test = Train_Model(X, Y)
    print("-" * 90)

    # Step 5: Evaluate Model
    print("Model Evaluation".center(90))
    Evaluate_Model(model, X_test, Y_test)
    print("-" * 90)

    # Step 6: Predict from User Input
    Predict_User_Input(model, scaler, feature_names)
    print("-" * 90)

########################################################
# Run the main function
########################################################
if __name__ == "__main__":
    main()
