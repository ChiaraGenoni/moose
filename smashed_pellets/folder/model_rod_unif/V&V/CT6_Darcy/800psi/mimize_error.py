import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
from scipy.optimize import minimize_scalar

# Create an empty dictionary to store the DataFrame
data_frames = {}
RMSE = np.array([])
data20 = pd.read_csv('experimental_data.csv')  
porosity = 0.018 

# Loop through numbers
for i in range(0, 11):
    filename = f'stochastic_tools_out_runner{i:02d}.csv'
    data_frames[f'data{i}'] = pd.read_csv(filename)
 
# Function to compute Absolute Root Mean Square Error (RMSE)
def compute_RMSE(y_values, experimental_y_values):
    absolute_error = np.abs(y_values - experimental_y_values)
    squared_error = absolute_error**2
    mean_squared_error = np.mean(squared_error)
    RMSE = np.sqrt(mean_squared_error)
    return RMSE

color_palette = plt.cm.get_cmap('tab20', len(data_frames))

# Plot the data for each DataFrame with different line colors
for idx, (key, df) in enumerate(data_frames.items()):
    plt.plot(df['time'], df['inlet-p'], color=color_palette(idx), label=f'Data for {key}', linestyle='-')
    # Compute the error between the plot and experimental data
    x_values = df['time']
    y_values = df['inlet-p']
    experimental_y_values = np.interp(x_values, data20['Time8'], data20['P_8'])
    range_of_observed_values = np.max(experimental_y_values) - np.min(experimental_y_values)
    rmse = compute_RMSE(y_values, experimental_y_values)/1e6
    # Append the value to the NumPy array
    RMSE = np.append(RMSE, rmse) 



particle_diameter_1 = pd.read_csv('parameters.csv')*1e6

degree =5 # Degree of the polynomial
coefficients = np.polyfit(particle_diameter_1['particle_diameter_1'], RMSE, degree)
poly_function = np.poly1d(coefficients)
y_fit = poly_function(particle_diameter_1['particle_diameter_1'])


# Define the polynomial function
def polynomial(x):
    return np.polyval(coefficients, x)

# Find the minimum using scipy's minimize_scalar
result = minimize_scalar(polynomial)

# Print the result
print("Minimum value:", result.fun)
print("Optimal solution:", result.x)

permeability = (result.x*1e-6)**2*(porosity**3/(1-porosity)**2)/150
print(permeability)