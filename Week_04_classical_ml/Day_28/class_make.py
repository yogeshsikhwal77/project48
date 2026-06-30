import random
import numpy as np

class KMeans:
    def __init__(self,n_cluster=2,max_iter=100):
        self.n_clusters = n_cluster
        self.max_iter = max_iter
        self.centroid = None

    def fit_predict(self,X):
        random_index = random.sample(range(0,X.shape[0]),self.n_clusters)
        self.centroid = X[random_index]
        for i in range(self.max_iter):
            #assign cluster
            cluster_group = self.assign_cluster(X)
            #move centroid
            old_centroids =self.centroid
            self.centroid = self.move_centroid(X,cluster_group)
            # check finish
            if (old_centroids == self.centroid).all():
                break

        return cluster_group


    def assign_cluster(self,X):
        cluster_group = []
        distances = []
        for row in X:
            for centroid in self.centroid:
                distances.append(np.sqrt(np.dot(row-centroid,row-centroid)))

            min_distance = min(distances)
            index_pos = distances.index(min_distance)
            cluster_group.append(index_pos)
            distances.clear()
        return np.array(cluster_group)
    
    def move_centroid(self,X,cluster_group):
        new_cluster = []
        cluster_type = np.unique(cluster_group)

        for type in cluster_type:
            new_cluster.append(X[cluster_group==type].mean(axis=0))

        return np.array(new_cluster)