import pdb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

plt.style.use('./presentation.mplstyle')

data = pd.read_csv('all_snps_cancers_reduced.csv')

columns_to_extract = [col for col in data.columns if 'beta.' in col]
SNP = data['SNP']
data_columns_extracted = data[columns_to_extract]

clusters = range(1, 20)
kmeans = [KMeans(n_clusters=i) for i in clusters]
score = [kmeans[i].fit(data_columns_extracted).score(data_columns_extracted) for i in range(len(kmeans))]
score
plt.plot(clusters, score)
plt.xlabel('Number of Clusters')
plt.ylabel('Score')
plt.title('Elbow Curve')
plt.show()

data_columns_extracted["cluster_label"] = kmeans[6].fit(data_columns_extracted).labels_
data_columns_extracted["SNP"] = SNP
data_columns_extracted.to_csv('all_snps_cancers_reduced_kmeans.csv', index = False)