#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Step 1: Import Libraries
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Step 2: Assume a Dataset
# Create the dataset
data = np.array([
    [1.0, 1.0],
    [1.5, 2.0],
    [3.0, 4.0],
    [5.0, 7.0],
    [3.5, 5.0],
    [4.5, 5.0],
    [3.5, 4.5]
])

# Convert to a Pandas DataFrame for better visualization
df = pd.DataFrame(data, columns=['X', 'Y'])
print("Dataset:")
print(df)

# Step 3: Apply K-Means Clustering
# Initialize KMeans with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)

# Fit the model to the data
kmeans.fit(data)

# Get the cluster labels for each data point
labels = kmeans.labels_

# Add the cluster labels to the DataFrame
df['Cluster'] = labels
print("\nDataset with Cluster Labels:")
print(df)

# Step 4: Find the New Centroids
# Get the centroids from the KMeans model
centroids = kmeans.cluster_centers_

# Display the centroids
print("\nInitial Centroids:")
print(centroids)

# Calculate new centroids manually
new_centroids = []
for i in range(3):  # Loop through each cluster
    cluster_points = data[labels == i]  # Get points in the cluster
    new_centroid = np.mean(cluster_points, axis=0)  # Calculate mean
    new_centroids.append(new_centroid)

# Convert to a NumPy array
new_centroids = np.array(new_centroids)
print("\nNew Centroids (Calculated Manually):")
print(new_centroids)

# Step 5: Visualize the Clusters and Centroids
# Plot the clusters
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', s=50, label='Data Points')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('K-Means Clustering (K=3)')
plt.legend()
plt.show()

