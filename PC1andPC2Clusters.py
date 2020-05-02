import pdb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt; plt.rcdefaults()
from pandas.plotting import scatter_matrix
import matplotlib as mpl 
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer

principalComponents = pd.read_csv('scaled_PCA_snp_cancers.csv')
kmeans = pd.read_csv('all_snps_cancers_reduced_kmeans.csv')

df_merge = principalComponents.merge(kmeans, on='SNP')
df_merge.to_csv('all_snps_cancers_reduced_kmeans_PCA.csv')

plt.plot(principalComponents['PC1'], principalComponents['PC2'])
plt.xlabel('PC1')
plt.ylabel('PC2')