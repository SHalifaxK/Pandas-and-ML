# Machine learning the IRIS FLOWER set

import pandas as pd
import matplotlib.pyplot as plt                                                       
import numpy as np

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)

#alternatively you can load the dataset directly from sklearn package                # new
#from sklearn.datasets import load_iris                                              # new
#dataset = load_iris()                                                               # new


print dataset.head
print '-----------'
print dataset.describe()
print '-----------'
print dataset.groupby('class').size()
print type(dataset)

#plot each feature separately

#dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)     
#plt.scatter(dataset.x,dataset.y)
#dataset.hist()
#plt.show()                                                                            

