import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans


def generate_data():
    x, y = make_blobs(n_samples=300,
                      centers=4,
                      cluster_std=0.60,
                      random_state=0)
    plt.scatter(x[:, 0], x[:, 1])


def main():
    generate_data()
