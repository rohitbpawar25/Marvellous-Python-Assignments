
# 🍷 Wine Classification using Logistic Regression

---

### 📊 Project Overview
**Title:** Wine Classification using Machine Learning  
**Objective:** Classify wines into three classes based on their chemical analysis using Logistic Regression.

---

### 🧠 Key Features
- **Dataset:** Wine chemical composition dataset with 13 features.  
- **Data Processing:** Data loading, cleaning, and scaling with StandardScaler.  
- **Model:** Logistic Regression for multi-class classification.  
- **Evaluation:** Classification report with accuracy, precision, recall, and F1 score.  
- **Interactive Prediction:** User inputs feature values to predict wine class.

---

### 🧰 Dependencies
Install required packages:
```bash
pip install pandas scikit-learn
```

---

### 📁 Dataset Details
* **Dataset File:** `WinePredictor.csv`  
* **Features:**  
  1. Alcohol  
  2. Malic acid  
  3. Ash  
  4. Alcalinity of ash  
  5. Magnesium  
  6. Total phenols  
  7. Flavanoids  
  8. Nonflavanoid phenols  
  9. Proanthocyanins  
  10. Color intensity  
  11. Hue  
  12. OD280/OD315 of diluted wines  
  13. Proline  
* **Target:** `Class` (Class 1, Class 2, Class 3)

---

## 📂 Workflow

1. **Load Data**  
   Reads the CSV file containing the wine dataset.

2. **Display Data Summary**  
   Shows dataset head, tail, shape, info, description, and missing value checks.

3. **Preprocess Data**  
   Separates features and target, applies feature scaling using StandardScaler.

4. **Train Model**  
   Splits data into train/test sets (80%/20%), trains Logistic Regression.

5. **Evaluate Model**  
   Predicts test set and prints classification report with accuracy and other metrics.

6. **User Input Prediction**  
   Takes new sample input from user, scales it, and predicts wine class.

---

## 🚀 Running the Project
1. Place `WinePredictor.csv` in the same folder as this script.  
2. Run the script:  
```bash
python wine_classification.py
```
3. Follow the prompts to view data summary, evaluation metrics, and input new data for prediction.

---

## 📈 Example Output
```
Classification Report:
              precision    recall  f1-score   support

           1       1.00      1.00      1.00        14
           2       1.00      0.91      0.95        11
           3       0.90      1.00      0.95         9

    accuracy                           0.97        34
   macro avg       0.97      0.97      0.97        34
weighted avg       0.98      0.97      0.97        34

Accuracy: 97.06
Precision: 97.22
Recall: 97.06
F1 Score: 97.00

Enter values for a new wine sample:
Alcohol: 13.0
Malic acid: 2.0
...
Predicted Wine Class: 1
```

---

## 📜 Author
- Name: Rohit Pawar  
- Date: 19-07-2025

---
