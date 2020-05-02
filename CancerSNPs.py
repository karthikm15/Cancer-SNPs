# Univariate Analysis


import pandas as pd 
import pdb 
from pandas.plotting import scatter_matrix
import matplotlib as mpl 
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
# loading the csv file into a dataframe
df = pd.read_csv('all_snps_cancers.csv')
# first step of data exploration
df.describe().to_csv('UnivariateAnalysis.csv') 
# deleting the columns with high missing values
deleted_columns = ['beta.Lung adenocarcinoma', 'se.Lung adenocarcinoma', 
                   'pval.Lung adenocarcinoma', 'beta.Cancer of urinary tract', 
                   'se.Cancer of urinary tract', 'pval.Cancer of urinary tract',
                   'beta.Neuroblastoma', 'se.Neuroblastoma', 'pval.Neuroblastoma',
                   'beta.Glioma', 'se.Glioma', 'pval.Glioma']
df = df.drop(columns = deleted_columns)
# Univariate Analysis Reduced (less missing values)
df.describe().to_csv("UnivariateAnalysisReduced.csv")
# New Dataset with the missing values (columns) removed
df.to_csv("all_snps_cancers_reduced.csv")
                   	