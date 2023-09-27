

import matplotlib as mpl
import numpy as np #library to import csv data
import matplotlib.pyplot as plt #library for visualization
import pylab
import pandas as pd

# data = np.genfromtxt('model_pellets.csv', delimiter=',', skip_header = 1)
data1 = pd.read_csv('model_pellets.csv')
data2 = pd.read_csv('experimental_data.csv')

print(data1)
print(data2)



# plt.plot(data[0], data[2], 'o', color='g', label = 'theoretical')
plt.plot(data1['time'], data1['inlet-p'], 'o', color='g', label = 'theoretical')
plt.plot(data2['time'], data2['inlet-p'], 'o', color='r', label = 'experimental')
plt.grid(which = 'major', axis = 'both', linestyle = '--')
plt.xlabel('time (s)')
plt.ylabel('pressure (Pa)')
plt.legend()


plt.savefig('plot')

# plt.show()




