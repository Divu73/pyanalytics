# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 11:45:50 2020

@author: divuk
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pydataset import data
Cars=data('mtcars')
Cars
Cars.head()
Cars.tail()
Cars.index
Cars.columns
Cars1=Cars.wt
Cars1.head()

plt.scatter(x=Cars.mpg, y=Cars.wt,color='green',marker='X')
plt.plot();

Cars.carb.unique()
carbsum = Cars.groupby('carb').size()
plt.bar(x=['1','2','3','4','6','8'], height=carbsum, width=0.4,color='Pink')
plt.show();


plt.barh(y=Cars.gear, width=0.5,color='Yellow')
plt.show();
