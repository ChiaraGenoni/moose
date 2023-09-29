import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

path = 'stochastic_tools_out.json'
data20 = pd.read_csv('CT1.csv')

# to open the JSON file in read mode, assign it to the variable file and convert into a pyhton data structure (dictionary)
with open(path, 'r') as file: 
  data_json = json.load(file)


# to extract the samples dictionary from data_json and convert it into a DataFrame
data_label = data_json['time_steps'][-1]['samples'] 
parameters_study = pd.DataFrame(data_label)
parameters_study.columns = ['particle_diameter_1']


raw_data = data_json['time_steps'][-1]['results']
df = pd.DataFrame(raw_data) 
df.columns = ['inlet-p', 'outlet-p','time','converged']
df

p_in = df['inlet-p'][:].tolist() 
t = df['time'][:].tolist() 

# # The first element of the list t is selected and ordered vertically
# t_header = np.stack(t[0],axis=0)
# A DataFrame is created, composed by all the inlet pressure values at each time-step 
md_df = pd.DataFrame(data = p_in)
md_df = md_df.T
print('Modeling Results')
md_df *= 1e-6
md_df


# Function to compute Absolute Root Mean Square Error (ARMSE)  
def compute_armse(y_values, experimental_y_values):
    absolute_error = np.abs(y_values - experimental_y_values)
    squared_error = absolute_error**2
    mean_squared_error = np.mean(squared_error)
    armse = np.sqrt(mean_squared_error)
    return armse




RMSE = []

for i in range(md_df.shape[1]):
    pressure = md_df.iloc[:, i]  # Select column using numerical index
    y_values = pressure.values
    x_values = np.linspace(0, 50, 501)
    experimental_y_values = np.interp(x_values, data20['time'], data20['CT1_600_1']/1e6)
    range_of_observed_values = np.max(experimental_y_values) - np.min(experimental_y_values)
    rmse = compute_armse(y_values, experimental_y_values)
    # Append the value to the NumPy array
    RMSE = np.append(RMSE, rmse) 

print(RMSE)



particle_diameter_1 = pd.read_csv('combinations.csv')*1e6

degree = 10 # Degree of the polynomial
coefficients = np.polyfit(particle_diameter_1['particle_diameter_1'], RMSE, degree)
poly_function = np.poly1d(coefficients)
y_fit = poly_function(particle_diameter_1['particle_diameter_1'])

plt.plot(particle_diameter_1['particle_diameter_1'], RMSE, color='C1', label = 'RMSE')
plt.plot(particle_diameter_1['particle_diameter_1'], y_fit, color='C2', label = 'Best Fit')
plt.xlabel('particle diameter (m)', fontsize = 12)
plt.ylabel('NRMSE', fontsize = 12)
plt.tick_params(axis='both', which='major', labelsize=12) 
plt.legend(fontsize = 12)
plt.grid()

import numpy as np
from scipy.optimize import minimize_scalar

# Define the polynomial function
def polynomial(x):
    return np.polyval(coefficients, x)

# Find the minimum using scipy's minimize_scalar
result = minimize_scalar(polynomial)



# Print the result
print("Minimum RMSE:", result.fun)
print("Optimal particle diameter:", result.x)
porosity = 0.036
optimal_permeability = (result.x*1e-6)**2*(porosity**3/(1-porosity)**2)/150
print("Optimal permeability:", optimal_permeability)