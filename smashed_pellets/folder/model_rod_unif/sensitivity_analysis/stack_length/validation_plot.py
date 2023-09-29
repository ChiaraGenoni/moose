import matplotlib as mpl
import math
import numpy as np #library to import csv data
import matplotlib.pyplot as plt #library for visualization
import pylab
import pandas as pd
import scipy.optimize

# data = np.genfromtxt('model_pellets.csv', delimiter=',', skip_header = 1)
data0 = pd.read_csv('stochastic_tools_out_runner0.csv')
data1 = pd.read_csv('stochastic_tools_out_runner1.csv')
data2 = pd.read_csv('stochastic_tools_out_runner2.csv')
data3 = pd.read_csv('stochastic_tools_out_runner3.csv')
data4 = pd.read_csv('stochastic_tools_out_runner4.csv')


def monoExp(x, m, t, b):
    return m*np.exp(-t*x) + b

# perfomr the fit 
p0 = (4200000, 0.5, 101325)
params, cv = scipy.optimize.curve_fit(monoExp, data0['time'], data0['inlet-p'], p0)
m, x, b = params
sampleRate = 20_000
tauSec = (1 / x) / sampleRate
time_scale0 = 5/x

# determine quality of the fit
squaredDiffs = np.square(data0['inlet-p'] - monoExp(data0['time'], m, x, b))
squaredDiffsFromMean = np.square(data0['inlet-p'] - np.mean(data0['inlet-p']))
rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)

# inspect the parameters
# print(f"Y = {m} * e^(-{x} * t) + {b}")
print(f"time_scale0 = {time_scale0}s")
# print(f"R² = {rSquared}")



def monoExp(x, m, t, b):
    return m*np.exp(-t*x) + b

# perfomr the fit 
p0 = (4200000, 0.5, 101325)
params, cv = scipy.optimize.curve_fit(monoExp, data1['time'], data1['inlet-p'], p0)
m, x, b = params
sampleRate = 20_000
tauSec = (1 / x) / sampleRate
time_scale1 = 5/x

# determine quality of the fit
squaredDiffs = np.square(data1['inlet-p'] - monoExp(data1['time'], m, x, b))
squaredDiffsFromMean = np.square(data1['inlet-p'] - np.mean(data1['inlet-p']))
rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)

# inspect the parameters
# print(f"Y = {m} * e^(-{x} * t) + {b}")
print(f"time_scale0 = {time_scale1}s")
# print(f"R² = {rSquared}")




def monoExp(x, m, t, b):
    return m*np.exp(-t*x) + b

# perfomr the fit 
p0 = (4200000, 0.5, 101325)
params, cv = scipy.optimize.curve_fit(monoExp, data2['time'], data2['inlet-p'], p0)
m, x, b = params
sampleRate = 20_000
tauSec = (1 / x) / sampleRate
time_scale2 = 5/x

# determine quality of the fit
squaredDiffs = np.square(data2['inlet-p'] - monoExp(data2['time'], m, x, b))
squaredDiffsFromMean = np.square(data2['inlet-p'] - np.mean(data2['inlet-p']))
rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)

# inspect the parameters
# print(f"Y = {m} * e^(-{x} * t) + {b}")
print(f"time_scale0 = {time_scale2}s")
# print(f"R² = {rSquared}")




def monoExp(x, m, t, b):
    return m*np.exp(-t*x) + b

# perfomr the fit 
p0 = (4200000, 0.5, 101325)
params, cv = scipy.optimize.curve_fit(monoExp, data3['time'], data3['inlet-p'], p0)
m, x, b = params
sampleRate = 20_000
tauSec = (1 / x) / sampleRate
time_scale3 = 5/x

# determine quality of the fit
squaredDiffs = np.square(data3['inlet-p'] - monoExp(data3['time'], m, x, b))
squaredDiffsFromMean = np.square(data3['inlet-p'] - np.mean(data3['inlet-p']))
rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)

# inspect the parameters
# print(f"Y = {m} * e^(-{x} * t) + {b}")
print(f"time_scale0 = {time_scale3}s")
# print(f"R² = {rSquared}")





def monoExp(x, m, t, b):
    return m*np.exp(-t*x) + b

# perfomr the fit 
p0 = (4200000, 0.5, 101325)
params, cv = scipy.optimize.curve_fit(monoExp, data4['time'], data4['inlet-p'], p0)
m, x, b = params
sampleRate = 20_000
tauSec = (1 / x) / sampleRate
time_scale4 = 5/x

# determine quality of the fit
squaredDiffs = np.square(data4['inlet-p'] - monoExp(data4['time'], m, x, b))
squaredDiffsFromMean = np.square(data4['inlet-p'] - np.mean(data4['inlet-p']))
rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)

# inspect the parameters
# print(f"Y = {m} * e^(-{x} * t) + {b}")
print(f"time_scale4 = {time_scale4}s")
# print(f"R² = {rSquared}")

output = np.array([time_scale0, time_scale1, time_scale2, time_scale3, time_scale4])
input = np.array([31.76, 39.7, 47.64, 55.58, 63.52])
num = 5*np.sum(output*input)-np.sum(output)*np.sum(input)
den = math.sqrt((5*np.sum(np.power(output,2))-(np.sum(output))**2)*5*np.sum(np.power(input,2))-(np.sum(input))**2)
r = num/den
print(r)




# plt.plot(data0['time'], data0['inlet-p'], '.', color='C1', label = '4')
# plt.plot(data1['time'], data1['inlet-p'], '.', color='C2', label = '5')
# plt.plot(data2['time'], data2['inlet-p'], '.', color='C3', label = '6')
# plt.plot(data3['time'], data3['inlet-p'], '.', color='C4', label = '7')
# plt.plot(data4['time'], data4['inlet-p'], '.', color='C5', label = '8')



# plt.grid(which = 'major', axis = 'both', linestyle = '--')
# plt.xlabel('time (s)')
# plt.ylabel('pressure (Pa)')
# plt.xlim(0,30)
# plt.ylim(0,5000000)
# plt.legend(title = '# of pellets')


# plt.savefig('fuel_rod_length')



# plt.show()




