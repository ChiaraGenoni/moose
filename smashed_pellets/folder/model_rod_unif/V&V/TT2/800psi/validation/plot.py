
import math 
import matplotlib as mpl
import numpy as np #library to import csv data
import matplotlib.pyplot as plt #library for visualization
import pylab
import pandas as pd

# data = np.genfromtxt('model_pellets.csv', delimiter=',', skip_header = 1)
data1 = pd.read_csv('model_pellets_out.csv')
# data2 = pd.read_csv('experimental_data.csv')
# square_error = (np.square((data1['pellet-inlet-p']-data2['inlet-p'])))
# mean_square_error = np.mean(square_error)
# RMSE = math.sqrt(mean_square_error)
# mean_square_value = np.mean(np.square(data1['inlet-p']))

# RRMSE = math.sqrt(mean_square_error/mean_square_value)*100


# theoretical_p = np.array(data1[2])
# experimental_p = np.array(data2[1])

# print(data1)
# print(data2)
# print(square_error)
# print(mean_square_error)
# print(RMSE)
# print(RRMSE)



plt.plot(data1['time'], data1['pellet-inlet-p'], 'o', color='g', label = 'P = 4.39 MPa')
# plt.plot(data2['time'], data2['inlet-p'], 'o', color='r', label = 'experimental')
plt.grid(which = 'major', axis = 'both', linestyle = '--')
plt.xlabel('time (s)')
plt.ylabel('inlet pressure (Pa)')
plt.xlim(0,30)
plt.ylim(0,5000000)
plt.legend()


plt.savefig('experiment_1')



plt.show()




