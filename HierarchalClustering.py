import pdb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt; plt.rcdefaults()
from pandas.plotting import scatter_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
from scipy.cluster import hierarchy
from scipy.cluster.hierarchy import fcluster


data = pd.read_csv('all_snps_cancers_reduced.csv')
columns_to_extract = [col for col in data.columns if 'beta.' in col]
SNP = data['SNP']
data_columns_extracted = data[columns_to_extract]

# Creates a table with the different clusters (represents the dendogram)
Z = hierarchy.linkage(data_columns_extracted, 'complete')
# Graphical representation of the dendogram
dn = hierarchy.dendrogram(Z)

plt.show()

# Taking only the first twenty clusters (negative becuse the matrix is inverse)
last = Z[-20:, 2]
# Reverse the list
last_rev = last[::-1]
# Naming the number of clusters
idxs = np.arange(1, len(last)+1)
# Plotting idxs (names) and last_rev (dendogram - 20)
plt.plot(idxs, last_rev)
plt.xlabel('Number of Clusters')
# Merge distance is the score
plt.ylabel('Merge Distance') 
plt.suptitle('Merge Distance and Number of Clusters')

plt.show()

k = 8 # determined from the plot
labels = fcluster(Z, k, criterion='maxclust')
data_columns_extracted["cluster_label"] = labels

data_columns_extracted.to_csv('all_snps_cancers_reduced_hierarchical_clustering.csv')