# K-Means

## K-Means Clustering Demo

dependencies: numpa, pandas, matplotlib, sklearn

source: <https://towardsdatascience.com/machine-learning-algorithms-part-9-k-means-example-in-python-f2ad05ed5203>

> K-Means Clustering is an unsupervised machine learning algorithm.
> In contrast to traditional supervised machine learning algorithms,
> K-Means attempts to classify data without having first been trained
> with labeled data. Once the algorithm has been run and the groups are
> defined, any new data can be easily assigned to the most relevant group.

The real world applications of K-Means include:

```text
    customer profiling
    market segmentation
    computer vision
    search engines
    astronomy
```

### How it works

Select K random points as cluster centers called centroids. For example
select 2 random points.

Assign each data point to the closest cluster by calculating its distance
with respect to each centroid

Determine the new cluster center by computing the average of the assigned points

Repeat steps 2 and 3 until none of the cluster assignments change

### Choose the right number of clusters

> We graph the relationship between the number of clusters and Within Cluster
> Sum of Squares (WCSS) then we select the number of clusters where the change
> in WCSS begins to level off (elbow method).
