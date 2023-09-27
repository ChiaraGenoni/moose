
import math 
import matplotlib as mpl
import numpy as np #library to import csv data
import matplotlib.pyplot as plt #library for visualization
import pylab
import pandas as pd

# data = np.genfromtxt('model_pellets.csv', delimiter=',', skip_header = 1)
data1 = pd.read_csv('model_pellets_csv_05.csv')
data2 = pd.read_csv('model_pellets_csv_07_05.csv')
data3 = pd.read_csv('model_pellets_csv_04_05.csv')
data4 = pd.read_csv('model_pellets_csv_05_06.csv')
data5 = pd.read_csv('model_pellets_csv_05_07.csv')
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



#plt.plot(data1['time'], data1['pellet-inlet-p'], '.', color='g', label = 'porosity = 0.05')
# plt.plot(data4['time'], data4['pellet-inlet-p'], '.', color='k', label = 'porosity = 0.05-0.06')
# plt.plot(data3['time'], data3['pellet-inlet-p'], '.', color='b', label = 'porosity = 0.06-0.05')
plt.plot(data5['time'], data5['pellet-inlet-p'], '.', color='y', label = 'porosity = 0.05-0.07')
plt.plot(data2['time'], data2['pellet-inlet-p'], '.', color='r', label = 'porosity = 0.07-0.05')
plt.grid(which = 'major', axis = 'both', linestyle = '--')
plt.xlabel('time (s)')
plt.ylabel('inlet pressure (Pa)')
plt.xlim(0,200)
plt.ylim(0,5000000)
plt.legend()


# plt.savefig('non-uniform porosity')

# #plt.plot(data1['time'], data1['pellet-inlet-p'], 'o', color='g', label = 'porosity = 0.05')
# plt.plot(data4['time'], data4['pellet-inlet-p'], 'o', color='k', label = 'porosity = 0.05-0.04')
# plt.plot(data3['time'], data3['pellet-inlet-p'], 'o', color='b', label = 'porosity = 0.04-0.05')
# #plt.plot(data5['time'], data5['pellet-inlet-p'], 'o', color='y', label = 'porosity = 0.05-0.03')
# #plt.plot(data2['time'], data2['pellet-inlet-p'], 'o', color='r', label = 'porosity = 0.03-0.05')
# plt.grid(which = 'major', axis = 'both', linestyle = '--')
# plt.xlabel('time (s)')
# plt.ylabel('inlet pressure (Pa)')
# plt.xlim(0,50)
# plt.ylim(0,5000000)
# plt.legend()

plt.savefig('pellets permutation 2')



plt.show()




