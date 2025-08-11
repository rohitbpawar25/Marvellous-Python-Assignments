########################################################
# Required Python Packages
########################################################

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

########################################################
# File Paths
########################################################

INPUT_PATH = "PlayPredictor.csv"  # Make sure this file exists in the same folder

########################################################
# Load Data
# Input: Filepath (str): Path to the CSV file
# Output: df (DataFrame): Loaded dataset
########################################################

def Load_Data(Filepath):
    df = pd.read_csv(Filepath)
    return df

########################################################
# Display Data
# Input: df (DataFrame): Dataset
# Output: None (prints data summary to console)
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
#   df (DataFrame): Encoded dataset
#   WeatherEN (LabelEncoder): Encoder for weather
#   TemperatureEN (LabelEncoder): Encoder for temperature
#   PlayEN (LabelEncoder): Encoder for play
########################################################

def Preprocess_Data(df):
    df = df.drop(columns=['Unnamed: 0'], errors='ignore')  # drop index if exists
    df.rename(columns={'Whether': 'Weather'}, inplace=True)  # rename if misspelled

    WeatherEN = LabelEncoder()
    TemperatureEN = LabelEncoder()
    PlayEN = LabelEncoder()

    df['Weather'] = WeatherEN.fit_transform(df['Weather'])
    df['Temperature'] = TemperatureEN.fit_transform(df['Temperature'])
    df['Play'] = PlayEN.fit_transform(df['Play'])

    return df, WeatherEN, TemperatureEN, PlayEN

########################################################
# Train Model
# Input:
#   df (DataFrame): Preprocessed data
#   K (int): Number of neighbors for KNN
# Output:
#   model (KNN): Trained KNN model
#   X_test (DataFrame): Test features
#   Y_test (Series): Actual labels for test set
########################################################

def Train_Model(df, K=3):
    X = df[['Weather', 'Temperature']]
    Y = df['Play']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = KNeighborsClassifier(n_neighbors=K)
    model.fit(X_train, Y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(Y_test, y_pred)
    print(f"Accuracy of Model with K={K}: {acc:.2f}")

    return model, X_test, Y_test, y_pred

########################################################
# Check Accuracy for multiple K values
# Input:
#   df (DataFrame): Preprocessed dataset
#   MaxK (int): Maximum K value to test
# Output: None
########################################################

def Check_Accuracy(df, MaxK=10):
    X = df[['Weather', 'Temperature']]
    Y = df['Play']

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    accuracies = []
    best_k = 1
    best_accuracy = 0

    for k in range(1, MaxK + 1):
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        accuracies.append(acc)
        
        # Track the best accuracy and corresponding K value
        if acc > best_accuracy:
            best_accuracy = acc
            best_k = k

        print(f"K={k} → Accuracy: {acc:.2f}")

    # Plot the accuracy vs K graph
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, MaxK + 1), accuracies, marker='o', linestyle='--', color='blue')
    plt.title("Accuracy vs K")
    plt.xlabel("K Value")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.show()

    print(f"\nBest Accuracy is {best_accuracy:.2f} at K={best_k}")

    return y_test, y_pred


########################################################
# Test Model with User Input
# Input:
#   model (KNN): Trained model
#   WeatherEN (LabelEncoder): Encoder for weather
#   TemperatureEN (LabelEncoder): Encoder for temperature
#   PlayEN (LabelEncoder): Encoder for play
# Output:
#   result (str): Predicted class label (e.g., "Yes", "No")
########################################################

def TestModel(model, WeatherEN, TemperatureEN, PlayEN):
    print(f"Possible Weather values: {list(WeatherEN.classes_)}")
    weather_input = input("Enter Weather: ").strip()

    print(f"Possible Temperature values: {list(TemperatureEN.classes_)}")
    temperature_input = input("Enter Temperature: ").strip()

    weather_enc = WeatherEN.transform([weather_input])[0]
    temperature_enc = TemperatureEN.transform([temperature_input])[0]

    # Make sure to pass a DataFrame with column names when predicting
    input_data = pd.DataFrame([[weather_enc, temperature_enc]], columns=['Weather', 'Temperature'])
    
    predicted = model.predict(input_data)
    result = PlayEN.inverse_transform(predicted)[0]
    print(f"🎯 Predicted Result: {result}")
    return result


########################################################
# Confusion Matrix
# Input:
#   y_test (array): Actual class labels
#   y_pred (array): Predicted class labels
# Output:
#   cm (2D array): Confusion matrix
########################################################

def ConfusionMatrix(y_test, y_pred):
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, cmap="Blues", fmt='d')
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    plt.show()
    return cm

########################################################
# Main Execution
# Case Study : Predicting Play or Not Based on Weather and Temperature
# Author name : Rohit Pawar
# Date : 19-07-2025
########################################################

def main():
    print("-" * 90)
    print("Case Study On Predicting Play Based on Weather and Temperature".center(90))
    print("-" * 90)

    # Step 1: Load Data
    print("Loading Data...".center(90))
    df = Load_Data(INPUT_PATH)
    print("-" * 90)

    # Step 2: Display Data
    print("Displaying Data...".center(90))
    Display_Data(df)
    print("-" * 90)

    # Step 3: Preprocessing
    print("Preprocessing Data...".center(90))
    df, WeatherEN, TemperatureEN, PlayEN = Preprocess_Data(df)
    print("-" * 90)

    # Step 4: Train Model with a Fixed K Value (K=3)
    print("Training Model with K=3...".center(90))
    model, X_test, Y_test, y_pred = Train_Model(df, K=3)
    print("-" * 90)

    # Step 5: Check Accuracy for Multiple K Values
    print("Checking Accuracy for Different K Values...".center(90))
    Check_Accuracy(df, MaxK=10)
    print("-" * 90)
    
    # Step 6: Predict using User Input
    print("Testing Model with User Input...".center(90))
    TestModel(model, WeatherEN, TemperatureEN, PlayEN)
    print("-" * 90)

    # Step 7: Confusion Matrix
    print("Generating Confusion Matrix...".center(90))
    ConfusionMatrix(Y_test, y_pred)
    print("-" * 90)

########################################################
# Run Main
########################################################

if __name__ == "__main__":
    main()
