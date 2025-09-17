# Create a bar plot of student names vs total marks

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

def BasicInfo(DataPath):
    
    df = pd.DataFrame(DataPath) 
    
    df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1)

    plt.figure(figsize=(8, 5))
    plt.bar(df['Name'], df['Total'], color='skyblue', edgecolor='black')

    plt.title('Total Marks by Student')
    plt.xlabel('Student Name')
    plt.ylabel('Total Marks')
    plt.show()

def main():

    Data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]}

    BasicInfo(Data)


if __name__ == "__main__":
    main()