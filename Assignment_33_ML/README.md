# 🎓 Student Performance Clustering Using KMeans

---

### 📊 Project Overview
**Title:** Student Performance Clustering Using KMeans  
**Objective:** Group students based on their academic performance and related features using KMeans clustering, then interpret and visualize these clusters.

---

### 🧠 Key Features
- **Dataset:** Student grades and behavioral data (G1, G2, G3, studytime, failures, absences).  
- **Preprocessing:** StandardScaler to normalize data before clustering.  
- **Clustering:** KMeans algorithm with 3 clusters to segment students.  
- **Semantic Labeling:** Clusters are labeled as `Top Performers`, `Average Students`, and `Struggling Students` based on cluster centers.  
- **Visualization:** Scatter plot of clusters using first and final period grades.  
- **Interactive:** Predict performance group for a new student via CLI input.

---

### 🧰 Dependencies
Install required packages:
```bash
pip install pandas scikit-learn matplotlib seaborn
```

---

### 📁 Dataset Details

* **Source:** Student performance dataset (CSV file `student-mat.csv`).
* **Key Features Used:**

  * `G1` (First period grade)
  * `G2` (Second period grade)
  * `G3` (Final grade)
  * `studytime` (Weekly study time)
  * `failures` (Number of past failures)
  * `absences` (School absences)

---

## 📂 Workflow

1. **Load Dataset**

   * Load `student-mat.csv` with semicolon separator.

2. **Display Data**

   * Preview sample rows and numerical statistics.

3. **Preprocess Data**

   * Select features and scale using `StandardScaler`.

4. **KMeans Clustering**

   * Apply KMeans with 3 clusters.

5. **Assign Semantic Labels**

   * Label clusters based on mean feature values for intuitive understanding.

6. **Annotate Data**

   * Add cluster IDs and labels to the dataframe.

7. **Visualization**

   * Plot clusters by `G1` and `G3` grades, colored by cluster labels.

8. **Predict New Student Group**

   * Input new student data and predict cluster label interactively.

---

## 🚀 Running the Project

1. Place `student-mat.csv` in your working directory.
2. Run the script:

```bash
python student_performance_clustering.py
```

3. Follow on-screen instructions to view data, cluster info, and predict new student group.

---

## 📊 Example Output

**Cluster Labels Assigned:**

```
{0: 'Average Students', 1: 'Top Performers', 2: 'Struggling Students'}
```

**Cluster Counts:**

```
Top Performers       130
Average Students     280
Struggling Students   90
```

**Prediction Example:**

```
Enter new student details to predict performance group:
G1 (First period grade): 15
G2 (Second period grade): 14
G3 (Final grade): 16
Weekly study time (1-4): 3
Number of past class failures: 0
Number of school absences: 2

The predicted performance group for the new student is: Top Performers
```

---

## 📜 Author

* Name: Your Name  
* Date: 2025-08-11
