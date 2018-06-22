# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 10:53:06 2018

@author: Mitali
"""

import numpy as np
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from sklearn.utils.extmath import safe_sparse_dot
from time import time

t0 = time()
with open('D:\\Mitali\\ML\\airplane_data\\2016-06-20-0001Z.json') as f:
   data = json.load(f)
df = pd.DataFrame(data['acList'])
features = ['Alt', 'AltT', 'EngMount', 'EngType', 'Engines', 'GAlt', 'Gnd', 'InHg', 'Lat', 'Long', 'Mil', 'Mlat', 'Spd', 'SpdTyp', 'Species', 'TT', 'Trak', 'TrkH', 'Vsi', 'VsiT', 'WTC']
for col in df:
    num = df[col].isnull().sum()
    if(num > 1000):
        df = df.drop(col, axis=1)
    elif(col not in features):
        df = df.drop(col, axis=1)
#df = df.dropna(axis=0)
df = df[df.Spd < 666]
df = df[df.Alt < 50000]


x0_train = df.Alt[:3000]
y_train = df.Spd[:3000]
x0_test = df.Alt[3000:]
y_test = df.Spd[3000:]
x0_test = x0_test[:,np.newaxis]
x0_train = x0_train[:,np.newaxis]
x0_test.sort(axis=0)
clf = linear_model.LinearRegression()
clf.fit(x0_train,y_train)
y = clf.predict(x0_test)
s = "y = " + str(clf.coef_[0]) + "x + " + str(clf.intercept_)
plt.title(s)
plt.scatter(x0_train, y_train)
plt.scatter(x0_test,y_test,color='k')
plt.plot(x0_test,y,color='k')
print (time() - t0)