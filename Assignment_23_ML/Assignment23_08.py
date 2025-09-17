# Plot a line chart of Amit’s marks across all subjects

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
    
    AmitMarks = df[df['Name'] == 'Amit'][['Math', 'Science', 'English']].iloc[0]

    plt.plot(AmitMarks.index, AmitMarks.values, marker='o')
    plt.title("Amit's Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Scores")
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