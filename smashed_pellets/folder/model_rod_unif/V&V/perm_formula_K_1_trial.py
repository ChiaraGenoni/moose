import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the function you want to fit to your data
def model_function(porosity, C1):
    return C1 * ((porosity / 100) ** 3) / (1 - porosity / 100) ** 2

# Generate example data with uncertainties in x-values and y-values
porosity_data = np.array([0, 2.2, 2.2, 2.2, 2.7])
y_data = np.array([0, 3.5e-15, 3.4e-15, 3.2e-15, 3.8e-15])
x_err = np.array([0, 0.1, 0.1, 0.1, 0.1])  # Uncertainties in x-values


# Perform the curve fit, considering data uncertainties in both x and y
params, covariance = curve_fit(model_function, porosity_data, y_data, sigma=x_err)

# Extract the best-fit parameters
best_fit_C1 = params[0]

# Calculate the standard error of the parameter from the covariance matrix
param_error = np.sqrt(covariance[0, 0])

# Plot the data points with error bars
plt.errorbar(porosity_data, y_data, xerr=x_err,  fmt='o', label='Data with Error Bars')

# Generate the best-fit curve using the fitted parameter
porosity_fit = np.linspace(min(porosity_data), max(porosity_data), 100)
y_fit = model_function(porosity_fit, best_fit_C1)

# Plot the best-fit curve
plt.plot(porosity_fit, y_fit, 'r-', label='Best Fit Curve')

# Display the result
print(f"Best Fit Parameter (C1): {best_fit_C1:.2e} ± {param_error:.2e}")

# Add labels and legend
plt.xlabel('Porosity (%)')
plt.ylabel('Y')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
