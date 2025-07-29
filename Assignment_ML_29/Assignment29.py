# Case Study on Diabetes Prediction

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

# 1. Load Data
def LoadData(Data):
    df = pd.read_csv(Data)
    print("-" * 90)
    return df

# 2. Display Data
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
    print("-" * 90)

# 3. Visualize Data
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

# 4. Preprocess Data
def PreprocessData(df):
    cols_with_zero = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    df[cols_with_zero] = df[cols_with_zero].replace(0, np.nan)
    df.fillna(df.mean(), inplace=True)

    X = df.drop('Outcome', axis=1)
    Y = df['Outcome']

    X_array = X.values
    Scaler = StandardScaler()
    X_Scaled = Scaler.fit_transform(X_array)

    return X_Scaled, Y, Scaler

# 5. Train Models
def TrainModels(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    models = {
        'Logistic Regression': LogisticRegression(),
        'KNN': KNeighborsClassifier(),
        'Decision Tree': DecisionTreeClassifier()
    }

    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        print(f"\n{name}")
        print("Accuracy:", accuracy_score(y_test, y_pred))
        print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
        print("Classification Report:\n", classification_report(y_test, y_pred))

        sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
        plt.title(f"{name} - Confusion Matrix")
        plt.show()

    return models['Logistic Regression']

# 6. Predict from User Input and Save
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

    output_df.to_csv('DiabetesPrediction.csv', index=False)
    print("\nPrediction saved to 'DiabetesPrediction.csv'.")
    print("Sample Output:\n", output_df)

# 7. Main Function
def main():
    Filepath = "diabetes.csv"
    df = LoadData(Filepath)
    DisplayData(df)
    VisualizeData(df)
    X_Scaled, Y, Scaler = PreprocessData(df)
    model = TrainModels(X_Scaled, Y)
    PredictFromUserInput(model, Scaler)

if __name__ == "__main__":
    main()
