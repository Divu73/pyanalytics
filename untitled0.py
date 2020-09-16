# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 21:24:04 2020

@author: divuk
"""

#python : Topic :Decision Tree using mtcars

#standard libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns
df = data('mtcars')
df.head()
#from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn import metrics, tree
df['am'].value_counts()

#classification
#predict if transmission of car is 0 or 1 on basis of mpg, hp, wt
X1 = df[['mpg','hp','wt']]
Y1 = df['am']
Y1.value_counts()

#regression
#predict if mpg (numerical value) on basis of am, hp, wt
X2 = df[['am','hp','wt']]
Y2 = df[['mpg']]
np.mean(Y2)
from sklearn.model_selection import train_test_split
X1_train, X1_test, Y1_train, Y1_test = train_test_split(X1, Y1, test_size=.20, random_state=123 )
X1_train.shape
X1_test.shape
10/data2.shape[0]



from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X1, Y1)
yPred1=clf.predict(X1_test)
yPred1
Y1_test
df2 = pd.DataFrame({'Actual':Y1_test, 'Predicted': yPred1, 'diff':Y1_test-yPred1})
df2
df2.shape[0]