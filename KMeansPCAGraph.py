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

principalComponents = pd.read_csv('scaled_PCA_snp_cancers.csv')
principalComponents = principalComponents.loc[principalComponents['SNP'] != 'rs4532479',:]
kmeans = pd.read_csv('all_snps_cancers_reduced_kmeans.csv')
kmeans = kmeans.loc[kmeans['SNP'] != 'rs4532479',:]

df_merge = principalComponents.merge(kmeans, on='SNP')
df_merge.to_csv('all_snps_cancers_reduced_kmeans_PCA.csv')

plt.xlabel('PC1')
plt.ylabel('PC2')

plt.scatter(df_merge['PC1'], df_merge['PC2'], c = df_merge['cluster_label'], linewidths = 0, cmap = "Set1", linestyle = 'None')
plt.show()

plt.xlabel('PC1')
plt.ylabel('PC3')

plt.scatter(df_merge['PC1'], df_merge['PC3'], c = df_merge['cluster_label'], linewidths = 0, cmap = "Set1", linestyle = 'None')
plt.show()

plt.xlabel('PC2')
plt.ylabel('PC3')

plt.scatter(df_merge['PC2'], df_merge['PC3'], c = df_merge['cluster_label'], linewidths = 0, cmap = "Set1", linestyle = 'None')
plt.show()