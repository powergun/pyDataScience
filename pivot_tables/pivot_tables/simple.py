import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
# source:
# https://datatofish.com/pivot-table-python/


def generate_data():
    employees = {
        'Name of Employee': [
            'Jon', 'Mark', 'Tina', 'Maria', 'Bill', 'Jon', 'Mark', 'Tina',
            'Maria', 'Bill', 'Jon', 'Mark', 'Tina', 'Maria', 'Bill', 'Jon',
            'Mark', 'Tina', 'Maria', 'Bill'
        ],
        'Sales': [
            1000, 300, 400, 500, 800, 1000, 500, 700, 50, 60, 1000, 900, 750,
            200, 300, 1000, 900, 250, 750, 50
        ],
        'Quarter':
        [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4],
        'Country': [
            'US', 'Japan', 'Brazil', 'UK', 'US', 'Brazil', 'Japan', 'Brazil',
            'US', 'US', 'US', 'Japan', 'Brazil', 'UK', 'Brazil', 'Japan',
            'Japan', 'Brazil', 'UK', 'US'
        ]
    }

    df = pd.DataFrame(
        employees, columns=['Name of Employee', 'Sales', 'Quarter', 'Country'])
    return df


def main():
    df = generate_data()

    # scenario 1: total sales per employee
    pivot = df.pivot_table(index=['Name of Employee'],
                           values=['Sales'],
                           aggfunc='sum')
    # print a tabular ascii table
    # print(pivot)

    # scenario 2: total sales by country
    matplotlib.use('Qt5Agg')
    pivot = df.pivot_table(index=['Country'], values=['Sales'],
                           aggfunc='sum').plot()
    # see README.md for additional installation steps (PyQt5)
    # plt.show()

    # scenario 3: sales by both employee and country
    pivot = df.pivot_table(index=[
        'Country',
        'Name of Employee',
    ],
                           values=['Sales'],
                           aggfunc='sum')
    # print(pivot)

    # scenario 4: max sales max individual safe by country
    pivot = df.pivot_table(index=['Country'], values=['Sales'], aggfunc='max')
    # print(pivot)

    # Scenario 5: Mean, median and minimum sales by country
    pivot = df.pivot_table(index=['Country'],
                           values=['Sales'],
                           aggfunc={'max', 'mean', 'min'}).plot()
    # print(pivot)