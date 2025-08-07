# Case study On Breast Cancer Prediction

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier, VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, confusion_matrix, classification_report,
    roc_auc_score, roc_curve
)


def LoadData():
    data = load_breast_cancer()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    print("DataSet Loaded Successfully..".center(90))
    print("-" * 90)
    return df, data


def DisplayData(df):
    print("First 5 rows:\n", df.head())
    print("-" * 90)
    print("Data Types:\n", df.dtypes)
    print("-" * 90)
    print("Summary Statistics:\n", df.describe())
    print("-" * 90)
    print("Missing values per column:\n", df.isnull().sum())
    print("-" * 90)


def PreprocessData(data):
    print("Data Scaling using StandardScaler...".center(90))
    X = data.data
    y = data.target
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, y, scaler


def TrainAndEvaluateModels(X_train, X_test, y_train, y_test):
    models = {
        "Decision Tree": DecisionTreeClassifier(max_depth=7),
        "Random Forest": RandomForestClassifier(max_depth=7),
        "Gradient Boosting": GradientBoostingClassifier()
    }

    for name, model in models.items():
        print(f"\n{name} model in testing".center(90))
        print("-" * 90)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        print(f"Accuracy: {acc*100:.4f}")
        print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
        print("Classification Report:\n", classification_report(y_test, y_pred))

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


def TrainVotingClassifier(X_train, X_test, y_train, y_test, models):
    voting_model = VotingClassifier(
        estimators=[
            ("Decision Tree", models["Decision Tree"]),
            ("Random Forest", models["Random Forest"]),
            ("Gradient Boosting", models["Gradient Boosting"])
        ],
        voting="hard"
    )

    print("\nVoting Classifier Evaluation".center(90))
    print("-" * 90)
    voting_model.fit(X_train, y_train)
    y_pred = voting_model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy Of Voting Model: {acc*100:.4f}")
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))
    
    return voting_model


def PlotFeatureImportance(model, feature_names, model_name):
    if hasattr(model, 'feature_importances_'):
        importances = model.feature_importances_
        indices = importances.argsort()[::-1]

        plt.figure(figsize=(10, 6))
        plt.title(f"{model_name} - Top 10 Feature Importances")
        plt.bar(range(10), importances[indices[:10]], align='center')
        plt.xticks(range(10), [feature_names[i] for i in indices[:10]], rotation=45)
        plt.tight_layout()
        plt.grid(True)
        plt.show()


def PredictWithUserInput(model, scaler, feature_names):
    print("\nEnter values for the following 30 features (numerical only):")
    user_input = []
    for feature in feature_names:
        val = float(input(f"{feature}: "))
        user_input.append(val)

    input_scaled = scaler.transform([user_input])
    prediction = model.predict(input_scaled)[0]
    result = "Malignant (Cancerous)" if prediction == 0 else "Benign (Non-cancerous)"
    print(f"\nPrediction: {result}")


def main():
    print("-" * 90)
    print("Breast Cancer Prediction Case Study".center(90))
    print("-" * 90)

    df, data = LoadData()
    DisplayData(df)
    X_scaled, y, scaler = PreprocessData(data)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42)

    models = TrainAndEvaluateModels(X_train, X_test, y_train, y_test)

    voting_model = TrainVotingClassifier(X_train, X_test, y_train, y_test, models)

    PlotFeatureImportance(models["Random Forest"], data.feature_names, "Random Forest")
    PlotFeatureImportance(models["Gradient Boosting"], data.feature_names, "Gradient Boosting")

    PredictWithUserInput(voting_model, scaler, data.feature_names)


if __name__ == "__main__":
    main()
