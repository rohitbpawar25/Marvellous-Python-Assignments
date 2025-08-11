# 📰 Fake News Classification using Logistic Regression, Decision Tree & Voting Classifier

---

### 📊 Project Overview
**Title:** Fake News Classification using Machine Learning  
**Objective:** Predict whether a news article is REAL or FAKE using text-based classification models like Logistic Regression, Decision Tree, and Voting Classifier.

---

### 🧠 Key Features
- **Industrial Format:** Designed for GitHub portfolio, resume inclusion, and technical interviews.
- **Text Vectorization:** Uses TF-IDF to transform raw news articles into numerical features.
- **Modeling Techniques:** Logistic Regression, Decision Tree Classifier, and Ensemble Voting Classifier.
- **Evaluation:** Visualizes performance via confusion matrices and accuracy scores.
- **Interactive CLI:** Accepts news input from user and predicts if it's real or fake.

---

### 🧰 Dependencies
Install required packages:
```bash
pip install pandas scikit-learn matplotlib
```
---

### 📁 Dataset Details

* **Source:** Kaggle or manually created from Real and Fake news sources.
Kaggle :(https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)
* **Files Used:**
  * `True.csv` → Real News  
  * `Fake.csv` → Fake News  
* **Main Column Used:** `text`  
* **Label Encoding:**

  * `0` → Fake News  
  * `1` → Real News  

---
## 📂 Workflow
1. **Data Preparation**  
   - Load `True.csv` and `Fake.csv` datasets.
   - Display dataset samples and class distribution.

2. **Data Preprocessing**  
   - Assign labels: `0` for Fake, `1` for Real.
   - Merge datasets into a single dataframe.

3. **Vectorization**  
   - Use `TfidfVectorizer` for text transformation.

4. **Train-Test Split**  
   - 80% training data, 20% testing data.

5. **Model Training**  
   - Train Logistic Regression & Decision Tree models.

6. **Model Evaluation**  
   - Accuracy score and Confusion Matrix plots.

7. **Ensemble Model**  
   - Hard voting using Logistic Regression & Decision Tree.

8. **User Prediction Mode**  
   - Enter custom news articles to classify.

## 📊 Visualizations
- **Class Distribution** (Bar Chart)
- **Confusion Matrix** for each model

## 🚀 Running the Project
1. **Prepare your data**  
   Place `True.csv` and `Fake.csv` in the same folder as the script.

2. **Run the script**
```bash
python fake_news_detection.py
```
3. **Follow the steps**  
   * Data loading & visualization  
   * Model training & evaluation  
   * Ensemble voting classifier  
   * Interactive news prediction

## 📈 Example Output

**Class Distribution**
```
Fake News Count: 23481
Real News Count: 21417
```

**Model Accuracies**
```
LogisticRegression Training Accuracy: 99.12%
LogisticRegression Testing Accuracy : 98.75%
DecisionTreeClassifier Training Accuracy: 100.00%
DecisionTreeClassifier Testing Accuracy : 95.43%
Voting Classifier Testing Accuracy : 98.12%
```

## 📜 Author
##Name : Rohit Pawar
##Date : 2023-02-20

