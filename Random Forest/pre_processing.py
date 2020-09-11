import numpy as nm
import matplotlib.pyplot as mtp
import pandas as pd
data_set= pd.read_csv('user_data.csv')
x= data_set.iloc[:, [2,3]].values
y= data_set.iloc[:, 4].values
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.25, random_state=0)
from sklearn.preprocessing import StandardScaler
st_x= StandardScaler()
x_train= st_x.fit_transform(x_train)
x_test= st_x.transform(x_test)
