import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math

# Define the formula you want to fit
def K1(porosity, C1):
    return C1* ((porosity/100)**3) / (1 - porosity/100)**2


# def K2(porosity, C2):
#     return C2 * ((porosity/100)**3) / (1 - porosity/100)


# # Compute Poriosity
# fuel_OD_TT1 = 0.00794 + 75e-6
# print("fuel_OD1 = " + str(fuel_OD_TT1))
# fuel_OD_CT4 = 0.00798 + 75e-6
# print("fuel_OD2 = " + str(fuel_OD_CT4)) 

# pellets_porosity_TT1 = 0.014
# smeared_porosity_TT1 = (0.00824**2-fuel_OD_TT1**2)/0.00824**2 + pellets_porosity_TT1
# print("porosity_1 = " + str(smeared_porosity_TT1))
# pellets_porosity_CT4 = 0.017
# smeared_porosity_CT4= (0.00824**2-fuel_OD_CT4**2)/0.00824**2 + pellets_porosity_CT4
# print("porosity_2 = " + str(smeared_porosity_CT4))




porosity_data_600 = np.array([0, 1.3, 1.3, 1.8 , 3.6, 3.6, 3.6])
porosity_data_800 = np.array([0, 1.3, 1.8, 1.8, 3.6, 3.6, 3.6])
porosity_data_1000 = np.array([0, 1.3, 1.8, 1.8, 3.6, 3.6, 3.6])

# Compute Error
porosity_error_600 = np.array([0, 0.75, 1.0, 0, 0, 0])
porosity_error_800 = np.array([0, 0.75, 1.0, 1.0, 0 ,0, 0])
porosity_error_1000 = np.array([0, 0.75, 1.0, 1.0, 0, 0, 0])

# Minimum Error
minimum_porosity_error_600 = porosity_data_600 - porosity_error_600
minimum_porosity_error_800 = porosity_data_800 - porosity_error_800
minimum_porosity_error_1000 = porosity_data_1000 - porosity_error_1000

# Maximum Error
maximum_porosity_error_600 = porosity_data_600 + porosity_error_600
maximum_porosity_error_800 = porosity_data_800 + porosity_error_800 
maximum_porosity_error_1000 = porosity_data_1000 + porosity_error_1000




# Make an Array of Empirical Data CT4, CT6, CT5, CT1, TT1_1, TT1_2
empirical_data_600_K= np.array([0, 2.8e-15, 3.8e-15 , 3.6e-14 , 4.3e-14, 3.25e-14])
empirical_data_800_K= np.array([0, 1.8e-15, 3.4e-15, 5.6e-16 , 2.4e-14 , 2.1e-14, 1.14e-14])
empirical_data_1000_K= np.array([0, 1.7e-15, 3.3e-15, 5.4e-16 , 1.7e-14 , 1.4e-14, 1.0e-14])


# Perform the curve fit to find the best fit parameter
fit_param, _ = curve_fit(K1, porosity_data_600, empirical_data_600_K)

# Get the best fit parameter
C_fit_600 = fit_param[0]
print(C_fit_600)

# Generate points for the best fit curve
porosity_fit = np.linspace(min(porosity_data_600), max(porosity_data_600), 100)
empirical_parameter_fit_600 = K1(porosity_fit, C_fit_600)


squaredDiffs = np.square(empirical_data_600_K - K1(porosity_data_600, C_fit_600))
squaredDiffsFromMean = np.square(empirical_data_600_K - np.mean(empirical_data_600_K))
rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)

print("R\u00B2 = " + str(rSquared))




# Perform the curve fit to find the best fit parameter
fit_param, _ = curve_fit(K1, porosity_data_800, empirical_data_800_K)

# Get the best fit parameter
C_fit_800 = fit_param[0]
print(C_fit_800)

# Generate points for the best fit curve
porosity_fit = np.linspace(min(porosity_data_800), max(porosity_data_800), 100)
empirical_parameter_fit_800 = K1(porosity_fit, C_fit_800)


squaredDiffs = np.square(empirical_data_800_K - K1(porosity_data_800, C_fit_800))
squaredDiffsFromMean = np.square(empirical_data_800_K - np.mean(empirical_data_800_K))
rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)

print("R\u00B2 = " + str(rSquared))



# Perform the curve fit to find the best fit parameter
fit_param, _ = curve_fit(K1, porosity_data_1000, empirical_data_1000_K)

# Get the best fit parameter
C_fit_1000 = fit_param[0]
print(C_fit_1000)

# Generate points for the best fit curve
porosity_fit = np.linspace(min(porosity_data_1000), max(porosity_data_1000), 100)
empirical_parameter_fit_1000 = K1(porosity_fit, C_fit_1000)

squaredDiffs = np.square(empirical_data_1000_K - K1(porosity_data_1000, C_fit_1000))
squaredDiffsFromMean = np.square( empirical_data_1000_K - np.mean(empirical_data_1000_K))
rSquared = 1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean)

print("R\u00B2 = " + str(rSquared))

# Plot the experimental data and the best fit curve
light_blue = '#9AC0CD'  # Hexadecimal color code for light blue
plt.errorbar(porosity_data_600, empirical_data_600_K, xerr=porosity_error_600, yerr=None, color = light_blue,  capsize = 2, linestyle='')
plt.errorbar(porosity_data_800, empirical_data_800_K, xerr=porosity_error_800, yerr=None, color = light_blue, capsize = 2, linestyle='')
plt.errorbar(porosity_data_1000, empirical_data_1000_K, xerr=porosity_error_1000, yerr=None, color = light_blue, capsize = 2, linestyle='')
plt.plot(porosity_data_1000, empirical_data_1000_K, 'go', label='7.0 MPa')
plt.plot(porosity_fit, empirical_parameter_fit_1000, 'g-')
plt.plot(porosity_data_800, empirical_data_800_K, 'rv', label='5.6 MPa')
plt.plot(porosity_fit, empirical_parameter_fit_800, 'r-')
plt.plot(porosity_data_600, empirical_data_600_K, 'bs', label='4.3 MPa')
plt.plot(porosity_fit, empirical_parameter_fit_600, 'b-')
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



