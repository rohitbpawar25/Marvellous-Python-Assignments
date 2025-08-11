# 📈 Advertising Sales Prediction Using Linear Regression

---

### 📊 Project Overview
**Title:** Advertising Sales Prediction Using Linear Regression  
**Objective:** Predict increased sales based on advertisement investments in TV, radio, and newspaper using a Linear Regression model.

---

### 🧠 Key Features
- **Dataset:** Advertising investments and corresponding sales (`Advertising.csv`).  
- **Preprocessing:** Dropping unnecessary index columns and selecting relevant features.  
- **Model:** Linear Regression from scikit-learn to model sales prediction.  
- **Data Split:** 50% training and 50% testing split for model validation.  
- **Evaluation:** Model performance evaluated using Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R-squared metrics.  
- **Interactive Prediction:** Allows user input for advertisement budgets and outputs predicted sales.

---

### 🧰 Dependencies
Install required packages:
```bash
pip install pandas numpy scikit-learn
```

---

### 📁 Dataset Details

* **Source:** Advertising investment and sales dataset (`Advertising.csv`).  
* **Key Features Used:**

  * `TV` (TV advertisement budget)  
  * `radio` (Radio advertisement budget)  
  * `newspaper` (Newspaper advertisement budget)  
  * `sales` (Target variable: sales amount)

---

## 📂 Workflow

1. **Load Dataset**  
   Load `Advertising.csv` from the working directory.

2. **Display Data Summary**  
   Preview dataset head, tail, shape, info, descriptive statistics, and check for missing values.

3. **Preprocess Data**  
   Drop unnecessary columns (e.g., index), select features (`TV`, `radio`, `newspaper`) and target (`sales`).

4. **Train Model**  
   Split dataset into 50% train and 50% test sets, then train a Linear Regression model.

5. **Evaluate Model**  
   Predict on test set and compute MSE, RMSE, and R² score.

6. **User Input Prediction**  
   Take advertisement budgets as input and output predicted sales value.

---

## 🚀 Running the Project

1. Place `Advertising.csv` in your working directory.  
2. Run the script:

```bash
python advertising_sales_prediction.py
```

3. Follow on-screen prompts to see data summary, evaluation metrics, and enter budgets to predict sales.

---

## 📊 Example Output

```
Mean Squared Error (MSE) on Test Set: 2.4705
Root Mean Squared Error (RMSE) on Test Set: 1.5717
R-Squared Value on Test Set: 0.9004
------------------------------------------------------------------------------------------
Enter TV Budget: 150
Enter Radio Budget: 30
Enter Newspaper Budget: 20
Predicted Sales: 18.25 units
------------------------------------------------------------------------------------------
```

---

## 📜 Author

* Name: Rohit Pawar  
* Date: 26-07-2025
