
import math 
import matplotlib as mpl
import numpy as np #library to import csv data
import matplotlib.pyplot as plt #library for visualization
import pylab
import pandas as pd

# data = np.genfromtxt('model_pellets.csv', delimiter=',', skip_header = 1)
data0 = pd.read_csv('output_0.csv')
data1 = pd.read_csv('output_1.csv')
data2 = pd.read_csv('output_2.csv')
# data3 = pd.read_csv('output_3.csv')

# convergence_degree = (np.log((data1['pellet-inlet-p']-data2['pellet-inlet-p'])/(data2['pellet-inlet-p']-data3['pellet-inlet-p']))/np.log(2))
# print(convergence_degree)
# zero_spacing_solution = (data3['pellet-inlet-p'] + (data3['pellet-inlet-p']-data2['pellet-inlet-p'])/(np.power(2, convergence_degree)-1))
# print(zero_spacing_solution)
# mesh_refinement_error_1 = np.absolute((zero_spacing_solution-data1['pellet-inlet-p'])/(zero_spacing_solution)*100)
# print(mesh_refinement_error_1)

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

# to plot numerical results withdifferent mesh refinemnt
plt.plot(data0['time'], data0['pellet-inlet-p'], '.', color='r', label = 'mesh refinement = 0')
plt.plot(data1['time'], data1['pellet-inlet-p'], '.', color='g', label = 'mesh refinement = 1')
plt.plot(data2['time'], data2['pellet-inlet-p'], '.', color='b', label = 'mesh refinement = 2')
plt.plot(data3['time'], data3['pellet-inlet-p'], '.', color='y', label = 'mesh refinement = 3')
plt.plot(data1['time'], zero_spacing_solution, '.', color='k', label = 'zero_spacing_solution')
plt.grid(which = 'major', axis = 'both', linestyle = '--')
plt.xlabel('time (s)')
plt.ylabel('inlet pressure (Pa)')
plt.xlim(0,20)
plt.ylim(0,5000000)
plt.legend()
plt.savefig('mesh_convergence_study')
plt.show()


# to plot the zero-grid-spacing solution






