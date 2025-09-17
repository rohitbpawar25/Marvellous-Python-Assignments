# Replace values in 'Marks' less than 50 with 'Fail' using where()
"""
 Data = {'Marks': [45, 67, 88, 32, 76]}

"""

import pandas as pd
import numpy as np


def ReplaceValues(Data):
    df = pd.DataFrame(Data)

    df['Result'] = df['Marks'].where(df['Marks'] >= 50, 'Fail')

    print(df)

def main():
    Data = {'Marks': [45, 67, 88, 32, 76]}

    ReplaceValues(Data)

if __name__ == "__main__":
    main()
