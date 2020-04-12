from pulp import LpProblem, LpMaximize, LpVariable, lpSum
import numpy as np
import pandas as pd


def main():
    prob = LpProblem("MatchingEmployees", LpMaximize)
    employees = range(8)
    names = [
        'Ben', 'Kate', 'Thinh', 'Jorge', 'Alfredo', 'Francisco', 'Olivia',
        'Chris'
    ]
    np.random.seed(0)
    c = np.random.randint(0, 10, (8, 8))
    np.fill_diagonal(c, 0)
    match_info = pd.DataFrame(c, index=names, columns=names)

    y = LpVariable.dicts("pair",
                         [(i, j) for i in employees for j in employees],
                         cat='Binary')
    prob += lpSum([(c[i][j] + c[j][i]) * y[(i, j)] for i in employees
                   for j in employees])

    for i in employees:
        prob += lpSum(y[(i, j)] for j in employees) <= 1
        prob += lpSum(y[(j, i)] for j in employees) <= 1
        prob += lpSum(y[(i, j)]
                      for j in employees) + lpSum(y[(j, i)]
                                                  for j in employees) <= 1
        prob += lpSum(y[(i, j)] for i in employees for j in employees) == 4

    prob.solve()
    print("Finish matching!\n")
    for i in employees:
        for j in employees:
            if y[(i, j)].varValue == 1:
                print(
                    '{} and {} with preference score {} and {}. Total score: {}'
                    .format(names[i], names[j], c[i, j], c[j, i],
                            c[i, j] + c[j, i]))
