########################################################
# Required Python Packages
########################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import (
    accuracy_score, confusion_matrix, roc_curve, auc, classification_report
)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
import joblib

########################################################
# File Paths
########################################################
INPUT_PATH = "breast-cancer-wisconsin.data"
OUTPUT_PATH = "breast-cancer-wisconsin.csv"
MODEL_PATH = "bc_rf_pipeline.joblib"

########################################################
# Headers
########################################################
HEADERS = [
    "CodeNumber", "ClumpThickness", "UniformityCellSize", "UniformityCellShape",
    "MarginalAdhesion", "SingleEpithelialCellSize", "BareNuclei", "BlandChromatin",
    "NormalNucleoli", "Mitoses", "CancerType"
]

########################################################
# Read raw data
########################################################
def read_data(path):
    """Read the data into pandas dataframe"""
    return pd.read_csv(path, header=None)

########################################################
# Add headers to dataset
########################################################
def add_headers(dataset, headers):
    """Add headers to dataset"""
    dataset.columns = headers
    return dataset

########################################################
# Convert .data to .csv
########################################################
def data_file_to_csv():
    """Convert raw .data file to CSV with headers"""
    dataset = read_data(INPUT_PATH)
    dataset = add_headers(dataset, HEADERS)
    dataset.to_csv(OUTPUT_PATH, index=False)
    print("File saved ...!")

########################################################
# Handle missing values
########################################################
def handle_missing_values_with_imputer(df, feature_headers):
    """Replace '?' with NaN and convert to numeric"""
    df = df.replace('?', np.nan)
    df[feature_headers] = df[feature_headers].apply(pd.to_numeric, errors='coerce')
    return df

########################################################
# Split dataset
########################################################
def split_dataset(dataset, train_percentage, feature_headers, target_header, random_state=42):
    """Split dataset into train/test"""
    return train_test_split(
        dataset[feature_headers], dataset[target_header],
        train_size=train_percentage, random_state=random_state,
        stratify=dataset[target_header]
    )

########################################################
# Display dataset statistics
########################################################
def dataset_statistics(dataset):
    """Print basic stats"""
    print(dataset.describe(include='all'))

########################################################
# Build ML pipeline
########################################################
def build_pipeline():
    """Create pipeline with imputer and RandomForest"""
    return Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("rf", RandomForestClassifier(n_estimators=300, random_state=42, n_jobs=-1))
    ])

########################################################
# Train pipeline
########################################################
def train_pipeline(pipeline, X_train, y_train):
    """Train pipeline"""
    pipeline.fit(X_train, y_train)
    return pipeline

########################################################
# Save model
########################################################
def save_model(model, path=MODEL_PATH):
    """Save trained model"""
    joblib.dump(model, path)
    print(f"Model saved to {path}")

########################################################
# Load model
########################################################
def load_model(path=MODEL_PATH):
    """Load trained model"""
    model = joblib.load(path)
    print(f"Model loaded from {path}")
    return model

########################################################
# Plot confusion matrix
########################################################
def plot_confusion_matrix_matshow(y_true, y_pred, title="Confusion Matrix"):
    """Visualize confusion matrix"""
    cm = confusion_matrix(y_true, y_pred)
    fig, ax = plt.subplots()
    cax = ax.matshow(cm)
    fig.colorbar(cax)
    for (i, j), v in np.ndenumerate(cm):
        ax.text(j, i, str(v), ha='center', va='center')
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    ax.set_title(title)
    plt.tight_layout()
    plt.show()

########################################################
# Plot feature importances
########################################################
def plot_feature_importances(model, feature_names, title="Feature Importances (Random Forest)"):
    """Visualize feature importances"""
    if hasattr(model, "named_steps") and "rf" in model.named_steps:
        rf = model.named_steps["rf"]
        importances = rf.feature_importances_
    elif hasattr(model, "feature_importances_"):
        importances = model.feature_importances_
    else:
        print("Feature importances not available.")
        return
    idx = np.argsort(importances)[::-1]
    plt.figure(figsize=(8, 4))
    plt.bar(range(len(importances)), importances[idx])
    plt.xticks(range(len(importances)), [feature_names[i] for i in idx], rotation=45, ha='right')
    plt.ylabel("Importance")
    plt.title(title)
    plt.tight_layout()
    plt.show()

########################################################
# Main execution
########################################################
def main():
    # Step 1: Convert raw file to CSV (run once)
    # data_file_to_csv()

    # Step 2: Load dataset
    dataset = pd.read_csv(OUTPUT_PATH)

    # Step 3: Show stats
    dataset_statistics(dataset)

    # Step 4: Prepare features and target
    feature_headers = HEADERS[1:-1]
    target_header = HEADERS[-1]

    # Step 5: Handle missing values
    dataset = handle_missing_values_with_imputer(dataset, feature_headers)

    # Step 6: Split data
    train_x, test_x, train_y, test_y = split_dataset(dataset, 0.7, feature_headers, target_header)
    print("Train/Test shapes:", train_x.shape, test_x.shape)

    # Step 7: Build and train model
    pipeline = build_pipeline()
    trained_model = train_pipeline(pipeline, train_x, train_y)

    # Step 8: Evaluate
    predictions = trained_model.predict(test_x)
    print("Train Accuracy:", accuracy_score(train_y, trained_model.predict(train_x)))
    print("Test Accuracy:", accuracy_score(test_y, predictions))
    print("Classification Report:\n", classification_report(test_y, predictions))
    print("Confusion Matrix:\n", confusion_matrix(test_y, predictions))

    # Step 9: Visuals
    plot_confusion_matrix_matshow(test_y, predictions)
    plot_feature_importances(trained_model, feature_headers)

    # Step 10: Save model
    save_model(trained_model)

    # Step 11: Load model and test sample
    loaded = load_model()
    sample = test_x.iloc[[0]]
    print("Sample prediction:", loaded.predict(sample)[0])

########################################################
# Application starter
########################################################
if __name__ == "__main__":
    main()
