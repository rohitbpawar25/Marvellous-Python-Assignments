########################################################
# Required Python Packages
########################################################

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, confusion_matrix, classification_report,
    roc_auc_score, roc_curve
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import joblib

########################################################
# File Paths
########################################################

INPUT_PATH = load_breast_cancer()  # Make sure this file exists in the same folder
OUTPUT_PATH = "Assignment_34_Model.pkl" 

########################################################
# Load Data
# Input: Filepath (str): Path to the CSV file
# Output: df (DataFrame): Loaded dataset
########################################################

def Load_Data(Filepath):
    data = Filepath  # Load the breast cancer dataset directly since it's a predefined dataset in sklearn
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    return df

########################################################
# Display Data
# Input: df (DataFrame): Dataset
# Output: None (prints data summary to console)
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
    print("Description:\n", df.describe())
    print("-" * 90)
    print("Null Values:\n", df.isnull().sum())
    print("-" * 90)
    print("NA Values:\n", df.isna().sum())

########################################################
# Preprocess Data
# Input: df (DataFrame): Raw dataset
# Output:
#   X: Feature set
#   Y: Target values
########################################################

def PreProcess_Data(df):
    X = df.drop(columns='target')  # Extract features (excluding target column)
    Y = df['target']  # Extract target column
    return X, Y

########################################################
# Train Model
# Input:
#   X_train (ndarray): Training features
#   X_test (ndarray): Test features
#   y_train (ndarray): Training target labels
#   y_test (ndarray): Test target labels
# Output:
#   models (dict): Dictionary of trained models
########################################################

def Train_Test(X_train, X_test, y_train, y_test):
    models = {
        "Decision Tree": DecisionTreeClassifier(max_depth=7),
        "Random Forest": RandomForestClassifier(max_depth=7),
        "Gradient Boosting": GradientBoostingClassifier()
    }

    trained_models = {}

    for name, clf in models.items():
        model_pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('classifier', clf)
        ])
        print("-" * 90)
        print(f"{name} model in testing..".center(90))
        model_pipeline.fit(X_train, y_train)
        y_pred = model_pipeline.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        print(f"Accuracy {name} is : {acc*100:.2f}")
        print(f"Confusion Matrix for {name}:\n", confusion_matrix(y_test, y_pred))
        print("\nClassification Report:\n", classification_report(y_test, y_pred))

        if hasattr(model_pipeline, 'predict_proba'):
            y_prob = model_pipeline.predict_proba(X_test)[:, 1]
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

        trained_models[name] = model_pipeline

    return trained_models

########################################################
# Save Best Model with Joblib
########################################################
def Save_Model(model, Filename):
    joblib.dump(model, Filename)

########################################################
# Feature Importance
# Input:
#   model (sklearn model): Trained model pipeline
#   feature_names (list): List of feature names
#   model_name (str): The name of the model
# Output:
#   None: Displays a bar plot of top 10 most important features
########################################################

def Feature_Importance(model, feature_names, model_name):
    if hasattr(model.named_steps['classifier'], 'feature_importances_'):
        importances = model.named_steps['classifier'].feature_importances_
        indices = importances.argsort()[::-1]

        plt.figure(figsize=(10, 6))
        plt.title(f"{model_name} - Top 10 Feature Importances")
        plt.bar(range(10), importances[indices[:10]], align='center')
        plt.xticks(range(10), [feature_names[i] for i in indices[:10]], rotation=45)
        plt.tight_layout()
        plt.grid(True)
        plt.show()

########################################################
# Predict With User Input
# Input:
#   model (sklearn model): A trained classifier pipeline
#   feature_names (list): List of feature names in the dataset
# Output:
#   None: Prints the prediction result based on the user input
########################################################

def Predict_With_User_Input(model, feature_names):
    print("\nEnter values for the following 30 features (numerical only):")
    user_input = []
    for feature in feature_names:
        val = float(input(f"{feature}: "))
        user_input.append(val)
    user_input_df = pd.DataFrame([user_input], columns=feature_names)
    prediction = model.predict(user_input_df)[0]
    result = "Malignant (Cancerous)" if prediction == 0 else "Benign (Non-cancerous)"
    print(f"\nPrediction: {result}")

########################################################
# Additional Function : Correlation Heatmap
# Input:
#   df (DataFrame): The dataset including features and target
# Output:
#   None: Displays a heatmap showing correlation between features
########################################################
def Plot_Correlation(df):
    import seaborn as sns
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.corr(), cmap="coolwarm", annot=False)
    plt.title("Feature Correlation Heatmap")
    plt.show()

########################################################
# Additional Function : Compare Model Accuracies
# Input:
#   models (dict): Dictionary of trained models
#   X_test (ndarray): Test features
#   y_test (ndarray): Test target labels
# Output:
#   None: Prints accuracy for each model and highlights the best model
########################################################
def Compare_Model_Accuracies(models, X_test, y_test):
    accuracies = {}
    for name, model in models.items():
        y_pred = model.predict(X_test)
        accuracies[name] = accuracy_score(y_test, y_pred)
    print("\nModel Accuracies:")
    for name, acc in accuracies.items():
        print(f"{name}: {acc:.4f}")
    best_model = max(accuracies, key=accuracies.get)
    print(f"\nBest Model: {best_model} with Accuracy: {accuracies[best_model]:.4f}")

########################################################
# Main Execution 
# Case Study : Breast Cancer Classification Using Decision Trees,Random Forest, and Gradient Boosting
# Author: Rohit Pawar
# Date: 02-08-2025
########################################################

def main():
    print("-" * 90)
    print("Case Study : Breast Cancer Classification Using Decision Trees,Random Forest, and Gradient Boosting".center(90))
    print("Author: Rohit Pawar".center(90))
    print("Date: 02-08-2025".center(90))
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
    X, Y = PreProcess_Data(df)
    print("-" * 90)

    # Step 4: Train-Test Split
    print("Splitting Data into Train and Test...".center(90))
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    # Step 5: Training Model
    print("Training Model...".center(90))
    models = Train_Test(X_train, X_test, y_train, y_test)
    print("-" * 90)

    # Step 6: Model Save
    print("Model Saved...".center(90))
    Save_Model(models["Gradient Boosting"], OUTPUT_PATH)
    print("-" * 90)

    # Step 7: Feature Importance for all models
    print("Feature Importance...".center(90))
    for model_name, model in models.items():
        Feature_Importance(model, df.columns[:-1], model_name)
        print(f"{model_name} is trained and feature importance is calculated")
    print("-" * 90)

    # Step 8: Additional Insights
    print("Correlation Heatmap...".center(90))
    Plot_Correlation(df)
    print("Comparing Model Accuracies...".center(90))
    Compare_Model_Accuracies(models, X_test, y_test)
    print("-" * 90)

    # Step 9: Predict With User Input
    print("Predicting with User Input...".center(90))
    feature_names = df.columns[:-1]
    Predict_With_User_Input(models['Gradient Boosting'], feature_names)
    print("-" * 90)

########################################################
# Run Main
########################################################

if __name__ == "__main__":
    main()
