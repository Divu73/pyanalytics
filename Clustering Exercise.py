# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 19:21:33 2020

@author: divuk
"""

#clustering iris dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns
df = data('iris')
df.head()
df.Species.value_counts()
df.head()
df.drop('Species')
df1=df.select_dtypes(exclude=['object'])
df1.head()
from sklearn.cluster import KMeans
KMeans=KMeans(n_clusters=3)
KMeans.fit(df1)
KMeans.inertia_
KMeans.cluster_centers_
KMeans.labels_
df1.shape
KMeans.n_iter_
KMeans.predict(df1)
pd.DataFrame(df1).head()
df1[0:5]

df1.columns
NCOLS = df1.columns 
#['ApplicantIncome','CoapplicantIncome','LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area']
NCOLS
clusterNos = KMeans.labels_
clusterNos
type(clusterNos)
df1
df1.groupby([clusterNos]).mean()

pd.options.display.max_columns =None#can't understand
df1.columns
plt.scatter(df1['Sepal.Length'],['Sepal.Width'],['Petal.Length'])
plt.scatter(data2.ApplicantIncome, data2.Credit_History, c=clusterNos) #better distinction
plt.scatter(data2.ApplicantIncome, data2.Loan_Amount_Term, c=clusterNos) #better distinction


#hierarchical clustering
import scipy.cluster.hierarchy as shc
dend = shc.dendrogram(shc.linkage(data2_scaled, method='ward'))

plt.figure(figsize = (10,7))
plt.title("Dendrogram")
dend = shc.dendrogram(shc.linkage(data2_scaled, method='ward'))
plt.axhline(y=6, color='r', linestyle='--')
plt.show();

from sklearn.cluster import AgglomerativeClustering
aggCluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='ward')
aggCluster.fit_predict(data2_scaled)
aggCluster
aggCluster.labels_

#compare
compare = pd.DataFrame({'kmCluster': kmeans.labels_, 'HCaggl': aggCluster.labels_, 'Diff': kmeans.labels_ - aggCluster.labels_})
compare
compare.Diff.sum()
compare.kmCluster.value_counts()
compare.HCaggl.value_counts()

#Customer Segmentation
#Product Segmentation