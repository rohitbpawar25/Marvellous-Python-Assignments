########################################################
# Required Python Packages
########################################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, confusion_matrix, classification_report,
    roc_auc_score, roc_curve
)

########################################################
# File Paths
########################################################

INPUT_PATH = "Bank.csv"  # Dataset file path

########################################################
# Load Data
# Input: Filepath (str): Path to CSV file
# Output: df (DataFrame): Loaded dataset
########################################################

def Load_Data(Filepath):
    df = pd.read_csv(Filepath, sep=';')
    return df

########################################################
# Display Data
# Input: df (DataFrame): Dataset
# Output: None (prints data summary)
########################################################

def Display_Data(df):
    print("First 5 Rows:\n", df.head())
    print("-" * 90)
    print("Last 5 Rows:\n", df.tail())
    print("-" * 90)
    print("Shape:", df.shape)
    print("-" * 90)
    print("Info:")
    print(df.info())
    print("-" * 90)
    print("Description:\n", df.describe(include='all'))
    print("-" * 90)
    print("Null Values:\n", df.isnull().sum())
    print("-" * 90)
    print("Class Distribution:\n", df['y'].value_counts())

    # Class distribution plot
    sns.countplot(x='y', data=df)
    plt.title("Target Class Distribution")
    plt.show()

########################################################
# Preprocess Data
# Input: df (DataFrame)
# Output:
#   X_scaled: Scaled feature set
#   Y: Target values
#   scaler: StandardScaler object
#   X_columns: Column names after preprocessing
########################################################

def PreProcess_Data(df):
    # Replace 'unknown' with NaN and handle missing
    df.replace('unknown', np.nan, inplace=True)
    df.ffill(inplace=True)

    # Normalize text categorical values so one-hot column names are consistent
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str).str.strip().str.lower()

    # Convert binary yes/no columns to 0/1 (keep as numeric)
    binary_cols = ['default', 'housing', 'loan']
    for col in binary_cols:
        if col in df.columns:
            df[col] = df[col].map({'yes': 1, 'no': 0}).fillna(df[col])

    # Encode target
    df['y'] = df['y'].map({'yes': 1, 'no': 0})

    # Determine categorical columns to one-hot (exclude binary and target)
    cat_cols = [c for c in df.select_dtypes(include=['object']).columns if c != 'y' and c not in binary_cols]

    # One-hot encode categorical columns (do NOT drop first; keep all columns)
    if len(cat_cols) > 0:
        df = pd.get_dummies(df, columns=cat_cols, prefix=cat_cols, prefix_sep='_', drop_first=False)

    # Features and target
    X = df.drop('y', axis=1)
    Y = df['y']

    # Scale numeric features
    numeric_cols = [c for c in ['age', 'balance', 'duration', 'campaign'] if c in X.columns]
    scaler = StandardScaler()
    if len(numeric_cols) > 0:
        X[numeric_cols] = scaler.fit_transform(X[numeric_cols])

    print("Data Preprocessing Completed.".center(90))
    print("-" * 90)
    return X, Y, scaler, X.columns

########################################################
# Train and Test Models
# Input:
#   X_train, X_test, y_train, y_test
# Output:
#   models: Dictionary of trained models
########################################################

def Train_Test(X_train, X_test, y_train, y_test):
    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "KNN": KNeighborsClassifier(n_neighbors=5),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)
    }

    for name, model in models.items():
        print("-" * 90)
        print(f"{name} model in testing..".center(90))
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        print(f"Accuracy {name} is : {acc*100:.2f}")
        print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
        print("\nClassification Report:\n", classification_report(y_test, y_pred))

        # ROC Curve
        if hasattr(model, 'predict_proba'):
            y_prob = model.predict_proba(X_test)[:, 1]
            fpr, tpr, _ = roc_curve(y_test, y_prob)
            auc_score = roc_auc_score(y_test, y_prob)

            plt.figure()
            plt.plot(fpr, tpr, label=f'{name} (AUC = {auc_score:.2f})')
            plt.plot([0, 1], [0, 1], 'k--')
            plt.title(f'{name} - ROC Curve')
            plt.xlabel('False Positive Rate')
            plt.ylabel('True Positive Rate')
            plt.legend(loc='lower right')
            plt.grid(True)
            plt.show()

    return models

########################################################
# Feature Importance
# Input:
#   model: Trained model
#   feature_names: List of feature names
#   model_name: Model name string
########################################################

def Feature_Importance(model, feature_names, model_name):
    if hasattr(model, 'feature_importances_'):
        importances = model.feature_importances_
        indices = importances.argsort()[::-1]

        plt.figure(figsize=(10, 6))
        plt.title(f"{model_name} - Top 10 Feature Importances")
        top_n = min(10, len(importances))
        plt.bar(range(top_n), importances[indices[:top_n]], align='center')
        plt.xticks(range(top_n), [feature_names[i] for i in indices[:top_n]], rotation=45)
        plt.tight_layout()
        plt.grid(True)
        plt.show()

########################################################
# Predict With User Input
# Input:
#   models: Trained models
#   scaler: StandardScaler object
#   X_columns: List of features
########################################################

def Predict_User_Input(models, scaler, X_columns):
    print("\nEnter customer details for prediction:")

    # Basic numeric + binary fields
    age = int(input("Age: "))
    job = input("Job (e.g., admin., technician, management, etc.): ").strip().lower()
    education = input("Education (primary, secondary, tertiary): ").strip().lower()
    default = input("Has credit in default? (yes/no): ").lower()
    balance = float(input("Average yearly balance: "))
    housing = input("Has housing loan? (yes/no): ").lower()
    loan = input("Has personal loan? (yes/no): ").lower()
    duration = float(input("Last contact duration (seconds): "))
    campaign = int(input("Number of contacts during campaign: "))

    # Start with empty dict (all columns zero)
    input_dict = {col: 0 for col in X_columns}

    # Fill numeric/binary fields (columns were normalized during preprocessing)
    if 'age' in input_dict:
        input_dict['age'] = age
    if 'balance' in input_dict:
        input_dict['balance'] = balance
    if 'duration' in input_dict:
        input_dict['duration'] = duration
    if 'campaign' in input_dict:
        input_dict['campaign'] = campaign
    if 'default' in input_dict:
        input_dict['default'] = 1 if default == 'yes' else 0
    if 'housing' in input_dict:
        input_dict['housing'] = 1 if housing == 'yes' else 0
    if 'loan' in input_dict:
        input_dict['loan'] = 1 if loan == 'yes' else 0

    # Set one-hot job column if present (column format: job_<category>)
    job_col = f'job_{job}'
    if job_col in input_dict:
        input_dict[job_col] = 1

    # Set one-hot education column if present (column format: education_<category>)
    edu_col = f'education_{education}'
    if edu_col in input_dict:
        input_dict[edu_col] = 1

    # Convert to DataFrame in correct column order
    input_df = pd.DataFrame([input_dict], columns=X_columns)

    # Scale numeric features exactly as in training
    numeric_cols = [c for c in ['age', 'balance', 'duration', 'campaign'] if c in input_df.columns]
    if len(numeric_cols) > 0:
        input_df[numeric_cols] = scaler.transform(input_df[numeric_cols])

    # Predict with each model
    for name, model in models.items():
        pred = model.predict(input_df)[0]
        result = "Subscribed" if pred == 1 else "Not Subscribed"
        print(f"\n{name} prediction: The customer is likely to be: {result}")

########################################################
# Main Execution 
# Case Study : Bank Term Deposit Subscription Prediction using Random Forest Classifier, Logistic Regression and Decision Tree Classifier
# Author: Rohit Pawar
# Date: 25-07-2025
########################################################

def main():
    print("-" * 90)
    print("Case Study : Bank Term Deposit Subscription Prediction".center(90))
    print("Author: Rohit Pawar".center(90))
    print("Date: 25-08-2025".center(90))
    print("-" * 90)

    # Step 1: Load Data
    print("Loaded Data...".center(90))
    df = Load_Data(INPUT_PATH)
    print("-" * 90)

    # Step 2: Display Data
    print("Displaying Data...".center(90))
    Display_Data(df)
    print("-" * 90)

    # Step 3: PreProcessing Data
    print("PreProcessed Data ...".center(90))
    X_scaled, Y, scaler, X_columns = PreProcess_Data(df)
    print("-" * 90)

    # Step 4: Train-Test Split
    print("Splitting Data into Train and Test...".center(90))
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=42)

    # Step 5: Training Model
    print("Training Model...".center(90))
    models = Train_Test(X_train, X_test, y_train, y_test)
    print("-" * 90)

    # Step 6: Feature Importance
    print("Feature Importance...".center(90))
    for model_name, model in models.items():
        Feature_Importance(model, list(X_columns), model_name)
    print("-" * 90)

    # Step 7: Predict With User Input
    print("Predicting with User Input...".center(90))
    Predict_User_Input(models, scaler, list(X_columns))
    print("-" * 90)

########################################################
# Run Main
########################################################

if __name__ == "__main__":
    main()
