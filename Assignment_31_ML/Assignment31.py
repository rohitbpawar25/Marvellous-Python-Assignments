########################################################
# Required Python Packages
########################################################

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, confusion_matrix, classification_report,
    roc_auc_score, roc_curve
)

########################################################
# File Paths
########################################################

INPUT_PATH = load_breast_cancer()  # Make sure this file exists in the same folder

########################################################
# Load Data
# Input: Filepath (str): Path to the CSV file
# Output: df (DataFrame): Loaded dataset
########################################################

def Load_Data(Filepath):
    
    data = Filepath # Load the breast cancer dataset directly since it's a predefined dataset in sklearn
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
#   X_scaled: Scaled feature set
#   Y: Target values
#   scaler: Fitted StandardScaler object
########################################################

def PreProcess_Data(df):

    X = df.drop(columns='target')  # Extract features (excluding target column)
    Y = df['target']  # Extract target column
    
    scaler = StandardScaler()  # Initialize the StandardScaler and scale the features
    X_scaled = scaler.fit_transform(X)
    
    return X_scaled, Y, scaler  # Return the scaled features, target, and the fitted scaler object

########################################################
# Train Model
# Input:
#   X_train (ndarray): Scaled training features
#   X_test (ndarray): Scaled test features
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

    for name, model in models.items():
        print("-" * 90)
        print(f"{name} model in testing..".center(90))
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        print(f"Accuracy {name} is : {acc*100:.2f}")
        print("Confusion Matrix for {name}:\n", confusion_matrix(y_test, y_pred))
        print("\nClassification Report:\n", classification_report(y_test, y_pred))

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
#   model (sklearn model): Trained model (e.g., Decision Tree, Random Forest, or Gradient Boosting)
#   feature_names (list): List of feature names (e.g., columns in the dataset excluding the target)
#   model_name (str): The name of the model used for plotting (e.g., 'Decision Tree', 'Random Forest')
# Output:
#   None: Displays a bar plot of the top 10 most important features for the given model
########################################################

def Feature_Importance(model, feature_names, model_name):
    if hasattr(model, 'feature_importances_'):  # Check if the model has the feature_importances_ attribute
        importances = model.feature_importances_
        indices = importances.argsort()[::-1]  # Sort the feature importances in descending order

        # Plot the top 10 important features
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
#   model (sklearn model): A trained classifier (e.g., Decision Tree, Random Forest, Gradient Boosting)
#   scaler (StandardScaler): Scaler object used to scale the features during training
#   feature_names (list): List of feature names in the dataset
# Output:
#   None: Prints the prediction result based on the user input
########################################################

def Predict_With_User_Input(model, scaler, feature_names):
    # Prompting the user to enter values for each feature
    print("\nEnter values for the following 30 features (numerical only):")
    user_input = []

    # Loop through each feature and request input from the user
    for feature in feature_names:
        val = float(input(f"{feature}: "))  # Convert input to float for numerical features
        user_input.append(val)  # Append the value to the user input list

    # Convert user input into a DataFrame (with feature names)
    user_input_df = pd.DataFrame([user_input], columns=feature_names)

    # Scale the input features using the same scaler used for training
    input_scaled = scaler.transform(user_input_df)  # Scaling the input

    # Predicting the class using the trained model
    prediction = model.predict(input_scaled)[0]  # Predict class (0 or 1)

    # Interpret the prediction: 0 -> Malignant, 1 -> Benign
    result = "Malignant (Cancerous)" if prediction == 0 else "Benign (Non-cancerous)"

    # Print the prediction result
    print(f"\nPrediction: {result}")


########################################################
# Main Execution 
# Case Study : Breast Cancer Classification Using Decision Trees,Random Forest, and Gradient Boosting
# Author: Rohit Pawar
# Date: 28-07-2025
########################################################

def main():
    print("-" * 90)
    print("Case Study : Breast Cancer Classification Using Decision Trees,Random Forest, and Gradient Boosting".center(90))
    print("Author: Rohit Pawar".center(90))
    print("Date: 28-07-2025".center(90))
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
    X_scaled, Y, scaler = PreProcess_Data(df)
    print("-" * 90)

    # Step 4: Train-Test Split
    print("Splitting Data into Train and Test...".center(90))
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, Y, test_size=0.3, random_state=42)

    # Step 5: Training Model
    print("Training Model...".center(90))
    models = Train_Test(X_train, X_test, y_train, y_test)
    print("-" * 90)

    # Step 6: Feature Importance for all models
    print("Feature Importance...".center(90))
    for model_name, model in models.items():
        Feature_Importance(model, df.columns[:-1], model_name)  # Display feature importance for all models
        print(f"{model_name} is trained and feature importance is calculated")
    print("-" * 90)

    # Step 7: Predict With User Input
    print("Predicting with User Input...".center(90))
    feature_names = df.columns[:-1]
    Predict_With_User_Input(models['Gradient Boosting'], scaler, feature_names)  # Predict with Gradient Boosting (or any model)
    print("-" * 90)

########################################################
# Run Main
########################################################

if __name__ == "__main__":
    main()
