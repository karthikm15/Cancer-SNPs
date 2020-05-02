# PCA on the Cancer SNPs
import matplotlib.pyplot as plt; plt.rcdefaults()
import pandas as pd 
import pdb 
from pandas.plotting import scatter_matrix
import matplotlib as mpl 
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
import numpy as np



df = pd.read_csv('all_snps_cancers_reduced.csv')
SNP = df['SNP']
x = StandardScaler().fit_transform(df.iloc[:,1:].values)
#x = pd.DataFrame(x, columns = ['PC1', 'PC2', 'PC3', 'PC4', 'PC5', 'PC6', 'PC7', 'PC8', 'PC9', 'PC10', 'PC11', 'PC12', 'PC13', 'PC14', 'PC15'])
pca = PCA(n_components=15)
principalComponents = pca.fit_transform(x)
principalComponents = pd.DataFrame(principalComponents, columns = ['PC1', 'PC2', 'PC3', 'PC4', 'PC5', 'PC6', 'PC7', 'PC8', 'PC9', 'PC10', 'PC11', 'PC12', 'PC13', 'PC14', 'PC15'])
principalComponents['SNP'] = SNP
principalComponents.to_csv('scaled_PCA_snp_cancers.csv')

objects = ('PC1', 'PC2', 'PC3', 'PC4', 'PC5', 'PC6', 'PC7', 'PC8', 'PC9', 'PC10', 'PC11', 'PC12', 'PC13', 'PC14', 'PC15')
y_pos = np.arange(len(objects))
performance = pca.explained_variance_ratio_
 
plt.bar(y_pos, performance, align='center', alpha=1)
plt.xticks(y_pos, objects)
plt.ylabel('Explained variance in percent')
plt.title('Variance Explained by PCA')
 
plt.show()

#df_beta = df_mean_imputed.loc[:,df_mean_imputed.columns.str.contains('beta')]
# equalizes the scale of all of the columns (converts to numpy matrix)
#x = StandardScaler().fit_transform(df_beta.loc[:, df_beta.columns != 'SNP'])
#pca = PCA(n_components= df_beta.shape[0])
#principalComponents = pca.fit_transform(x)
#columns = []
#for i in range(df_beta.shape[0]):
#	columns.append('principal component' + str(i))
#principalDf = pd.DataFrame(data = principalComponents, columns = columns)
#print(pca.explained_variance_ratio_)
