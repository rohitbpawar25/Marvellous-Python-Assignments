# 🏦 Bank Term Deposit Subscription Prediction using Logistic Regression, KNN & Random Forest

---

### 📊 Project Overview  
**Title:** Bank Term Deposit Subscription Prediction  
**Objective:** Predict whether a customer will subscribe to a term deposit based on personal, financial, and campaign-related attributes.  

---

### 🧠 Key Features  
- **Industrial Format:** Well-structured for GitHub portfolio, resume, and academic submission.  
- **Data Preprocessing:** Handles missing values, binary encoding, one-hot encoding, and feature scaling.  
- **Modeling Techniques:** Logistic Regression, K-Nearest Neighbors (KNN), and Random Forest Classifier.  
- **Evaluation:** Accuracy score, classification report, confusion matrix, and ROC curves.  
- **Feature Importance:** Plots top features influencing predictions.  
- **Interactive CLI:** Accepts user input to predict subscription status.  

---

### 🧰 Dependencies  
Install required packages:  
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

---

### 📁 Dataset Details  
- **Source:** UCI Machine Learning Repository - Bank Marketing Dataset  
- **File Used:** `Bank.csv`  
- **Main Target Variable:** `y`  
  - `0` → Not Subscribed  
  - `1` → Subscribed  

---

## 📂 Workflow  

1. **Data Preparation**  
   - Load dataset from CSV file.  
   - Display samples, dataset shape, null values, and class distribution.  

2. **Data Preprocessing**  
   - Replace `"unknown"` with NaN and forward-fill missing values.  
   - Binary encode `default`, `housing`, and `loan` columns.  
   - One-hot encode categorical variables (job, education, etc.).  
   - Standardize numeric columns (`age`, `balance`, `duration`, `campaign`).  

3. **Train-Test Split**  
   - 80% training data, 20% testing data.  

4. **Model Training**  
   - Logistic Regression  
   - K-Nearest Neighbors (KNN)  
   - Random Forest Classifier  

5. **Model Evaluation**  
   - Accuracy score  
   - Confusion matrix  
   - Classification report  
   - ROC-AUC curve  

6. **Feature Importance**  
   - Plots top 10 most important features for Random Forest.  

7. **User Prediction Mode**  
   - Enter customer details to predict subscription status.  

---

## 📊 Visualizations  
- **Class Distribution** (Bar Chart)  
- **ROC Curves** for each model  
- **Feature Importance** (Bar Chart for Random Forest)  

---

## 🚀 Running the Project  

1. **Prepare your data**  
   Place `Bank.csv` in the same folder as the script.  

2. **Run the script**  
```bash
python bank_term_deposit_prediction.py
```

3. **Follow the steps**  
   - Data loading & visualization  
   - Model training & evaluation  
   - Feature importance analysis  
   - Interactive prediction mode  

---

## 📈 Example Output  

**Class Distribution**  
```
No     : 39922  
Yes    : 5289  
```

**Model Accuracies**  
```
Logistic Regression Accuracy : 90.45%  
KNN Accuracy                 : 88.32%  
Random Forest Accuracy       : 92.76%  
```

**Sample Prediction Output**  
```
Random Forest prediction: The customer is likely to be: Subscribed
```

---

## 📜 Author  
- **Name:** Rohit Pawar  
- **Date:** 2025-08-25  
