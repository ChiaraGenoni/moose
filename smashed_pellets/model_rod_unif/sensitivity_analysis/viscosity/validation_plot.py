import matplotlib as mpl
import math
import numpy as np #library to import csv data
import matplotlib.pyplot as plt #library for visualization
import pylab
import pandas as pd
import scipy.optimize
import scipy.stats



# temperatures = [300, 500, 700, 900, 1100, 1200]
# viscosities = [1.9271e-5, 2.2099e-5, 2.6691e-5, 3.3621e-5, 4.3257e-5, 4.9497e-5]

# plt.plot(temperatures, viscosities, marker='o', linestyle='-', color='b')
# plt.xlabel('Temperature (K)')
# plt.ylabel('Dynamic Viscosity (kg/(m*s))')
# plt.title('Dynamic Viscosity of Air')
# plt.grid(True)
# plt.show()
# plt.savefig('Dynamic Viscosity of Air')


# data = np.genfromtxt('model_pellets.csv', delimiter=',', skip_header = 1)
data0 = pd.read_csv('stochastic_tools_out_runner0.csv')
data1 = pd.read_csv('stochastic_tools_out_runner1.csv') 
data2 = pd.read_csv('stochastic_tools_out_runner2.csv')
data3 = pd.read_csv('stochastic_tools_out_runner3.csv')
data4 = pd.read_csv('stochastic_tools_out_runner4.csv')
data5 = pd.read_csv('stochastic_tools_out_runner5.csv')
data6 = pd.read_csv('stochastic_tools_out_runner6.csv')
data7 = pd.read_csv('stochastic_tools_out_runner7.csv')
data8 = pd.read_csv('stochastic_tools_out_runner8.csv')
data9 = pd.read_csv('stochastic_tools_out_runner9.csv')


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
print(f"time_scale0 = {time_scale4}s")
# print(f"R² = {rSquared}")



def monoExp(x, m, t, b):
    return m*np.exp(-t*x) + b

# perfomr the fit 
p0 = (4200000, 0.5, 101325)
params, cv = scipy.optimize.curve_fit(monoExp, data6['time'], data6['inlet-p'], p0)
m, x, b = params
sampleRate = 20_000
tauSec = (1 / x) / sampleRate
time_scale6 = 5/x

# determine quality of the fit
squaredDiffs = np.square(data6['inlet-p'] - monoExp(data6['time'], m, x, b))
squaredDiffsFromMean = np.square(data6['inlet-p'] - np.mean(data6['inlet-p']))
rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)

# inspect the parameters
# print(f"Y = {m} * e^(-{x} * t) + {b}")
print(f"time_scale0 = {time_scale6}s")
# print(f"R² = {rSquared}")




def monoExp(x, m, t, b):
    return m*np.exp(-t*x) + b

# perfomr the fit 
p0 = (4200000, 0.5, 101325)
params, cv = scipy.optimize.curve_fit(monoExp, data8['time'], data8['inlet-p'], p0)
m, x, b = params
sampleRate = 20_000
tauSec = (1 / x) / sampleRate
time_scale8 = 5/x

# determine quality of the fit
squaredDiffs = np.square(data8['inlet-p'] - monoExp(data8['time'], m, x, b))
squaredDiffsFromMean = np.square(data8['inlet-p'] - np.mean(data8['inlet-p']))
rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)

# inspect the parameters
# print(f"Y = {m} * e^(-{x} * t) + {b}")
print(f"time_scale0 = {time_scale8}s")
# print(f"R² = {rSquared}")


def monoExp(x, m, t, b):
    return m*np.exp(-t*x) + b

# perfomr the fit 
p0 = (4200000, 0.5, 101325)
params, cv = scipy.optimize.curve_fit(monoExp, data9['time'], data9['inlet-p'], p0)
m, x, b = params
sampleRate = 20_000
tauSec = (1 / x) / sampleRate
time_scale9 = 5/x

# determine quality of the fit
squaredDiffs = np.square(data9['inlet-p'] - monoExp(data9['time'], m, x, b))
squaredDiffsFromMean = np.square(data9['inlet-p'] - np.mean(data9['inlet-p']))
rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)

# inspect the parameters
# print(f"Y = {m} * e^(-{x} * t) + {b}")
print(f"time_scale9 = {time_scale9}s") 
# print(f"R² = {rSquared}")

# compute Pearson coefficient
output = np.array([time_scale0, time_scale2, time_scale4, time_scale6, time_scale8, time_scale9])
input = np.array([300, 500, 700, 900, 1100, 1200])
pearson = scipy.stats.pearsonr(input, output)


# compute OAT sensitivity coefficient
OAT = (time_scale0-time_scale9)/time_scale0*300/(300-1200)*100

print(pearson)
print(OAT)






plt.plot(data0['time'], data0['inlet-p'], '.', color='C1', label = '300 K')
# plt.plot(data1['time'], data1['inlet-p'], '.', color='g', label = '400 K')
plt.plot(data2['time'], data2['inlet-p'], '.', color='C2', label = '500 K')
# plt.plot(data3['time'], data3['inlet-p'], '.', color='b', label = '600 K')
plt.plot(data4['time'], data4['inlet-p'], '.', color='C3', label = '700 K')
# plt.plot(data5['time'], data5['inlet-p'], '.', color='r', label = '800 K')
plt.plot(data6['time'], data6['inlet-p'], '.', color='C4', label = '900 K')
# plt.plot(data7['time'], data7['inlet-p'], '.', color='g', label = '1000 K')
plt.plot(data8['time'], data8['inlet-p'], '.', color='C5', label = '1100 K')
plt.plot(data9['time'], data9['inlet-p'], '.', color='C6', label = '1200 K')



plt.grid(which = 'major', axis = 'both', linestyle = '--')
plt.xlabel('time (s)')
plt.ylabel('pressure (Pa)')
plt.xlim(0,30)
plt.ylim(0,5000000)
plt.legend(title = 'Viscosity @ T')


plt.savefig('viscosity')



plt.show()




