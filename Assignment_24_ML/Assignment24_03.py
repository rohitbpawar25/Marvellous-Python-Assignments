# Q2: Group students by gender and calculate average marks.

"""
data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

"""

import pandas as pd

def CalAvg(Datapath):
    df = pd.DataFrame(Datapath)
    AverageMarks = df.groupby('Gender')[['Math','Science','English']].mean()
    print("Average Marks are :",AverageMarks)
   

def main():
    Data = {
    'Name': ['Amit','Raj', 'Pooja'],
    'Gender': ['Male','Male', 'Female'],
    'Math': [80,70, 85],
    'English': [75,60, 95],
    'Science': [85,75, 89]
}
    CalAvg(Data)

if __name__ == "__main__":
    main()
