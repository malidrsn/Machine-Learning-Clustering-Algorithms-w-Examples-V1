# 1-) her data point cluster olarak görülür
# 2-) en yakın 2 data point alınıp 1 cluster yapılır
# 3-) en yakın 2 cluster alınıp 1  cluster yapılır
# 4-) return to step 3
# distance bakarak işlem yapılır. euclidean distance kullanılır
#   1-) en yakın 2 noktaya göre distance seç
#   2-) en uzak 2 noktaya göre distance seç
#   3-) mean'e göre distance seç
#   4-) centroid'e göre distance seç


# Hierarchical'da kullanılan dendogram nedir ?
# dendongram = her bir HC oluşturma stepini gösteren görselleştirmedir(plot'tur)
# iki data point için histogram çizmek gibi gösterilir.
# x ekseni = data points y ekseni = euclidean distance
# buna bağlı  olrak distance üzerinden bir threshold seçilir ve grafiği kesen nokta sayısına göre kaç tane clusterimiz olduğu belli olur
# en yüksek distance bakılır. kesilmeyen kısımlarından kesen noktalar belirlenir ve o sayıda cluster oluşturulur.

