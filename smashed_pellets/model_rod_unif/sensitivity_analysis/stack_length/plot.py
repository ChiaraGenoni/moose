
import math 
import matplotlib as mpl
import numpy as np #library to import csv data
import matplotlib.pyplot as plt #library for visualization
import pylab
import pandas as pd

# data = np.genfromtxt('model_pellets.csv', delimiter=',', skip_header = 1)
data1 = pd.read_csv('stochastic_tools_out_runner0.csv')
data2 = pd.read_csv('stochastic_tools_out_runner1.csv')
data3 = pd.read_csv('stochastic_tools_out_runner2.csv')
data4 = pd.read_csv('stochastic_tools_out_runner3.csv')
data5 = pd.read_csv('stochastic_tools_out_runner4.csv')
data6 = pd.read_csv('stochastic_tools_out_runner5.csv')
data7 = pd.read_csv('stochastic_tools_out_runner6.csv')
data8 = pd.read_csv('stochastic_tools_out_runner7.csv')
data9 = pd.read_csv('stochastic_tools_out_runner8.csv')
data10 = pd.read_csv('stochastic_tools_out_runner9.csv')

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
# print(mean_square_error)ß
# print(RMSE)
# print(RRMSE)


# plt.plot(data1['time'], data1['pellet-inlet-p'], '.', color='g', label='1e-5 Pa s')
# plt.plot(data2['time'], data2['pellet-inlet-p'], '.', color='r', label='1.5e-5 Pa s')
# plt.plot(data3['time'], data3['pellet-inlet-p'], '.', color='y', label='2e-5 Pa s')
# plt.plot(data4['time'], data4['pellet-inlet-p'], '.', color='b', label='2.5e-5 Pa s')
# plt.plot(data5['time'], data5['pellet-inlet-p'], '.', color='k', label='3e-5 Pa s')
# plt.plot(data6['time'], data6['pellet-inlet-p'], '.', color='c', label='3.5e-5 Pa s')
# plt.plot(data7['time'], data7['pellet-inlet-p'], '.', color='m', label='4e-5 Pa s')
# plt.plot(data8['time'], data8['pellet-inlet-p'], '.', color='C0', label='4.5e-5 Pa s')
# plt.plot(data9['time'], data9['pellet-inlet-p'], '.', color='C1', label='5e-5 Pa s')

# plt.plot(data1['time'], data1['pellet-inlet-p'], '.', color='g', label ='0.01')
# plt.plot(data2['time'], data2['pellet-inlet-p'], '.', color='r', label='0.02')
# plt.plot(data3['time'], data3['pellet-inlet-p'], '.', color='y', label='0.03')
# plt.plot(data4['time'], data4['pellet-inlet-p'], '.', color='b', label='0.04')
plt.plot(data5['time'], data5['pellet-inlet-p'], '.', color='k', label='0.05')
plt.plot(data6['time'], data6['pellet-inlet-p'], '.', color='c', label='0.06')
plt.plot(data7['time'], data7['pellet-inlet-p'], '.', color='m', label='0.07')
plt.plot(data8['time'], data8['pellet-inlet-p'], '.', color='C0', label='0.08')
plt.plot(data9['time'], data9['pellet-inlet-p'], '.', color='C1', label='0.09')
# plt.plot(data10['time'], data10['pellet-inlet-p'], '.', color='C2', label='0.1')


plt.grid(which = 'major', axis = 'both', linestyle = '--')
plt.xlabel('time (s)')
plt.ylabel('inlet_pressure (Pa)')
plt.xlim(0,150)
plt.ylim(0,5000000)
plt.legend(title = 'porosity')


# plt.savefig('viscosity')
plt.savefig('porosity')




plt.show()




