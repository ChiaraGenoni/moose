import matplotlib.pyplot as plt
import math 
import matplotlib as mpl
import numpy as np #library to import csv data
import matplotlib.pyplot as plt #library for visualization
import pylab
import pandas as pd
import scipy.optimize 





def time_scale(gap_thickness):
    d_cladding = 0.00824
    hydraulic_diameter = 2*gap_thickness
    P = 101325
    fuel_length = 0.00794*4
    air_viscosity = 0.0000181
    plenum_volume = math.pi*(0.0254*6-fuel_length)*d_cladding**2/4
    decay_constant = math.pi*hydraulic_diameter**4*P/(128*air_viscosity*fuel_length*plenum_volume)
    tau = 5/decay_constant
    return tau



gap_thickness = np.linspace(0.00002, 0.0001, 100)
gap = gap_thickness*1e6

plt.plot(gap, time_scale(gap_thickness), linestyle='-', color='b')
plt.ylabel('time scale (s)')
plt.xlabel('gap (micron)')
plt.xlim(0,100)
# plt.yscale('log')
plt.title('time-scale vs. gap thickness')
plt.grid(True)
plt.show()  



# def pressure(time):
#     decay_constant = 
#     delta_P = (4300000-101325)
#     P = 101325+delta_P*math.pow(math.e, -decay_constant*time)
#     return P
    

# t = np.linspace(0, 40, 40)
# plt.plot(t, pressure(t), marker='o', color='C1', title='analytical solution')





# time_scale = np.array([7.05E-02, 8.08E-02, 9.30E-02, 1.08E-01, 1.25E-01, 1.47E-01, 1.73E-01, 2.05E-01, 2.45E-01, 2.95E-01, 3.59E-01, 4.42E-01, 5.49E-01, 6.91E-01, 8.82E-01, 1.14E+00, 1.51E+00, 2.04E+00, 2.81E+00, 3.99E+00, 5.87E+00, 8.98E+00, 1.45E+01, 2.49E+01, 4.65E+01, 9.78E+01, 2.44E+02, 7.97E+02, 4.33E+03])
# hydraulic_diameter = np.array([0.000299, 0.000289, 0.000279, 0.000269, 0.000259, 0.000249, 0.000239, 0.000229, 0.000219, 0.000209, 0.000199, 0.000189, 0.000179, 0.000169, 0.000159, 0.000149, 0.000139, 0.000129, 0.000119, 0.000109, 9.9E-05, 8.9E-05, 7.9E-05, 6.9E-05, 5.9E-05, 4.9E-05, 3.9E-05, 2.9E-05, 1.9E-05])
# gap = hydraulic_diameter/2*1E6
# increment = np.array([1.344518953, 14.57592768, 15.12630283, 15.71980498, 16.36170166, 17.05815317, 17.81640985, 18.64506386, 19.55437406, 20.55668984, 21.66701099, 22.90373721, 24.28968655, 25.85350221, 27.63163161, 29.67116827, 32.034028, 34.80324907, 38.0927873, 42.06328531, 46.94851897, 53.10196045, 61.08372406, 71.83514836, 87.0631815, 110.1956512, 149.1872929, 227.0893747, 442.7222013])

# plt.plot(gap, time_scale, marker='o', linestyle='-', color='b')
# plt.ylabel('time scale (s)')
# plt.xlabel('gap (micron)')
# plt.title('time_scale vs. gap')
# plt.grid(True)
# plt.show()

# plt.plot(gap, increment, marker='o', linestyle='-', color='g')
# plt.ylabel('increment (%)')
# plt.xlabel('gap (micron)')
# plt.title('increment vs. gap')
# plt.grid(True)
# plt.show()




# def calculate_knudsen_number(T, P, L):
#     k = 1.380649e-23  # Boltzmann's constant
#     d = 3.46e-10  # Molecular diameter of air

#     mean_free_path = (k * T) / (np.sqrt(2) * np.pi * d**2 * P)
#     knudsen_number = mean_free_path / L

#     return knudsen_number

# # Define the range of pressure and characteristic length
# pressure_range = np.linspace(1e5, 7e6, 100)  # Pressure range from 100 kPa to 10 MPa
# length_range = np.linspace(10e-6, 200e-6, 100)  # Characteristic length range from 1 µm to 1 mm

# # Create a grid of pressure and length values
# P, L = np.meshgrid(pressure_range, length_range)

# # Calculate the Knudsen number for each combination of pressure and length
# T = 300  # Temperature in Kelvin
# knudsen_numbers = calculate_knudsen_number(T, P, L)

# # Plot the Knudsen number as a contour plot
# plt.figure(figsize=(8, 6))
# plt.contourf(P, L, knudsen_numbers, levels=100, cmap='viridis')
# plt.colorbar(label='Knudsen Number')
# plt.xscale('log')
# plt.yscale('log')
# plt.xlabel('Pressure (Pa)')
# plt.ylabel('Characteristic Length (m)')
# plt.title('Knudsen Number')
# plt.grid(True)
# # plt.show()





# to fit the exponential curve on the experimental data

# data1 = pd.read_csv('4_3_experimental_data.csv')
# data2 = pd.read_csv('5_7_experimental_data.csv')
# data3 = pd.read_csv('7_0_experimental_data.csv')


# def monoExp1(x, t):
#     return (4300000-101325)*np.exp(-t*x) + 101325

# perfomr the fit 
# p0 = (0.5)
# params, cv = scipy.optimize.curve_fit(monoExp1, data1['time'], data1['inlet-p'], p0)
# x = params
# sampleRate = 20_000
# tauSec = (1 / x) / sampleRate
# viscosity = 0.0000181
# L = 0.03176
# D_cladding = 0.00833
# D_fuel = 0.00794
# delta_P = 4198675
# Area = math.pi*(D_cladding**2-D_fuel**2)/4
# V = D_cladding**2*(0.0254*6-L)
# hydraulic_diameter = math.sqrt(params*4*128*viscosity*L*V/(3.14*(Area)*delta_P))
# gap_thickness = hydraulic_diameter/2
# print(f"decay_constant={params}")
# print(f"gap_thickness={gap_thickness}")

# determine quality of the fit
# squaredDiffs = np.square(data1['inlet-p'] - monoExp1(data1['time'], x))
# squaredDiffsFromMean = np.square(data1['inlet-p'] - np.mean(data1['inlet-p']))
# rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)
# print(f"R² = {rSquared}")





# def monoExp2(x, t):
#     return (5715936-101325)*np.exp(-t*x) + 101325

# perfomr the fit 
# p0 = (0.5)
# params, cv = scipy.optimize.curve_fit(monoExp2, data2['time'], data2['inlet-p'], p0)
# x = params
# sampleRate = 20_000
# tauSec = (1 / x) / sampleRate
# viscosity = 0.0000181
# L = 0.03176
# D_cladding = 0.00833
# D_fuel = 0.00794
# delta_P = 5715936-101325
# Area = math.pi*(D_cladding**2-D_fuel**2)/4
# V = D_cladding**2*(0.0254*6-L)
# hydraulic_diameter = math.sqrt(params*4*128*viscosity*L*V/(3.14*(Area)*delta_P))
# gap_thickness = hydraulic_diameter/2
# print(f"decay_constant={params}")
# print(f"gap_thickness={gap_thickness}")

# # determine quality of the fit
# squaredDiffs = np.square(data2['inlet-p'] - monoExp2(data2['time'], x))
# squaredDiffsFromMean = np.square(data2['inlet-p'] - np.mean(data2['inlet-p']))
# rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)
# print(f"R² = {rSquared}") 






# def monoExp3(x, t):
#     return (6989190-101325)*np.exp(-t*x) + 101325

# # perfomr the fit 
# p0 = (0.5)
# params, cv = scipy.optimize.curve_fit(monoExp3, data3['time'], data3['inlet-p'], p0)
# x = params
# sampleRate = 20_000
# tauSec = (1 / x) / sampleRate
# viscosity = 0.0000181
# L = 0.03176
# D_cladding = 0.00833 
# D_fuel = 0.00794
# delta_P = 6989190-101325
# Area = math.pi*(D_cladding**2-D_fuel**2)/4
# V = D_cladding**2*(0.0254*6-L)
# hydraulic_diameter = math.sqrt(params*4*128*viscosity*L*V/(3.14*(Area)*delta_P))
# gap_thickness = hydraulic_diameter/2
# print(f"decay_constant={params}")
# print(f"gap_thickness={gap_thickness}")

# # determine quality of the fit
# squaredDiffs = np.square(data3['inlet-p'] - monoExp3(data3['time'], x))
# squaredDiffsFromMean = np.square(data3['inlet-p'] - np.mean(data3['inlet-p']))
# rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)
# print(f"R² = {rSquared}")





# plot the curve

# plt.plot(data1['time'], data1['inlet-p'], marker='o', color='C1', label='4.3 MPa darcy_curve')
# plt.plot(data1['time'], monoExp1(params,data1['time']), marker='o', color='C2', label='4.3 MPa experimental data')
# plt.plot(data2['time'], data2['inlet-p'], marker='v', color='C3', label='5.7 MPa darcy_curve')
# plt.plot(data2['time'], monoExp2(params,data2['time']), marker='v', color='C4', label='5.7 MPa experimental data')
# plt.plot(data3['time'], data3['inlet-p'], marker='*', color='C5', label='7.0 MPa darcy_curve')
# plt.plot(data3['time'], monoExp3(params,data3['time']), marker='*', color='C6', label='7.0 MPa experimental data')
# plt.ylabel('pressure (MPa)')
# plt.xlabel('time (s)')
# plt.xlim(0,30)
# plt.title('pressure vs. time')
# plt.legend()
# plt.grid(True)
# plt.show()

