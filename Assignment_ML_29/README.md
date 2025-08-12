# 🩺 Diabetes Prediction Using Machine Learning  

---

### 📊 Project Overview  
**Title:** Diabetes Prediction Using Machine Learning  
**Objective:** Predict whether a patient is diabetic (`1`) or not (`0`) based on medical attributes using multiple machine learning algorithms.  

---

### 🧠 Key Features  
- **Dataset:** PIMA Indians Diabetes dataset (`diabetes.csv`).  
- **EDA:** Display dataset summary, statistics, missing values, and correlation; visualize distributions, boxplots, and pairplots.  
- **Preprocessing:**  
  - Replace zero values in key columns with `NaN` and fill with mean values.  
  - Feature scaling using `StandardScaler`.  
  - Split dataset into features and target.  
- **Models:**  
  - Logistic Regression  
  - K-Nearest Neighbors (KNN)  
  - Decision Tree  
- **Evaluation:** Accuracy, confusion matrix (visualized), precision, recall, and F1 score.  
- **Predictions:**  
  - Predict from user input and save result to `DiabetesPrediction.csv`.  
  - Predict on test set and save results to `TestPredictions.csv`.  

---

### 🧰 Dependencies  
Install required packages:  
```bash
pip install pandas numpy seaborn matplotlib scikit-learn
```  

---

### 📁 Dataset Details  
**Source:** PIMA Indians Diabetes Dataset (`diabetes.csv`)  
**Key Features:**  

- `Pregnancies` (Number of pregnancies)  
- `Glucose` (Plasma glucose concentration)  
- `BloodPressure` (Diastolic blood pressure)  
- `SkinThickness` (Triceps skin fold thickness)  
- `Insulin` (2-Hour serum insulin)  
- `BMI` (Body mass index)  
- `DiabetesPedigreeFunction` (Diabetes pedigree function)  
- `Age` (Age in years)  
- `Outcome` (Target: 1 for diabetic, 0 for not diabetic)  

---

## 📂 Workflow  

1. **Load Dataset**  
   Load `diabetes.csv` from the working directory.  

2. **Display Data Summary**  
   Show head, info, statistics, shape, correlation, and missing values.  

3. **Visualize Data**  
   Plot distribution of target variable, feature histograms, boxplots, and pairplots.  

4. **Preprocess Data**  
   Replace invalid zero values, fill missing data, scale features with `StandardScaler`.  

5. **Train Models**  
   Train Logistic Regression, KNN, and Decision Tree models using an 80–20 train-test split.  

6. **Evaluate Models**  
   Calculate and display accuracy, confusion matrix (heatmap), and classification report for each model.  

7. **Save Test Predictions**  
   Predict on the test dataset with Logistic Regression and save to `TestPredictions.csv`.  

8. **User Input Prediction**  
   Take patient details as input, predict diabetes status, and save to `DiabetesPrediction.csv`.  

---

## 🚀 Running the Project  

1. Place `diabetes.csv` in your working directory.  
2. Run the script:  

```bash
python diabetes_prediction.py
```  

3. Follow on-screen prompts to view EDA, model evaluation, and enter patient details for prediction.  

---

## 📊 Example Output  

```
Logistic Regression
Accuracy: 0.792
Confusion Matrix:
[[87 13]
 [19 35]]
Classification Report:
              precision    recall  f1-score   support
           0       0.82      0.87      0.85       100
           1       0.73      0.65      0.69        54
------------------------------------------------------------------------------------------
Prediction: The patient is likely :- Diabetic.
Prediction saved to 'DiabetesPrediction.csv'.
Test predictions saved to 'TestPredictions.csv'.
------------------------------------------------------------------------------------------
```  

---

## 📜 Author  
* Name: Rohit Pawar  
* Date: 24-07-2025  
