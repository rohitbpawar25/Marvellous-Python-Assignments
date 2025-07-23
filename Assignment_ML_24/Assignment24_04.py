# Plot a pie chart of subject marks for 'Sagar'

"""
data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

"""

import pandas as pd
import matplotlib.pyplot as plt

def Pie(data):
    df = pd.DataFrame(data)


    sagar_data = df[df['Name'] == 'Sagar']
    if sagar_data.empty:
        print("Sagar not found in the dataset.")
        return

   
    subject_scores = sagar_data.drop(columns=['Name']).iloc[0]

   
    plt.figure(figsize=(8, 8))
    plt.pie(subject_scores, labels=subject_scores.index, autopct='%1.1f%%', startangle=140)
    plt.title("Subject-wise Marks Distribution for Sagar")
    plt.axis('equal')
    plt.show()

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    Pie(data)

if __name__ == "__main__":
    main()

