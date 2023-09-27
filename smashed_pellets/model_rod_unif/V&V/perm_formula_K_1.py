import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math

# Define the formula you want to fit
def K1(porosity, C1):
    return C1* ((porosity/100)**3) / (1 - porosity/100)**2


k1_error_600 = np.array([0, 3.4e-17, 3.4e-17, 3.4e-17, 0])
k1_error_800 = np.array([0, 3.4e-17, 3.4e-17, 3.4e-17, 0, 0])
k1_error_1000 = np.array([0, 3.4e-17, 3.4e-17, 0, 0, 0])




# Porosity of CT4, CT5, CT6 CT1, TT1
porosity_data_600 = np.array([0, 2.6, 2.6, 2.6, 1.8, 3.6, 3.6, 3.6, 3.6])
porosity_data_800 = np.array([0, 2.6, 2.6, 2.6, 1.8, 1.8, 3.6, 3.6, 3.6, 3.6])
porosity_data_1000 = np.array([0, 2.6, 2.6, 2.6, 1.8, 1.8, 3.6, 3.6, 3.6, 3.6])

# Make an Array of Empirical Data CT4, CT5, CT1, TT1
empirical_data_600_K= np.array([0, 3.2e-15, 3.2e-15, 3.2e-15, 3.8e-15, 1.82e-14, 1.25e-14, 1.58e-14, 1.45e-14])
empirical_data_800_K= np.array([0, 2e-15, 2e-15, 2e-15, 5.6e-16, 3.4e-15, 1.14e-14, 2.04e-14, 1.76e-14, 1.29e-14])
empirical_data_1000_K= np.array([0, 2e-15, 2e-15, 3.6e-16, 0.8e-15, 3.2e-15, 2.0e-14, 1.42e-14, 1.5e-14, 1.62e-14])

# Compute Error
porosity_error_600 = np.array([0, 0.75, 0.75, 0.75, 1.0, 0, 0, 0, 0])
porosity_error_800 = np.array([0, 0.75, 0.75, 0.75, 1.0, 1.0, 0, 0, 0, 0])
porosity_error_1000 = np.array([0, 0.75, 0.75, 0, 0, 0, 0, 0, 0, 0])

k1_error_600 = np.array([0, 3.4e-17, 3.4e-17, 3.4e-17, 3.4e-17, 3.4e-17, 3.4e-17, 3.4e-17, 3.4e-17])
k1_error_800 = np.array([3.4e-17, 3.4e-17 , 3.4e-17, 3.4e-17, 3.4e-17, 3.4e-17, 3.4e-17, 3.4e-17, 3.4e-17, 3.4e-17])
k1_error_1000 = np.array([0, 3.4e-17, 3.4e-17, 3.4e-17, 3.4e-17, 3.4e-17, 3.4e-17, 3.4e-17, 3.4e-17, 3.4e-17])


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
plt.errorbar(porosity_data_600, empirical_data_600_K, xerr=porosity_error_600, yerr=k1_error_600, color = light_blue,  capsize = 2, linestyle='')
plt.errorbar(porosity_data_800, empirical_data_800_K, xerr=porosity_error_800, yerr=k1_error_800, color = light_blue, capsize = 2, linestyle='')
plt.errorbar(porosity_data_1000, empirical_data_1000_K, xerr=porosity_error_1000, yerr=k1_error_1000, color = light_blue, capsize = 2, linestyle='')
plt.plot(porosity_data_1000, empirical_data_1000_K, 'go', label='7.0 MPa')
plt.plot(porosity_fit, empirical_parameter_fit_1000, 'g-')
plt.plot(porosity_data_800, empirical_data_800_K, 'rv', label='5.6 MPa')
plt.plot(porosity_fit, empirical_parameter_fit_800, 'r-')
plt.plot(porosity_data_600, empirical_data_600_K, 'bs', label='4.3 MPa')
plt.plot(porosity_fit, empirical_parameter_fit_600, 'b-')
plt.xlabel('Porosity (%)', fontsize = 12)
plt.ylabel('K (m \u00B2)', fontsize = 12)
plt.tick_params(axis='both', which='major', labelsize=12)
# plt.fill_between(empirical_data_600_K, minimum_porosity_error_600, maximum_porosity_error_600, color ='blue', alpha = 0.2)
# plt.fill_between(empirical_data_800_K, minimum_porosity_error_800, maximum_porosity_error_800, color ='red')
# plt.fill_between(empirical_data_1000_K, minimum_porosity_error_1000, maximum_porosity_error_1000, color ='green')

plt.legend(fontsize = 12)
# plt.yscale('log')
# plt.xscale('log')
plt.grid(True)
plt.show()



