from ocean_data import read_netcdf_from_path, get_latitude_and_longitude, AEE

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np


netcdf_file = "tests/data/4903185_prof.nc"

netcdf_data = read_netcdf_from_path(netcdf_file)

variable_name_x = "TEMP"
variable_name_y = "PSAL"
temp = netcdf_data["TEMP"][0, :]
sal = netcdf_data["PSAL"][0, :]
pres = netcdf_data["PRES"][0, :]


aes_temp = AEE(temp)
aes_sal = AEE(sal)
aes_pres = AEE(pres)

#plt.plot(aes_temp, aes_sal, "*")
#plt.savefig("temp_vs_sal.png")

x = np.array([aes_temp, aes_sal]).T
sse = []
labels = []
silhouette_coefficients = []
for i in range(2,12):
    kmeans = KMeans(init="random", n_clusters=i, n_init=10, max_iter=300, random_state=0)
    kmeans.fit(x)
    sse.append(kmeans.inertia_)
    labels.append(kmeans.labels_)
    silhouette_coefficients.append(silhouette_score(x, kmeans.labels_))

print(silhouette_coefficients)

plt.style.use("fivethirtyeight")
plt.plot(range(2, 12),silhouette_coefficients)
plt.xticks(range(2, 12))
plt.xlabel("Number of Clusters")
plt.ylabel("Silhouette Coefficient")
plt.savefig("silhouette.png")

