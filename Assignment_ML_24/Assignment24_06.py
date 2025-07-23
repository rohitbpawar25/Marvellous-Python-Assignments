# Count how many students passed
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

    df['Total'] = df[['Math','Science','English']].sum(axis=1)
    df["Status"] = df['Total'].apply(lambda x: 'Pass' if x>250 else 'Fail')
    Pass = df[df['Status'] == 'Pass'].shape[0] 
    print(f"Number of student who pass: {Pass}")

   
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

