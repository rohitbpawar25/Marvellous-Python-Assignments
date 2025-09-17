# 🧠 Breast Cancer Classification Using Decision Tree, Random Forest & Gradient Boosting

---

### 📊 Project Overview
**Title:** Breast Cancer Classification Using Decision Tree, Random Forest & Gradient Boosting  
**Objective:** Classify breast cancer tumors as **Malignant (Cancerous)** or **Benign (Non-cancerous)** using multiple ML models, compare their performance, and enable interactive prediction using user input.  

* **Files in Project:**  
  - `Assignment34.py` → Full pipeline (load data, train models, evaluate, save best model).  
  - `RunModel.py` → Load the saved model (`Assignment_34_Model.pkl`) and predict with user input.  

---

### 🧠 Key Features
- **Dataset:** Breast Cancer Wisconsin dataset from `sklearn.datasets`.  
- **Preprocessing:** StandardScaler used inside pipelines for normalization.  
- **Models Trained:**  
  - Decision Tree  
  - Random Forest  
  - Gradient Boosting  
- **Evaluation:** Accuracy, Confusion Matrix, Classification Report, ROC Curves, AUC Score.  
- **Visualization:**  
  - ROC Curves for each model  
  - Feature Importance (Top 10 features)  
  - Correlation Heatmap  
- **Model Persistence:** Save model with `joblib.dump` and reload with `joblib.load`.  
- **Interactive:** Predict outcome (Malignant/Benign) with CLI input of 30 features.  

---

### 🧰 Dependencies
Install required packages:
```bash
pip install pandas scikit-learn matplotlib seaborn joblib
```

---

### 📁 Dataset Details

* **Source:** `load_breast_cancer()` from Scikit-learn.  
* **Samples:** 569 tumor samples.  
* **Features:** 30 numeric features (mean, error, and worst values of tumor measurements).  
* **Target Classes:**  
  * `0` → Malignant (Cancerous)  
  * `1` → Benign (Non-cancerous)  

---

## 📂 Workflow (Assignment34.py)

1. **Load Dataset**

   * Load breast cancer dataset with `load_breast_cancer()`.  
   * Convert to Pandas DataFrame and add `target` column.  

2. **Display Data**

   * Show head, tail, dataset shape, datatypes, description, and null values check.  

3. **Preprocess Data**

   * Split into features (X) and target (Y).  

4. **Train-Test Split**

   * 70% training and 30% testing with `train_test_split`.  

5. **Model Training**

   * Train pipelines for:
     - Decision Tree  
     - Random Forest  
     - Gradient Boosting  
   * Evaluation Metrics: Accuracy, Confusion Matrix, Classification Report.  
   * Plot ROC Curves with AUC scores.  

6. **Save Best Model**

   * Save Gradient Boosting model:  
     ```python
     import joblib
     joblib.dump(model, "Assignment_34_Model.pkl")
     ```

7. **Load Saved Model**

   * Reload trained model for prediction:  
     ```python
     model = joblib.load("Assignment_34_Model.pkl")
     ```

8. **Feature Importance**

   * Plot Top 10 most important features for each model.  

9. **Additional Insights**

   * Plot Correlation Heatmap.  
   * Compare accuracy across models and display best model.  

10. **Interactive Prediction**

   * Prompt user for 30 feature values via CLI.  
   * Predict result as **Malignant (Cancerous)** or **Benign (Non-cancerous)**.  

---

## 🚀 Running the Project

1. Run training pipeline and save model:
   ```bash
   python Assignment34.py
   ```

2. Load saved model and predict with user input:
   ```bash
   python RunModel.py
   ```

---

## 📊 Example Output

**Model Accuracy Comparison:**
```
Decision Tree: 0.9181
Random Forest: 0.9532
Gradient Boosting: 0.9649
Best Model: Gradient Boosting
```

**Prediction Example (RunModel.py):**
```
Enter value for mean radius: 17.99
Enter value for mean texture: 10.38
...
Prediction: Malignant (Cancerous)
```

---

## 📜 Author

* Name: Rohit Pawar  
* Date: 02-08-2025
