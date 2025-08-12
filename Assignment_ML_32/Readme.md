# 📰 Fake News Classification using Logistic Regression, Decision Tree & Voting Classifier

---

### 📊 Project Overview
**Title:** Fake News Classification using Machine Learning  
**Objective:** Predict whether a news article is REAL or FAKE using text-based classification models like Logistic Regression, Decision Tree, and an Ensemble Voting Classifier — with preprocessing and TF-IDF vectorization combined in one streamlined step.

---

### 🧠 Key Features
- **Industrial-Grade Format:** Suitable for GitHub portfolios, resumes, and interviews.
- **Integrated Preprocessing & Vectorization:** Cleans and labels data, then transforms it into numerical features using `TfidfVectorizer` — all in a single function.
- **Models Used:** Logistic Regression, Decision Tree Classifier, and Hard Voting Classifier.
- **Evaluation:** Reports training/testing accuracy and plots confusion matrices.
- **Interactive CLI:** Lets users type custom news text to classify as real or fake.

---

### 🧰 Dependencies
Install required packages:
```bash
pip install pandas scikit-learn matplotlib
```

---

### 📁 Dataset Details
* **Source:** Kaggle (or any manually curated dataset)  
  Kaggle link: [Fake and Real News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)
* **Files Used:**
  * `True.csv` → Real News  
  * `Fake.csv` → Fake News  
* **Main Column Used:** `text`  
* **Label Encoding:**
  * `0` → Fake News  
  * `1` → Real News  

---

## 📂 Workflow
1. **Data Loading**  
   - Load `True.csv` and `Fake.csv`.
   - Display sample rows and class distribution.

2. **Preprocessing + Vectorization**  
   - Assign labels (`0` fake, `1` real).
   - Merge datasets into one dataframe.
   - Vectorize text data using `TfidfVectorizer`.

3. **Train-Test Split**  
   - 80% training, 20% testing.

4. **Model Training**  
   - Train Logistic Regression & Decision Tree Classifier.

5. **Evaluation**  
   - Accuracy scores for training/testing sets.
   - Confusion Matrix visualizations.

6. **Ensemble Voting Classifier**  
   - Combine Logistic Regression & Decision Tree for final predictions.

7. **Interactive Prediction Mode**  
   - Accept custom news text input from the user.

---

## 📊 Visualizations
- **Class Distribution** (Bar Chart)
- **Confusion Matrices** for each model

---

## 🚀 Running the Project
1. Place `True.csv` and `Fake.csv` in the same directory as the script.
2. Run the script:
```bash
python fake_news_detection.py
```
3. Follow the prompts to:
   - View dataset stats  
   - Train & evaluate models  
   - Test with your own news text  

---

## 📈 Example Output
```
Fake News Count: 23481
Real News Count: 21417

LogisticRegression Training Accuracy: 99.12%
LogisticRegression Testing Accuracy : 98.75%
DecisionTreeClassifier Training Accuracy: 100.00%
DecisionTreeClassifier Testing Accuracy : 95.43%
Voting Classifier Testing Accuracy : 98.12%
```

---

## 📜 Author
- **Name:** Rohit Pawar  
- **Date:** 28-07-2025  
