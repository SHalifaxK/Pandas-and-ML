#import dummy TESLA share data and manipulating it to suit for analysis


#imports
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style


#set matplotlib style so the grapf will look slitly better, from matplotlib import style
style.use('ggplot')

#read the Tesla data from a csv to pandas dataframe
data = pd.read_csv('C:/Users/kantomaa/TSLA.csv')

#making sublots using matplotlib, syntax for subplot2grid matplotlib.pyplot.subplot2grid(shape, loc, rowspan=1, colspan=1, **kwargs)
ax1 = plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
ax2 = plt.subplot2grid((6,1),(5,0),rowspan=5,colspan=1,sharex=ax1)

#plotting the data, data.index is the date
#also setting the index is just simply data.set_index['****']
ax1.plot(data.index, data['Open'])
ax2.plot(data.index, data['Close'])

plt.show()
