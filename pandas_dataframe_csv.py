# Machine learning the IRIS FLOWER set

import pandas as pd


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)


print dataset.head
print '-----------'
print dataset.describe()
print '-----------'
print dataset.groupby('class').size()
