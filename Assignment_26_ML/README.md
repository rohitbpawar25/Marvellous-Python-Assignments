
# 🎯 Play Predictor Using K-Nearest Neighbors (KNN)

---

### 📊 Project Overview  
**Title:** Predicting Play or Not Based on Weather and Temperature  
**Objective:** Build a KNN classifier to predict whether to play outside depending on weather and temperature conditions.

---

### 🧠 Key Features
- **Dataset:** Weather, Temperature, and Play (Yes/No) data.  
- **Preprocessing:** Label encoding categorical variables (Weather, Temperature, Play).  
- **Model:** K-Nearest Neighbors classifier to predict Play decision.  
- **Hyperparameter Tuning:** Check model accuracy over multiple K values (1 to 10).  
- **Visualization:** Accuracy vs K graph and Confusion Matrix heatmap.  
- **User Interaction:** Predict Play status based on user input weather and temperature.

---

### 🧰 Dependencies

Install the required Python packages:

```bash
pip install pandas scikit-learn matplotlib seaborn
```

---

### 📁 Dataset Details

* **File:** `PlayPredictor.csv`  
* **Features:**  
  - `Weather` (e.g., Sunny, Rainy, Overcast)  
  - `Temperature` (e.g., Hot, Mild, Cool)  
  - `Play` (Yes/No)

---

## 📂 Workflow

1. **Load Dataset**  
   Load the CSV file into a pandas DataFrame.

2. **Display Data**  
   Show the first and last 5 rows, dataset shape, summary info, and check for missing values.

3. **Preprocess Data**  
   Label encode categorical columns to numeric values for model compatibility.

4. **Train KNN Model**  
   Train the model with a fixed K (default 3), evaluate accuracy on test split.

5. **Evaluate Accuracy Across K**  
   Loop through K=1 to 10 to find the best K with highest accuracy and plot accuracy graph.

6. **User Input Prediction**  
   Accept weather and temperature input from the user to predict Play or Not.

7. **Confusion Matrix**  
   Display confusion matrix heatmap for model evaluation.

---

## 🚀 Running the Project

1. Place `PlayPredictor.csv` in your working directory.  
2. Run the script:

```bash
python play_predictor_knn.py
```

3. Follow the prompts to view data summary, model accuracy, and input your own conditions for prediction.

---

## 📊 Example Output

```
Accuracy of Model with K=3: 0.85
K=1 → Accuracy: 0.80
K=2 → Accuracy: 0.82
K=3 → Accuracy: 0.85
...
Best Accuracy is 0.85 at K=3

Possible Weather values: ['Overcast', 'Rainy', 'Sunny']
Enter Weather: Sunny
Possible Temperature values: ['Cool', 'Hot', 'Mild']
Enter Temperature: Hot
🎯 Predicted Result: No
```

---

## 📜 Author

- Name: Rohit Pawar  
- Date: 19-07-2025
