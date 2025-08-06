import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve

def LoadData(FilePath):
    print("Load Data Successfully..".center(90))
    df = pd.read_csv(FilePath, sep=";")
    df.to_csv("NewBank.csv", index=False)
    print("DataSet Change And Save Successfully..".center(90))
    print("-"*90)
    return df

def NewData(NewPath):
    df = pd.read_csv(NewPath)
    print("New Data Loaded Successfully..".center(90))
    print("-"*90)
    return df

def ExploreData(df):
    print("First 5 rows:\n", df.head())
    print("-"*90)
    print("Last 5 rows:\n", df.tail())
    print("-"*90)
    print("Data Types:\n", df.dtypes)
    print("-"*90)
    print("Summary Statistics:\n", df.describe(include='all'))
    print("-"*90)
    print(f"Shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    print("-"*90)
    print("Missing values per column:\n", df.isnull().sum())
    print("-"*90)

    unknown_counts = (df == 'unknown').sum()
    print("Counts of 'unknown' values in categorical columns:\n", unknown_counts[unknown_counts > 0])
    print("-"*90)

def VisualizeData(df):
    plt.figure(figsize=(8,5))
    sns.countplot(x='y', data=df)
    plt.title('Target Variable Distribution')
    plt.show()
    print("-"*90)

    df.hist(figsize=(12,10))
    plt.suptitle('Feature Distributions')
    plt.show()
    print("-"*90)

def PreprocessData(df):
    df.replace('unknown', np.nan, inplace=True)
    for col in df.columns:
        if df[col].dtype == object:
            df[col].fillna(df[col].mode()[0], inplace=True)

    binary_cols = ['default', 'housing', 'loan', 'y']
    le = LabelEncoder()
    for col in binary_cols:
        df[col] = le.fit_transform(df[col])

    df.drop(columns=['contact', 'day', 'month', 'pdays', 'previous', 'marital', 'poutcome'], inplace=True)

    df = pd.get_dummies(df, columns=['job', 'education'], drop_first=True)

    X = df.drop('y', axis=1)
    y = df['y']

    numeric_cols = ['age', 'balance', 'duration', 'campaign']
    scaler = StandardScaler()
    X[numeric_cols] = scaler.fit_transform(X[numeric_cols])

    print("Data Preprocessing Completed.".center(90))
    print("-"*90)
    return X, y, scaler, X.columns

def TrainAndEvaluateModels(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    models = {
        'Logistic Regression': LogisticRegression(max_iter=1000),
        'K-Nearest Neighbors': KNeighborsClassifier(),
        'Random Forest': RandomForestClassifier(random_state=42)
    }

    for name, model in models.items():
        print(f"{name} model in testing".center(90))
        print("-"*90)

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        print(f"Accuracy: {acc:.4f}\n")
        print("Confusion Matrix:")
        print(confusion_matrix(y_test, y_pred))
        print("Classification Report:")
        print(classification_report(y_test, y_pred))

        if hasattr(model, 'predict_proba'):
            y_prob = model.predict_proba(X_test)[:,1]
            roc_auc = roc_auc_score(y_test, y_prob)
            fpr, tpr, _ = roc_curve(y_test, y_prob)

            plt.figure()
            plt.plot(fpr, tpr, label=f'{name} (AUC = {roc_auc:.2f})')
            plt.plot([0,1], [0,1], 'k--')
            plt.title(f'{name} - ROC Curve')
            plt.xlabel('False Positive Rate')
            plt.ylabel('True Positive Rate')
            plt.legend(loc='lower right')
            plt.grid(True)
            plt.show()

        print("-"*90)

    return models, X.columns

def PredictFromUserInput(models, scaler, X_columns):
    print("\nEnter customer details for prediction:")

    age = int(input("Age: "))
    job = input("Job (e.g., admin., technician, management, etc.): ").strip()
    education = input("Education (primary, secondary, tertiary): ").strip()
    default = input("Has credit in default? (yes/no): ").lower()
    balance = float(input("Average yearly balance: "))
    housing = input("Has housing loan? (yes/no): ").lower()
    loan = input("Has personal loan? (yes/no): ").lower()
    duration = float(input("Last contact duration (seconds): "))
    campaign = int(input("Number of contacts during campaign: "))

    input_dict = {
        'age': age,
        'balance': balance,
        'duration': duration,
        'campaign': campaign,
        'default': 1 if default == 'yes' else 0,
        'housing': 1 if housing == 'yes' else 0,
        'loan': 1 if loan == 'yes' else 0
    }

    job_col = 'job_' + job
    if job_col in X_columns:
        input_dict[job_col] = 1

    edu_col = 'education_' + education
    if edu_col in X_columns:
        input_dict[edu_col] = 1

    input_df = pd.DataFrame([input_dict])
    input_df = input_df.reindex(columns=X_columns, fill_value=0)

    numeric_cols = ['age', 'balance', 'duration', 'campaign']
    input_df[numeric_cols] = scaler.transform(input_df[numeric_cols])

    for name, model in models.items():
        pred = model.predict(input_df)[0]
        result = "Subscribed" if pred == 1 else "Not Subscribed"
        print("-"*90)
        print(f"{name} prediction: The customer is likely to be: {result}")
        print("-"*90)

def main():
    print("-"*90)
    print("Bank Term Deposit Subscription Prediction".center(90))
    print("-"*90)

    FilePath = "Bank.csv"
    df = LoadData(FilePath)

    NewPath = "NewBank.csv"
    df = NewData(NewPath)

    ExploreData(df)
    VisualizeData(df)

    X, y, scaler, X_columns = PreprocessData(df)

    models, X_columns = TrainAndEvaluateModels(X, y)

    PredictFromUserInput(models, scaler, X_columns)

if __name__ == "__main__":
    main()
