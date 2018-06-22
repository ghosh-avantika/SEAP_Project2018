# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')

#importing datasets
data = pd.read_csv('airplane')#change when data is received
print(data.shape)
data.head()

#Value plotting
pt1 = data['V1'].values
pt2 = data['V2'].values
x = np.array(list(zip(pt1, pt2)))
plt.scatter(pt1, pt2, c='black', s=7)

#Calculating distance for updating centroid
def dist(a, b, ax=1):
    return np.linalg.norm(a - b, axis=ax)

# Number of clusters
number = 3
# X coordinates of random centroids
x_coord = np.random.randint(0, np.max(x)-20, size=number)
# Y coordinates of random centroids
y_coord = np.random.randint(0, np.max(x)-20, size=number)
C = np.array(list(zip(x_coord, y_coord)), dtype=np.float32)
print(C)

# To store the value of centroids when it updates
old = np.zeros(C.shape)
# Cluster Lables(0, 1, 2)
clusters = np.zeros(len(x))
# Error func. - Distance between new centroids and old centroids
error = dist(C, old, None)
# Loop will run till the error becomes zero
while error != 0:
    # Assigning each value to its closest cluster
    for i in range(len(x)):
        distances = dist(x[i], C)
        cluster = np.argmin(distances)
        clusters[i] = cluster
    # Storing the old centroid values
    old = deepcopy(C)
    # Finding the new centroids by taking the average value
    for i in range(number):
        points = [x[j] for j in range(len(x)) if clusters[j] == i]
        C[i] = np.mean(points, axis=0)
    error = dist(C, old, None)