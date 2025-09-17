# 🏥 Breast Cancer Classification — Decision Tree, Random Forest & Gradient Boosting

---

## 📌 Project Overview
**Title:** Breast Cancer Classification Using Decision Trees, Random Forest, and Gradient Boosting  
**Objective:** Build and evaluate tree-based classification models to predict whether a tumour is **malignant** or **benign** using the sklearn `breast_cancer` dataset.

---

## 🧠 Key Features
- Loads the built-in `sklearn.datasets.load_breast_cancer` dataset and prepares it as a `pandas.DataFrame`.  
- Data inspection utilities (head/tail, shape, info, description, null checks).  
- Preprocessing using `StandardScaler` to normalize numerical features.  
- Models trained: **Decision Tree**, **Random Forest**, and **Gradient Boosting**.  
- Evaluation: Accuracy, confusion matrix, classification report, ROC curve and AUC (when supported).  
- Feature importance plots for tree-based models (top 10 features).  
- Interactive CLI: prompt user to input 30 numerical feature values to get a prediction from a trained model.

---

## 🧰 Dependencies
Install required packages with pip:
```bash
pip install pandas matplotlib scikit-learn
```

> The script uses only standard scientific Python libraries and scikit-learn's built-in dataset (no CSV required).

---

## 📂 Files & Structure
```
BreastCancerProject/
├─ breast_cancer_pipeline.py   # main script (contains functions shown in code)
├─ README.md                   # this file
└─ (optional outputs like plots saved by the script)
```

> In your case the main script uses `load_breast_cancer()` from sklearn as `INPUT_PATH` — no external dataset file is required.

---

## 🛠️ How the code is organised (functions)
- `Load_Data(Filepath)` — loads sklearn dataset into a DataFrame and adds `target` column.  
- `Display_Data(df)` — prints dataset head, tail, shape, info, description, and null checks.  
- `PreProcess_Data(df)` — separates features/target and returns scaled features (`StandardScaler`) + target.  
- `Train_Test(X_train, X_test, y_train, y_test)` — defines models, trains them, prints accuracy & reports, and plots ROC curves. Returns the trained model dictionary.  
- `Feature_Importance(model, feature_names, model_name)` — plots top 10 feature importances for tree-based models.  
- `Predict_With_User_Input(model, scaler, feature_names)` — interactively collects 30 numerical features from user, scales them, and returns prediction (0 → Malignant, 1 → Benign).  
- `main()` — orchestrates the whole pipeline: load, display, preprocess, train/test split, training, plotting feature importances, and interactive prediction.

---

## 🚀 Run the project
1. Make sure dependencies are installed.
2. Place `breast_cancer_pipeline.py` (your main script) in the working directory.
3. Run the script:
```bash
python breast_cancer_pipeline.py
```

The script will:
- print dataset summaries,
- train the three models (Decision Tree, Random Forest, Gradient Boosting),
- display accuracy, confusion matrices and classification reports,
- plot ROC curves (for models that provide `predict_proba`),
- plot top-10 feature importances for each tree-based model,
- ask you to enter 30 feature values for a custom prediction with the chosen model (default in code: Gradient Boosting).

---

## 📈 Example output (sample)
```
Accuracy Decision Tree is : 95.32
Accuracy Random Forest is : 96.48
Accuracy Gradient Boosting is : 97.14
```
ROC curve and feature-importance plots will open in new matplotlib windows when run locally.

---

## ⚠️ Notes & Tips
- The interactive `Predict_With_User_Input` expects **numerical** input for each of the 30 features in the same order as `feature_names` printed by the script.  
- For reproducibility, the `train_test_split` uses `random_state=42` in the provided code. Adjust `test_size` and `random_state` as needed.  
- If you prefer a non-interactive prediction, you can modify the script to accept a CSV row or a JSON payload for inference.

---

## 🧾 Author
**Rohit Pawar**  
**Date:** 28-07-2025
