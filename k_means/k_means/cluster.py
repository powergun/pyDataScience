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
    # call show() to launch the display window
    # see: https://pythonspot.com/matplotlib-scatterplot/
    # plt.show()

    return x, y


def demo_elbow_method(x):
    # to demo elbow method (the optimal num of clusters is known to be 4)
    # To get the values used in the graph, we train multiple models using
    # a different number of clusters and storing the value of the intertia_
    # property (WCSS) every time.
    wcss = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i,
                        init='k-means++',
                        max_iter=300,
                        n_init=10,
                        random_state=0)
        kmeans.fit(x)
        wcss.append(kmeans.inertia_)
    plt.plot(range(1, 11), wcss)
    plt.title('Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()


def k_means(x):
    # Next, we’ll categorize the data using the optimum number of
    # clusters (4) we determined in the last step. k-means++ ensures
    # that you get don’t fall into the random initialization trap.
    kmeans = KMeans(n_clusters=4,
                    init='k-means++',
                    max_iter=300,
                    n_init=10,
                    random_state=0)
    pred_y = kmeans.fit_predict(x)
    plt.scatter(x[:, 0], x[:, 1])
    plt.scatter(kmeans.cluster_centers_[:, 0],
                kmeans.cluster_centers_[:, 1],
                s=300,
                c='red')
    plt.show()


if __name__ == '__main__':
    x, y = generate_data()
    k_means(x)
