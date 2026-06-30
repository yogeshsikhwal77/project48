from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from class_make import KMeans
import pandas as pd

centroid = [(-5,-5),(5,5)]
cluster_std = [1,1]
X,y = make_blobs(n_samples=100,cluster_std=cluster_std,centers=centroid,n_features=2,random_state=2)

km = KMeans(n_cluster=2,max_iter=100)
y_means = km.fit_predict(X)

plt.scatter(X[y_means == 0,0],X[y_means == 0,1],color='red')
plt.scatter(X[y_means == 1,0],X[y_means == 1,1],color='blue')

plt.show()