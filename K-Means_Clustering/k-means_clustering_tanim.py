# label'ler yoktur.
# datalarımızın ne olduğu belli değildir.
# kümeleme yapılır
# her data point en yakın centroid'e (cluster) atanır. mesafeye bağlı olarak seçim yapılır. (distance )
# 1-)K değeri seçilir. grup sayısıdır. Random olarak centroid seçilir.(random nokta seçilir)
# 2-) random centroid ata
# 3-) data pointleri centroide göre uzaklığa bağlı olarak (euclidean) bak ve cluster yap
# 4-) bu centroidlerin yeri değişmeyene kadara yeni centroid bul ve ata

# K-means clustering evaulation
# metrik seçimi
"""
datalarımız kaç tane gruptan oluşuyor yani K = ?
** bunun için metriklerimiz var
1- ilk metriğimiz WCSS = within cluster sum of squares = Toplam(distance(Pi,CN)^2) = Pi in CN- Pi = point
WCSS düşük olmalıdır. bu yüzden K değerini yüksek seçmeliyiz. bunu ise elbow kuralına göre seçmeliyiz.
elbow kuralı = dirsek kuralı = azalan grafikte dirsek olan noktayı seç demektir. optimum K değerini verir
"""

