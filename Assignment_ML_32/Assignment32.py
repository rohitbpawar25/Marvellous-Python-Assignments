########################################################
# Required Python Packages
########################################################

import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from sklearn.ensemble import VotingClassifier

########################################################
# File Paths
########################################################

INPUT_PATH_1 = "True.csv"
INPUT_PATH_2 = "Fake.csv"

########################################################
# Load Data
# Input:
#   FakeData (str): File path to the CSV containing fake news
#   RealData (str): File path to the CSV containing real news
# Output:
#   dfFake (DataFrame): Fake news dataset
#   dfReal (DataFrame): Real news dataset
########################################################

def Load_Data(FakeData, RealData):
    dfFake = pd.read_csv(FakeData)
    dfReal = pd.read_csv(RealData)
    return dfFake, dfReal

########################################################
# Display Data
# Input:
#   dfFake (DataFrame): Fake news dataset
#   dfReal (DataFrame): Real news dataset
# Output:
#   None: Prints dataset info and plots class distribution
########################################################

def DisplayData(dfFake, dfReal):
    print("Fake News Sample\n".center(90))
    print(dfFake.head(), "\n")
    print("-"*90)
    print("Real News Sample\n".center(90))
    print(dfReal.head(), "\n")
    print("-"*90)
    print(f"Fake News Count: {len(dfFake)}")
    print("-"*90)
    print(f"Real News Count: {len(dfReal)}")
    
    # Plot bar chart of class distribution
    plt.bar(["Fake News", "Real News"], [len(dfFake), len(dfReal)], color=["red", "green"])
    plt.title("Class Distribution")
    plt.ylabel("Number of Articles")
    plt.show()

########################################################
# Preprocess Data (with Vectorization)
# Input:
#   dfFake (DataFrame): Fake news dataset
#   dfReal (DataFrame): Real news dataset
# Output:
#   dfConcat (DataFrame): Combined dataset with labels
#   X_vectorized (matrix): TF-IDF transformed text features
#   vectorizer (TfidfVectorizer): Fitted vectorizer object
########################################################

def PreprocessData(dfFake, dfReal):
    dfFake['label'] = 0
    dfReal['label'] = 1
    dfConcat = pd.concat([dfFake, dfReal], ignore_index=True)

    vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
    X_vectorized = vectorizer.fit_transform(dfConcat['text'])
    return dfConcat, X_vectorized, vectorizer

########################################################
# Split Dataset
# Input:
#   X (matrix): Feature matrix
#   y (Series): Target labels
#   train_percentage (float): Proportion of training data
#   random_state (int): Seed for reproducibility
# Output:
#   X_train, X_test, Y_train, Y_test: Split datasets
########################################################

def split_dataset(X, y, train_percentage, random_state=42):
    return train_test_split(
        X, y,
        train_size=train_percentage, random_state=random_state
    )

########################################################
# Train Models
# Input:
#   X_train (matrix): Training features
#   Y_train (Series): Training labels
# Output:
#   Models (dict): Dictionary containing trained models
########################################################

def TrainModel(X_train, Y_train):
    Models = {
        "LogisticRegression": LogisticRegression(),
        "DecisionTreeClassifier": DecisionTreeClassifier(),
    }
    for name, model in Models.items():
        model.fit(X_train, Y_train)
        print(f"Model {name} Trained Successfully".center(90))
    return Models

########################################################
# Evaluate Models
# Input:
#   models (dict): Trained models
#   X_train, Y_train, X_test, Y_test: Train/test sets
# Output:
#   None: Prints accuracy and plots confusion matrix
########################################################

def EvaluateModels(models, X_train, Y_train, X_test, Y_test):
    for name, model in models.items():
        train_predictions = model.predict(X_train)
        test_predictions = model.predict(X_test)

        print(f"{name} Training Accuracy: {accuracy_score(Y_train, train_predictions) * 100:.4f}%")
        print(f"{name} Testing Accuracy : {accuracy_score(Y_test, test_predictions) * 100:.4f}%")

        cm = confusion_matrix(Y_test, test_predictions)
        ConfusionMatrixDisplay(cm).plot()
        plt.title(f"Confusion Matrix - {name}")
        plt.show()

########################################################
# Voting Classifier
# Input:
#   models (dict): Trained base models
#   X_train, Y_train, X_test, Y_test: Train/test sets
# Output:
#   voting_clf (VotingClassifier): Trained ensemble model
########################################################

def VotingModel(models, X_train, Y_train, X_test, Y_test):
    voting_clf = VotingClassifier(
        estimators=[(name, model) for name, model in models.items()],
        voting='hard'
    )
    voting_clf.fit(X_train, Y_train)

    train_predictions = voting_clf.predict(X_train)
    test_predictions = voting_clf.predict(X_test)

    print(f"Voting Classifier Training Accuracy: {accuracy_score(Y_train, train_predictions) * 100:.4f}%")
    print(f"Voting Classifier Testing Accuracy : {accuracy_score(Y_test, test_predictions) * 100:.4f}%")

    cm = confusion_matrix(Y_test, test_predictions)
    ConfusionMatrixDisplay(cm).plot()
    plt.title("Confusion Matrix - Voting Classifier")
    plt.show()

    return voting_clf

########################################################
# Predict With User Input
# Input:
#   vectorizer (TfidfVectorizer): Fitted vectorizer for text data
#   model (sklearn model): Trained classification model
# Output:
#   None: Takes user input and prints prediction
########################################################

def PredictSingleNews(vectorizer, model):
    while True:
        text = input("\nEnter a news article (or type 'exit' to quit): ")
        if text.lower() == 'exit':
            break
        text_vectorized = vectorizer.transform([text])
        prediction = model.predict(text_vectorized)[0]
        if prediction == 0:
            print("Prediction: FAKE NEWS ❌")
        else:
            print("Prediction: REAL NEWS ✅")

########################################################
# Main execution
# Case Study : Predict Whether A News Article Is Fake Or Real Using Text 
# Author: Rohit Pawar
# Date: 28-07-2025
########################################################

def main():
    print("-"*90)
    print("Predict Whether A News Article Is Fake Or Real Using Text".center(90))
    print("Author: Rohit Pawar".center(90))
    print("Date: 28-07-2025".center(90))
    print("-"*90)

    # Step 1: Load dataset
    print("Data Loaded Successfully..".center(90))
    dfFake, dfReal = Load_Data(INPUT_PATH_1, INPUT_PATH_2)
    print("-"*90)

    # Step 2: Display data
    print("Data Preview..\n".center(90))
    DisplayData(dfFake, dfReal)
    print("-"*90)

    # Step 3: Preprocess + Vectorize
    print("Data Preprocessed & Vectorized Successfully..".center(90))
    df, X_vectorized, vectorizer = PreprocessData(dfFake, dfReal)
    print("-"*90)

    # Step 4: Split
    print("Data Split Successfully..".center(90))
    X_train, X_test, Y_train, Y_test = split_dataset(
        X_vectorized, df['label'], train_percentage=0.8
    )
    print("-"*90)

    # Step 5: Train Models
    print("Models Trained Successfully..".center(90))
    models = TrainModel(X_train, Y_train)
    print("-"*90)

    # Step 6: Evaluate Models
    print("Models Evaluated Successfully..".center(90))
    EvaluateModels(models, X_train, Y_train, X_test, Y_test)
    print("-"*90)

    # Step 7: Voting Classifier
    print("Voting Classifier Trained Successfully..".center(90))
    voting_model = VotingModel(models, X_train, Y_train, X_test, Y_test)
    print("-"*90)

    # Step 8: User Prediction Input
    print("User Prediction Input..".center(90))
    PredictSingleNews(vectorizer, voting_model)
    print("-"*90)

########################################################
# Run Main
########################################################

if __name__ == "__main__":
    main()
