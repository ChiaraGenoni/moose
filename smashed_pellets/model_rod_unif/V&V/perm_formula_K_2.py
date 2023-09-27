import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math



def K2(porosity, C2):
    return C2 * ((porosity/100)**3) / (1 - porosity/100)


# Porosity of CT4, CT1, TT1
porosity_data_600 = np.array([2.2, 2.2, 5.4, 5.4, 5.4, 5.4])
porosity_data_800 = np.array([2.2, 2.2, 2.2, 5.4, 5.4, 5.4, 5.4]) 
porosity_data_1000 = np.array([2.2, 2.2, 5.4, 5.4, 5.4, 5.4])

# Compute Error
porosity_error_600 = np.array([0.75, 0.75, 0, 0, 0, 0])
porosity_error_800 = np.array([0.75, 0.75, 0.75, 0, 0, 0, 0])
porosity_error_1000 = np.array([0.75, 0.75, 0, 0, 0, 0])

k2_error_600 = np.array([2.68e-11, 2.68e-11, 2.2e-11, 2.2e-11, 2.2e-11, 2.2e-11])
k2_error_800 = np.array([2.68e-11, 2.68e-11, 2.68e-11, 2.2e-11, 2.2e-11, 2.2e-11, 2.2e-11])
k2_error_1000 = np.array([2.68e-11, 2.68e-11, 2.2e-11, 2.2e-11, 2.2e-11, 2.2e-11])

# Minimum Error
minimum_porosity_error_600 = porosity_data_600 - porosity_error_600
minimum_porosity_error_800 = porosity_data_800 - porosity_error_800
minimum_porosity_error_1000 = porosity_data_1000 - porosity_error_1000

# Maximum Error
maximum_porosity_error_600 = porosity_data_600 + porosity_error_600
maximum_porosity_error_800 = porosity_data_800 + porosity_error_800
maximum_porosity_error_1000 = porosity_data_1000 + porosity_error_1000


# Make an Array of Empirical Data CT4, CT1, TT1
empirical_data_600_K= np.array([1.2e-10 , 1.2e-10, 2.9e-10, 2.9e-10, 2.8e-10, 2e-10])
empirical_data_800_K= np.array([1.2e-10, 1.2e-10, 1.2e-10, 2.4e-10, 2.4e-10, 2.4e-10, 2e-10])
empirical_data_1000_K= np.array([1.45e-10, 1.45e-10, 2.4e-10, 2.7e-10, 2.4e-10, 2.2e-10])


# Perform the curve fit to find the best fit parameter
fit_param, _ = curve_fit(K2, porosity_data_600, empirical_data_600_K)
 
# Get the best fit parameter
C_fit_600 = fit_param[0]
print(C_fit_600)

# Generate points for the best fit curve
porosity_fit = np.linspace(min(porosity_data_600), max(porosity_data_600), 100)
empirical_parameter_fit_600 = K2(porosity_fit, C_fit_600)


squaredDiffs = np.square(empirical_data_600_K - K2(porosity_data_600, C_fit_600))
squaredDiffsFromMean = np.square(empirical_data_600_K - np.mean(empirical_data_600_K))
rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)

print("R\u00B2 = " + str(rSquared))




# Perform the curve fit to find the best fit parameter
fit_param, _ = curve_fit(K2, porosity_data_800, empirical_data_800_K)

# Get the best fit parameter
C_fit_800 = fit_param[0]
print(C_fit_800)

# Generate points for the best fit curve
porosity_fit = np.linspace(min(porosity_data_800), max(porosity_data_800), 100)
empirical_parameter_fit_800 = K2(porosity_fit, C_fit_800)


squaredDiffs = np.square(empirical_data_800_K - K2(porosity_data_800, C_fit_800))
squaredDiffsFromMean = np.square(empirical_data_800_K - np.mean(empirical_data_800_K))
rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)

print("R\u00B2 = " + str(rSquared))



# Perform the curve fit to find the best fit parameter
fit_param, _ = curve_fit(K2, porosity_data_1000, empirical_data_1000_K)

# Get the best fit parameter
C_fit_1000 = fit_param[0]
print(C_fit_1000)

# Generate points for the best fit curve
porosity_fit = np.linspace(min(porosity_data_1000), max(porosity_data_1000), 100)
empirical_parameter_fit_1000 = K2(porosity_fit, C_fit_1000)

squaredDiffs = np.square(empirical_data_1000_K - K2(porosity_data_1000, C_fit_1000))
squaredDiffsFromMean = np.square( empirical_data_1000_K - np.mean(empirical_data_1000_K))
rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)

print("R\u00B2 = " + str(rSquared))

# Plot the experimental data and the best fit curve
light_blue = '#9AC0CD'  # Hexadecimal color code for light blue
plt.errorbar(porosity_data_600, empirical_data_600_K, xerr=porosity_error_600, yerr=k2_error_600, color = light_blue,  capsize = 2, linestyle='')
plt.errorbar(porosity_data_800, empirical_data_800_K, xerr=porosity_error_800, yerr=k2_error_800, color = light_blue, capsize = 2, linestyle='')
plt.errorbar(porosity_data_1000, empirical_data_1000_K, xerr=porosity_error_1000, yerr=k2_error_1000, color = light_blue, capsize = 2, linestyle='')
plt.plot(porosity_data_1000, empirical_data_1000_K, 'go', label='7.0 MPa')
# plt.plot(porosity_fit, empirical_parameter_fit_1000, 'g-')
plt.plot(porosity_data_800, empirical_data_800_K, 'rv', label='5.6 MPa')
# plt.plot(porosity_fit, empirical_parameter_fit_800, 'r-')
plt.plot(porosity_data_600, empirical_data_600_K, 'bs', label='4.3 MPa')
# plt.plot(porosity_fit, empirical_parameter_fit_600, 'b-')
plt.xlabel('Porosity (%)', fontsize = 12)
plt.ylabel('Permeability (m \u00B2)', fontsize = 12)
plt.tick_params(axis='both', which='major', labelsize=12)
# plt.fill_between(empirical_data_600_K, minimum_porosity_error_600, maximum_porosity_error_600, color ='blue', alpha = 0.2)
# plt.fill_between(empirical_data_800_K, minimum_porosity_error_800, maximum_porosity_error_800, color ='red')
# plt.fill_between(empirical_data_1000_K, minimum_porosity_error_1000, maximum_porosity_error_1000, color ='green')


plt.legend(fontsize = 12)
# plt.yscale('log')
# plt.xscale('log')
plt.grid(True)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Given empirical data
empirical_data_600_K = np.array([2.9e-10, 2.9e-10, 2.8e-10, 2e-10])
empirical_data_800_K = np.array([2.4e-10, 2.4e-10, 2.4e-10, 2e-10])
empirical_data_1000_K = np.array([2.4e-10, 2.7e-10, 2.4e-10, 2.2e-10])

# Corresponding pressures
pressures_600 = [4.3, 4.3, 4.3, 4.3]
pressures_800 = [5.6, 5.6, 5.6, 5.6] 
pressures_1000 = [7.0, 7.0, 7.0, 7.0] 


# Plotting
plt.figure(figsize=(8, 6))
plt.plot(pressures_600, empirical_data_600_K, marker='o', linestyle = '')
plt.plot(pressures_800, empirical_data_800_K, marker='s', linestyle = '')
plt.plot(pressures_1000, empirical_data_1000_K, marker='^', linestyle = '')

plt.xlabel('Pressure (MPa)', fontsize = 12)
plt.ylabel('K₂ (kg/m)', fontsize = 12)
plt.legend()
plt.grid()

plt.show()







