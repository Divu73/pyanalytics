# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 23:22:52 2020

@author: divuk
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
flw=data('iris')
flw.head()
flw1=flw['Species']
flw1
flw.index
flw.columns
flw2=flw.drop('Species')
flw.drop?
