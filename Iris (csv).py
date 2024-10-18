#Iris Dataset em csv

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils

base = pd.read_csv('iris.data')
base.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']

entradas = base.iloc[:,0:4].values
saidas = base.iloc[:,4].values

labelencoder = LabelEncoder()
saidas = labelencoder.fit_transform(saidas)
saidas_dummy = np_utils.to_categorical(saidas)