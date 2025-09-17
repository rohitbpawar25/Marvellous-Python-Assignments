
########################################################
# Required Python Packages
########################################################
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

########################################################
# File Paths
########################################################

INPUT_PATH = "diabetes.csv"  # Ensure this file is in the same folder as this script

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
def DisplayData(df):
    print("First 5 rows:\n", df.head())
    print("-" * 90)
    print("Last 5 rows:\n", df.tail())
    print("-" * 90)
    print("Data types:\n", df.dtypes)
    print("-" * 90)
    print("Summary statistics:\n", df.describe())
    print("-" * 90)
    print("Shape:", df.shape)
    print("Size:", df.size)
    print("Columns:", df.columns)
    print("Index:", df.index)
    print("-" * 90)
    print("Info:")
    print(df.info())
    print("-" * 90)
    print("Correlation:\n", df.corr())
    print("-" * 90)
    print("Null values:\n", df.isnull().sum())
    print("NA values:\n", df.isna().sum())

########################################################
# Visualize Data
# Input: df (DataFrame): Dataset
# Output: None (displays plots)
########################################################
def VisualizeData(df):
    sns.countplot(x='Outcome', data=df)
    plt.title("Target Variable Distribution")
    plt.show()

    df.hist(figsize=(10, 8))
    plt.suptitle("Feature Distributions")
    plt.show()

    sns.boxplot(data=df)
    plt.title("Boxplot for Outlier Detection")
    plt.show()
    
    # Pairplot to visualize feature relationships colored by Outcome
    sns.pairplot(df, hue='Outcome')
    plt.suptitle("Pairplot of features by Outcome", y=1.02)
    plt.show()

########################################################
# Preprocess Data
# Input: df (DataFrame): Raw dataset
# Output:
#   X_scaled (ndarray): Feature matrix after scaling
#   Y (Series): Target variable
#   scaler (StandardScaler): Fitted scaler object for future transformations
########################################################
def PreprocessData(df):
    cols_with_zero = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    # Replace zero values with NaN for imputation
    df[cols_with_zero] = df[cols_with_zero].replace(0, np.nan)
    # Fill NaN with column mean
    df.fillna(df.mean(), inplace=True)

    X = df.drop('Outcome', axis=1)
    Y = df['Outcome']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, Y, scaler

########################################################
# Train Model
# Input:
#   X (ndarray): Features
#   Y (Series): Target variable
# Output:
#   model (LogisticRegression): Trained Logistic Regression model (default returned)
#   X_test (ndarray): Test features
#   Y_test (Series): Test target variable
########################################################
def TrainModels(X, Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    models = {
        'Logistic Regression': LogisticRegression(max_iter=1000),
        'K-Nearest Neighbors': KNeighborsClassifier(),
        'Decision Tree': DecisionTreeClassifier()
    }

    for name, model in models.items():
        model.fit(X_train, Y_train)
        Y_pred = model.predict(X_test)

        print(f"\n{name}")
        print("Accuracy:", accuracy_score(Y_test, Y_pred))
        print("Confusion Matrix:\n", confusion_matrix(Y_test, Y_pred))
        print("Classification Report:\n", classification_report(Y_test, Y_pred))
        print("-"*90)

        sns.heatmap(confusion_matrix(Y_test, Y_pred), annot=True, fmt='d', cmap='Blues')
        plt.title(f"{name} - Confusion Matrix")
        plt.show()

    # Returning Logistic Regression model by default as final model
    return models['Logistic Regression'], X_test, Y_test

########################################################
# Predict From User Input
# Input:
#   model (LogisticRegression): Trained model
#   scaler (StandardScaler): Scaler used during training
# Output: None (prints prediction and saves CSV)
########################################################
def PredictFromUserInput(model, scaler):
    print("\nEnter patient details for prediction:")

    pregnancies = float(input("Pregnancies: "))
    glucose = float(input("Glucose: "))
    blood_pressure = float(input("BloodPressure: "))
    skin_thickness = float(input("SkinThickness: "))
    insulin = float(input("Insulin: "))
    bmi = float(input("BMI: "))
    diabetes_pedigree = float(input("DiabetesPedigreeFunction: "))
    age = float(input("Age: "))

    features = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]
    input_array = np.array(features).reshape(1, -1)
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)

    result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"
    print(f"\nPrediction: The patient is likely :- {result}.")

    # Save to CSV
    output_df = pd.DataFrame([{
        'Pregnancies': pregnancies,
        'Glucose': glucose,
        'BloodPressure': blood_pressure,
        'SkinThickness': skin_thickness,
        'Insulin': insulin,
        'BMI': bmi,
        'DiabetesPedigreeFunction': diabetes_pedigree,
        'Age': age,
        'Prediction': result
    }])

    output_df.to_csv('TestPredictions.csv', index=False)
    print("\nPrediction saved to 'TestPredictions.csv'.")
    print("Sample Output:\n", output_df)

########################################################
# Main Execution
# Case Study : Diabetes Prediction Using Machine Learning
# Author: Rohit Pawar
# Date: 24-07-2025
########################################################
def main():
    print("-" * 90)
    print("Case Study: Diabetes Prediction Using Machine Learning".center(90))
    print("Author: Rohit Pawar".center(90))
    print("Date: 24-07-2025".center(90))
    print("-" * 90)

    print("Loading data from CSV file...".center(90))
    df = Load_Data(INPUT_PATH)
    print("Data loaded successfully.".center(90))
    print("-" * 90)

    print("Displaying data summary...".center(90))
    DisplayData(df)
    print("-" * 90)

    print("Visualizing data...".center(90))
    VisualizeData(df)
    print("-" * 90)

    print("Preprocessing data...".center(90))
    X, Y, scaler = PreprocessData(df)
    print("Data preprocessed successfully.".center(90))
    print("-" * 90)

    print("Training models...".center(90))
    model, X_test, Y_test = TrainModels(X, Y)

    print("Predicting from user input...".center(90))
    PredictFromUserInput(model, scaler)
    print("-" * 90)

########################################################
# Run the main function
########################################################
if __name__ == "__main__":
    main()
