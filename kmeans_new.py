import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Define the data points
X = np.array([[10, 10], [10, 11], [11, 12], [1, 2], [1, 1], [2, 2], [5, 6], [6, 6], [5, 5]])

# Define the initial centroids
initial_centroids = np.array([[10, 10], [1, 1], [5, 5]])

# Create a KMeans object with 3 clusters and fit the data
kmeans = KMeans(n_clusters=3, init=initial_centroids).fit(X)

# Get the cluster assignments for each data point
labels = kmeans.labels_

# Get the final centroids for each cluster
centroids = kmeans.cluster_centers_

# Print the final centroids
print("Final centroids:")
print(centroids)

print(X[:,0])

# Plot the data points and the final centroids
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=200, linewidths=3, color='r')
plt.show()
