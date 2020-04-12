import os
import sys

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# source:
# https://www.analyticsvidhya.com/blog/2020/03/pivot-table-pandas-python/


def this_dir():
    return os.path.dirname(os.path.realpath(sys.argv[0]))


def resource_file(name):
    return os.path.join(this_dir(), name)


def main():
    matplotlib.use('Qt5Agg')

    df = pd.read_csv(resource_file('train.csv'))
    print(df.head())
    df.drop(['PassengerId', 'Ticket', 'Name'], inplace=True, axis=1)
    pivot = pd.pivot_table(data=df, index=['Sex'])
    print(pivot)

    pivot = pd.pivot_table(df,
                           index=['Sex'],
                           columns=['Pclass'],
                           values=['Survived'],
                           aggfunc=np.sum)
    pivot.plot(kind='bar')
    plt.show()