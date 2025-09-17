# Plot a histogram of Math marks
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

    plt.figure(figsize=(8,6))
    plt.hist(df['Math'],bins=5,color='skyblue',edgecolor='black')
    plt.title('Histogram of Math Marks')
    plt.xlabel('Math Marks')
    plt.ylabel('Number of Students')
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

