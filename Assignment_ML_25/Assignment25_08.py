# Fill missing values in a numeric column using interpolation

"""
 Data = {'Marks': [85, np.nan, 90, np.nan, 95]}
 
"""

import pandas as pd
import numpy as np


def Interpolation(Data):
    df = pd.DataFrame(Data)


    df['Marks'] = df['Marks'].interpolate()

    print(df)

def main():
    Data = {'Marks': [85, np.nan, 90, np.nan, 95]}

    Interpolation(Data)

if __name__ == "__main__":
    main()
