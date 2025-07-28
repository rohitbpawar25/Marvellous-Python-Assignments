# Assignment: Machine Learning - Wine Prediction

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

def LoadData(filepath):
    print("-" * 90)
    print("Loading dataset...")
    df = pd.read_csv(filepath)
    print("Data Loaded Successfully:")
    print("-" * 90)
    return df

def DisplayData(df):
    print("First 5 rows:")
    print(df.head())
    print("-" * 90)
    print("Last 5 rows:")
    print(df.tail())
    print("-" * 90)
    print("Data Info:")
    print(df.info())
    print("-" * 90)
    print("Summary Statistics:")
    print(df.describe())
    print("-" * 90)
    print("Null Values per Column:")
    print(df.isnull().sum())
    print("-" * 90)

def PreprocessData(df):
    X = df.drop(columns=['Class'])
    Y = df['Class']
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print("Data Preprocessed Successfully..")
    print("-" * 90)
    return X_scaled, Y, scaler, X.columns.tolist()

def TrainModel(X_scaled, Y):
    print("Splitting data and training the model...")
    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=42)
    model = LogisticRegression()
    model.fit(X_train, Y_train)
    print("Model Trained Successfully..")
    print("-" * 90)
    return model, X_test, Y_test

def EvaluateModel(model, X_test, Y_test):
    print("Evaluating the model...")
    Y_pred = model.predict(X_test)
    print("Evaluation Complete")
    print("-" * 90)
    print("Classification Report:")
    print(classification_report(Y_test, Y_pred))
    print(f"Accuracy: {accuracy_score(Y_test, Y_pred):.2f}")
    print(f"Precision: {precision_score(Y_test, Y_pred, average='weighted'):.2f}")
    print(f"Recall: {recall_score(Y_test, Y_pred, average='weighted'):.2f}")
    print(f"F1 Score: {f1_score(Y_test, Y_pred, average='weighted'):.2f}")
    print("-" * 90)

def PredictUserInput(model, scaler, feature_names):
    print("Enter values for a new wine sample:")
    user_input = []
    for feature in feature_names:
        val = float(input(f"{feature}: "))
        user_input.append(val)
    user_df = pd.DataFrame([user_input], columns=feature_names)
    user_scaled = scaler.transform(user_df)
    prediction = model.predict(user_scaled)
    print(f"\nPredicted Wine Class: {prediction[0]}")
    print("-" * 90)

def main():
    filepath = ("WinePredictor.csv")
    df = LoadData(filepath)
    DisplayData(df)
    X_scaled, Y, scaler, feature_names = PreprocessData(df)
    model, X_test, Y_test = TrainModel(X_scaled, Y)
    EvaluateModel(model, X_test, Y_test)
    PredictUserInput(model, scaler, feature_names)

if __name__ == "__main__":
    main()