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
* **Files Used:**

  * `True.csv` → Real News  
  * `Fake.csv` → Fake News  
* **Main Column Used:** `text`  
* **Label Encoding:**

  * `0` → Fake News  
  * `1` → Real News  

---

### 🔧 Workflow Breakdown

#### 1. **Load and Display Data**

* Load both CSV files using `pandas`.
* Preview samples and visualize class distribution using `matplotlib`.

#### 2. **Preprocessing**

* Add a `label` column (`0` for fake, `1` for real).
* Concatenate fake and real news dataframes into one.

#### 3. **Text Vectorization**

Uses TF-IDF to convert the text data into numerical feature vectors.

```python
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_vectorized = vectorizer.fit_transform(df['text'])
```

#### 4. **Train-Test Split**

Split the dataset into 80% training and 20% testing data.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, df['label'], train_size=0.8, random_state=42
)
```

#### 5. **Train Models**

Train Logistic Regression and Decision Tree classifiers.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

logistic_model = LogisticRegression()
tree_model = DecisionTreeClassifier()

logistic_model.fit(X_train, y_train)
tree_model.fit(X_train, y_train)
```

#### 6. **Evaluate Models**

Evaluate training and testing accuracy and plot confusion matrices.

```python
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

predictions = model.predict(X_test)
acc = accuracy_score(y_test, predictions)
cm = confusion_matrix(y_test, predictions)
ConfusionMatrixDisplay(cm).plot()
```

#### 7. **Voting Classifier**

Combine both models using hard voting for better generalization.

```python
from sklearn.ensemble import VotingClassifier

voting_clf = VotingClassifier(
    estimators=[('lr', logistic_model), ('dt', tree_model)],
    voting='hard'
)
voting_clf.fit(X_train, y_train)
```

#### 8. **Command-line Prediction**

User can input a news article and get a real-time prediction.

```python
text = input("Enter a news article: ")
vec = vectorizer.transform([text])
prediction = voting_clf.predict(vec)
print("REAL NEWS ✅" if prediction[0] else "FAKE NEWS ❌")
```

---

### 🧪 Sample CLI Prediction

```bash
Enter a news article (or type 'exit' to quit): 
"NASA announces breakthrough in Mars exploration mission."

Prediction: REAL NEWS ✅
```

---

### 🗂️ Project Structure

```
📁 FakeNewsClassifier/
├── True.csv
├── Fake.csv
├── fake_news_classifier.py
├── README.md
```

---

### 📅 Author & Contact

* **Author:** Rohit Pawar 
* **Date:** August 11, 2025  

---

