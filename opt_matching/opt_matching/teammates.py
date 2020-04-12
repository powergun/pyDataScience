from pulp import LpProblem, LpMaximize


def main():
    prob = LpProblem("MatchingEmployees", LpMaximize)
