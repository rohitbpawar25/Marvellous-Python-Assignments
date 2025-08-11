########################################################
# Required Python Packages
########################################################

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

########################################################
# File Path
########################################################

INPUT_PATH = "student-mat.csv"

########################################################
# Read raw data
########################################################

def Load_Data(DataPath):
    df = pd.read_csv(DataPath, sep=";")
    return df

########################################################
# Display Data
########################################################

def Display_Data(df):
    print("Student Performance Data Sample :\n".center(90))
    print(df.head(), "\n")
    print("-" * 90)
    
    print("Statistical Summary of Numerical Features :\n".center(90))
    print(df.describe(), "\n")
    print("-" * 90)
    
    if 'cluster' in df.columns:
        print("Count of Students per Cluster".center(90))
        print(df['cluster'].value_counts(), "\n")

########################################################
# Preprocess Data
########################################################

def Preprocess_Data(df):
    Select_Feature = ['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']
    X = df[Select_Feature].copy()

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, scaler, Select_Feature

########################################################
# Apply KMeans Clustering
########################################################

def KMeans_Model(X_scaled, n_clusters):
    model = KMeans(n_clusters=n_clusters, random_state=42)
    clusters = model.fit_predict(X_scaled)
    return model, clusters

########################################################
# Assign Semantic Labels to Clusters
########################################################

def Assign_Cluster_Labels(model, scaler):
    centers = scaler.inverse_transform(model.cluster_centers_)
    labels = {}
    for i, center in enumerate(centers):
        G1, G2, G3, studytime, failures, absences = center
        if (G1 > 12 and G2 > 12 and G3 > 12) and (failures < 1) and (studytime >= 2) and (absences < 5):
            labels[i] = 'Top Performers'
        elif (G1 < 10 and G2 < 10 and G3 < 10) and (failures >= 1) and (studytime < 2) and (absences >= 5):
            labels[i] = 'Struggling Students'
        else:
            labels[i] = 'Average Students'
    return labels

########################################################
# Add Cluster Columns to DataFrame
########################################################

def Add_Cluster_Columns(df, clusters, cluster_labels):
    df['cluster'] = clusters
    df['cluster_label'] = df['cluster'].map(cluster_labels)
    return df

########################################################
# Plot Clusters
########################################################

def Plot_Clusters(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='G1', y='G3', hue='cluster_label', palette='Set1', s=70)
    plt.title('Clusters of Students by G1 and G3 Grades')
    plt.xlabel('G1 (First period grade)')
    plt.ylabel('G3 (Final grade)')
    plt.legend(title='Cluster')
    plt.show()

########################################################
# Predict and Display New Student's Cluster
########################################################

def Predict_New_Student(model, scaler, cluster_labels, features):
    print("\nEnter new student details to predict performance group:")
    G1 = float(input("G1 (First period grade): "))
    G2 = float(input("G2 (Second period grade): "))
    G3 = float(input("G3 (Final grade): "))
    studytime = float(input("Weekly study time (1-4): "))
    failures = int(input("Number of past class failures: "))
    absences = int(input("Number of school absences: "))

    new_student_df = pd.DataFrame([[G1, G2, G3, studytime, failures, absences]], columns=features)
    new_student_scaled = scaler.transform(new_student_df)
    pred_cluster = model.predict(new_student_scaled)[0]
    pred_label = cluster_labels[pred_cluster]

    print(f"\nThe predicted performance group for the new student is: {pred_label}")

########################################################
# Main execution
########################################################

def main():
    print("-" * 90)
    print("Student Performance Clustering Using KMeans".center(90))
    print("-" * 90)

    # Step 1: Load dataset
    print("Load dataset".center(90))
    df = Load_Data(INPUT_PATH)
    print("Dataset loaded successfully.".center(90))
    print("-" * 90)

    # Step 2: Display raw data sample and stats
    print("Display data preview".center(90))
    Display_Data(df)
    print("-" * 90)

    # Step 3: Preprocess data
    print("Preprocess data".center(90))
    X_scaled, scaler, features = Preprocess_Data(df)
    print("Data preprocessing completed.".center(90))
    print("-" * 90)

    # Step 4: Apply KMeans clustering
    print("Apply KMeans clustering".center(90))
    model, clusters = KMeans_Model(X_scaled, n_clusters=3)
    print("Clustering completed.".center(90))
    print("-" * 90)

    # Step 5: Assign semantic labels to clusters
    print("Assign cluster labels".center(90))
    cluster_labels = Assign_Cluster_Labels(model, scaler)
    print(f"Cluster labels assigned: {cluster_labels}")
    print("-" * 90)

    # Step 6: Add cluster info to dataframe
    print("Annotate data with cluster info".center(90))
    df = Add_Cluster_Columns(df, clusters, cluster_labels)
    Display_Data(df)
    print("-" * 90)

    # Step 7: Visualize clusters
    print("Visualize clusters".center(90))
    Plot_Clusters(df)
    print("-" * 90)

    # Step 8: Predict new student cluster
    print("Predict new student performance group".center(90))
    Predict_New_Student(model, scaler, cluster_labels, features)
    print("-" * 90)

if __name__ == "__main__":
    main()
