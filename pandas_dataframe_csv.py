# Machine learning the IRIS FLOWER set

import pandas as pd
import matplotlib.pyplot as plt                                                       # new

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)


print dataset.head
print '-----------'
print dataset.describe()
print '-----------'
print dataset.groupby('class').size()

#plot each feature separately
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)     # new
plt.show()                                                                            # new
