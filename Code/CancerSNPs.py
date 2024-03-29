# Univariate Analysis Performed


import pandas as pd 
import pdb 
from pandas.plotting import scatter_matrix
import matplotlib as mpl 
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
# loading the csv file into a dataframe
df = pd.read_csv('all_snps_cancers.csv')
# first step of data exploration
df.describe().to_csv('Univariate_Analysis.csv') 
# Univariate Analysis Reduced (less missing values)
df.describe().to_csv("Univariate_Analysis_Reduced.csv")
# New Dataset with the missing values (columns) removed
for i in df:
	for j in df[i]:
		if (j == "NaN" or j == "" or j == []):
			j = np.nan
#imp = SimpleImputer(missing_values = np.nan, strategy = "mean")
#imp.fit_transform(df)
df_beta = df.fillna(df.mean())
df_beta.to_csv("all_snps_cancers_reduced.csv", index = False)
                   	
