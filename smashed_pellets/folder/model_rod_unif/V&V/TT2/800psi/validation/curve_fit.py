import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd


# create scattered plot

data1 = pd.read_csv('model_pellets_out.csv')
data2 = np.delete(data1, [0, 1, 2, 3], 0)
print(data2)
time = np.array(data2[:,0])
pressure = np.array(data2[:,1]-101325)
# print(time)
# print(pressure)




# # def func(x, a, b, c): return a*np.exp(-b*x) + c

def func(x, a, b): return a*np.exp(b*x)

popt, pcov = curve_fit(func, time, pressure, maxfev=1700000)

print(popt)
print(pcov)

a = popt[0]
b = popt[1]

# # c = popt[2]


plt.plot(time, func(time, a, b) , label="Fitted Curve")
plt.plot(time, pressure, '.', color='g', label = 'data')
plt.grid(which = 'major', axis = 'both', linestyle = '--')
plt.xlabel('time (s)')
plt.ylabel('inlet pressure (Pa)')
plt.xlim(0,30)
plt.ylim(0, 3000000)
plt.legend()
plt.show()


