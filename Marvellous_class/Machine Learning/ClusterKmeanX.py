import copy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Initialisation
df = pd.DataFrame({
    'x': [12, 20, 28, 18, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53, 55, 61, 64, 69, 72],
    'y': [39, 36, 30, 52, 54, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14, 8, 19, 7, 24]
})

np.random.seed(200)
k = 3
centroids = {i+1: [np.random.randint(0, 80), np.random.randint(0, 80)] for i in range(k)}
colmap = {1: 'r', 2: 'g', 3: 'b'}

# Initial plot
plt.scatter(df['x'], df['y'], color='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.title("Marvellous : Dataset with random centroid")
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show()

# Step 2: Assignment
def assignment(df, centroids):
    for i in centroids.keys():
        df[f'distance_from_{i}'] = np.sqrt((df['x'] - centroids[i][0])**2 + (df['y'] - centroids[i][1])**2)
    distance_cols = [f'distance_from_{i}' for i in centroids.keys()]
    df['closest'] = df.loc[:, distance_cols].idxmin(axis=1).map(lambda x: int(x.lstrip('distance_from_')))
    df['color'] = df['closest'].map(lambda x: colmap[x])
    return df

df = assignment(df, centroids)

# Plot after assignment
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.title("Marvellous : Dataset with clustering & random centroid")
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show()

# Step 3: Update
def update(centroids):
    for i in centroids.keys():
        centroids[i][0] = np.mean(df[df['closest'] == i]['x'])
        centroids[i][1] = np.mean(df[df['closest'] == i]['y'])
    return centroids

old_centroids = copy.deepcopy(centroids)
centroids = update(centroids)

# Plot updated centroids with arrows
fig = plt.figure(figsize=(5, 5))
ax = plt.axes()
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
    old_x, old_y = old_centroids[i]
    dx = (centroids[i][0] - old_x) * 0.75
    dy = (centroids[i][1] - old_y) * 0.75
    ax.arrow(old_x, old_y, dx, dy, head_width=2, head_length=3, fc=colmap[i], ec=colmap[i])
plt.title("Marvellous : Dataset with clustering and updated centroids")
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show()

# Repeat until convergence
while True:
    closest_centroids = df['closest'].copy(deep=True)
    centroids = update(centroids)
    df = assignment(df, centroids)
    if closest_centroids.equals(df['closest']):
        break

# Final plot
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in centroids.keys():
    plt.scatter(*centroids[i], color=colmap[i])
plt.title("Marvellous : Final dataset with set centroids")
plt.xlim(0, 80)
plt.ylim(0, 80)
plt.show()
