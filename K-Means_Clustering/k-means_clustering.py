import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# create dataset
# Gaussian dağılımı
# 1000 tane değerim olacak bunların ortalamasını aldığım zaman 25'i verecek
# ayrıca bu dataların 2/3'ü 20 ile 30 arasında olacak (25-5,25+5)
# class1
x1 = np.random.normal(25, 5, 1000)
y1 = np.random.normal(25, 5, 1000)
# class2
x2 = np.random.normal(55, 5, 1000)
y2 = np.random.normal(60, 5, 1000)
# class3
x3 = np.random.normal(55, 5, 1000)
y3 = np.random.normal(15, 5, 1000)

x = np.concatenate((x1, x2, x3), axis=0)
y = np.concatenate((y1, y2, y3), axis=0)

dictionary = {"x": x, "y": y}

data = pd.DataFrame(dictionary)
# data.info()
# data.describe()

# data görselleştirme
plt.scatter(x1, y1)
plt.scatter(x2, y2)
plt.scatter(x3, y3)
plt.show()
"""
# K-Means algoritması bunu görecek
plt.scatter(x1, y1, color="black")
plt.scatter(x2, y2, color="black")
plt.scatter(x3, y3, color="black")
plt.show()
"""

# K-Means Clustering
from sklearn.cluster import KMeans

wcss = []
for k in range(1, 15):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(data)
    wcss.append(kmeans.inertia_)  # inertia her K değeri için wcss değeri demektir.
plt.plot(range(1, 15), wcss)
plt.xlabel("Number of K value")
plt.ylabel("wcss")
plt.show()
# cluster sayımız 3 çıktı. elbow değeri 3 çıkıyor

# K = 3 için modelimiz
kmeans2 = KMeans(n_clusters=3)
clusters = kmeans2.fit_predict(data)  # fit et ve data üzerine uygula predict et
data["label"] = clusters  # data kısmına clustersleri label ismiyle ekliyoruz
plt.scatter(data.x[data.label == 0], data.y[data.label == 0], color="red")
plt.scatter(data.x[data.label == 1], data.y[data.label == 1], color="blue")
plt.scatter(data.x[data.label == 2], data.y[data.label == 2], color="green")

# centroid noktaları
plt.scatter(kmeans2.cluster_centers_[:, 0], kmeans2.cluster_centers_[:, 1], color="yellow")

plt.show()
