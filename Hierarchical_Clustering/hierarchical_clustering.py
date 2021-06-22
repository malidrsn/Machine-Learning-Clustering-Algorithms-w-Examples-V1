import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# create dataset
# Gaussian dağılımı
# 1000 tane değerim olacak bunların ortalamasını aldığım zaman 25'i verecek
# ayrıca bu dataların 2/3'ü 20 ile 30 arasında olacak (25-5,25+5)
# class1
x1 = np.random.normal(25, 5, 100)
y1 = np.random.normal(25, 5, 100)
# class2
x2 = np.random.normal(55, 5, 100)
y2 = np.random.normal(60, 5, 100)
# class3
x3 = np.random.normal(55, 5, 100)
y3 = np.random.normal(15, 5, 100)

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

# dendongram çizdirme
# linkage = dendongram çizdirmek için gerekli algoritma (hierarchical clustering)
from scipy.cluster.hierarchy import linkage, dendrogram

# "ward" cluster içindeki yayılımları varyansları küçültecek minimize eder
merg = linkage(data, method="ward")  # HR algoritmasıdır metodudur.

dendrogram(merg, leaf_rotation=90)  # leaf_rotation = lifdeki sayıların rotasyonudur.
plt.xlabel("data points")
plt.ylabel("euclidean distance")
plt.show()
# dendrograma bakılarak kırmızı çizgi en yüksek mesafeye sahip ortadan threshold çekersek 3 nokta kesilir ve cluster sayımızı verir


# Hierarchical Clustering
from sklearn.cluster import AgglomerativeClustering  # tümevarım demektir dendrogramdan dolayı

hierarchical_cluster = AgglomerativeClustering(n_clusters=3, affinity="euclidean", linkage="ward")
clusters = hierarchical_cluster.fit_predict(data)
data["label"] = clusters  # dataya clustersları atamak

plt.scatter(data.x[data.label == 0], data.y[data.label == 0], color="red")
plt.scatter(data.x[data.label == 1], data.y[data.label == 1], color="blue")
plt.scatter(data.x[data.label == 2], data.y[data.label == 2], color="green")
plt.show()
