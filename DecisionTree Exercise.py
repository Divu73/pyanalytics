# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 13:51:38 2020

@author: divuk
"""

import numpy as np
import pandas as pd
from pydataset import data
import matplotlib.pyplot as plt
car=data('mtcars')
car
car.columns
car.index
car.head()
car.tail()

x=car.drop('am', axis=1)
x
x.columns
y=car['am']
y
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test= train_test_split(x,y,test_size=.2)
x_train.shape
x_test.shape

from sklearn.tree import DecisionTreeClassifier
Model=DecisionTreeClassifier()
Model.fit(x_train,y_train)
