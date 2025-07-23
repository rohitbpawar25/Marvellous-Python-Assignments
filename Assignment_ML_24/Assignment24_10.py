#Visualize the distribution of 'English' marks and detect any outliers using a boxplot

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

    plt.figure(figsize=(6, 6))
    plt.boxplot(df['English'], patch_artist=True, boxprops=dict(facecolor='lightgreen'))
    plt.title('Boxplot of English Marks')
    plt.ylabel('Marks')
    plt.grid(True)
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

