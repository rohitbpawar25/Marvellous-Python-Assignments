# PlayPredictor Case Study

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

def LoadData(filepath):
    print("-" * 90)
    df = pd.read_csv(filepath)
    print("Data Loaded Successfully:")
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
    print("-" * 90)
    print("Before Drop:\n", df.head())

    # Drop unwanted columns
    df = df.drop(columns=['Unnamed: 0'], errors='ignore')

    # Rename column if typo exists
    df.rename(columns={'Whether': 'Weather'}, inplace=True)

    print("After Drop and Rename:\n", df.head())
    print("-" * 90)

    # Label Encoding
    WeatherEN = LabelEncoder()
    TemperatureEN = LabelEncoder()
    PlayEN = LabelEncoder()

    df['Weather'] = WeatherEN.fit_transform(df['Weather'])
    df['Temperature'] = TemperatureEN.fit_transform(df['Temperature'])
    df['Play'] = PlayEN.fit_transform(df['Play'])

    print("After Encoding:\n", df.head())
    print("-" * 90)

    return df, WeatherEN, TemperatureEN, PlayEN

def TrainModel(df, K=3):
    print("-" * 90)
    X = df[['Weather', 'Temperature']]
    Y = df['Play']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2,random_state=42)
    model = KNeighborsClassifier(n_neighbors=K)
    model.fit(X_train, Y_train)
    print("Model Trained on full dataset")
    print("-" * 90) 
    return model

def TestModel(model, weather_enc, temperature_enc, PlayEN):
    print("-" * 90)
    predicted = model.predict([[weather_enc, temperature_enc]])
    result = PlayEN.inverse_transform(predicted)[0]
    print(f"Predicted Result: {result}")
    print("-" * 90)
    return result

def CheckAccuracy(df, MaxK=10):
    print("Checking Accuracy for Different K Values")
    X = df[['Weather', 'Temperature']]
    Y = df['Play']

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    accuracies = []

    for k in range(1, MaxK + 1):
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        accuracies.append(acc)
        print(f"K={k} → Accuracy: {acc:.2f}")

    plt.figure(figsize=(8, 5))
    plt.plot(range(1, MaxK + 1), accuracies, marker='o', linestyle='--', color='blue')
    plt.title("Accuracy vs K")
    plt.xlabel("K Value")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.show()

    return y_test, y_pred

def ConfusionMatrix(y_test, y_pred):
    print("-" * 90)
    print("Confusion Matrix")
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, cmap="Blues", fmt='d')
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    plt.show()
    print("-" * 90)
    return cm

def main():
    filepath = "PlayPredictor.csv"  # Ensure file is in the same folder
    df = LoadData(filepath)
    DisplayData(df)
    df, WeatherEN, TemperatureEN, PlayEN = PreprocessData(df)

    model = TrainModel(df, K=3)

    print(f"Possible Weather values: {list(WeatherEN.classes_)}")
    weather_input = input("Enter Weather: ").strip()

    print(f"Possible Temperature values: {list(TemperatureEN.classes_)}")
    temperature_input = input("Enter Temperature: ").strip()

    
    weather_enc = WeatherEN.transform([weather_input])[0]
    temperature_enc = TemperatureEN.transform([temperature_input])[0]

    TestModel(model, weather_enc, temperature_enc, PlayEN)

    y_test, y_pred = CheckAccuracy(df, MaxK=10)
    ConfusionMatrix(y_test, y_pred)

if __name__ == "__main__":
    main()
