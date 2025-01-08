#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Step 1: Import Libraries
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # For 3D visualization

# Step 2: Prepare the Dataset
data = {
    'Object': ['OB-1', 'OB-2', 'OB-3', 'OB-4', 'OB-5', 'OB-6', 'OB-7', 'OB-8'],
    'X': [1, 1, 1, 2, 1, 2, 1, 2],
    'Y': [4, 2, 4, 1, 1, 4, 1, 1],
    'Z': [1, 2, 2, 2, 1, 2, 2, 1]
}

# Convert to a Pandas DataFrame
df = pd.DataFrame(data)
print("Dataset:")
print(df)

# Extract the coordinates (X, Y, Z) for clustering
coordinates = df[['X', 'Y', 'Z']].values

# Step 3: Apply K-Means Clustering
# Initialize KMeans with 2 clusters
kmeans = KMeans(n_clusters=2, random_state=42)

# Fit the model to the data
kmeans.fit(coordinates)

# Get the cluster labels for each object
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
for i in range(2):  # Loop through each cluster
    cluster_points = coordinates[labels == i]  # Get points in the cluster
    new_centroid = np.mean(cluster_points, axis=0)  # Calculate mean
    new_centroids.append(new_centroid)

# Convert to a NumPy array
new_centroids = np.array(new_centroids)
print("\nNew Centroids (Calculated Manually):")
print(new_centroids)

# Step 5: Visualize the Clusters (3D Scatter Plot)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the clusters
scatter = ax.scatter(df['X'], df['Y'], df['Z'], c=df['Cluster'], cmap='viridis', s=100, label='Data Points')

# Plot the centroids
ax.scatter(centroids[:, 0], centroids[:, 1], centroids[:, 2], c='red', marker='X', s=200, label='Centroids')

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('K-Means Clustering (K=2) in 3D')
plt.legend()
plt.show()

