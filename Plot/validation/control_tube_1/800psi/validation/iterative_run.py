
import os

range = [0, 1, 2, 3, 4, 5, 6]
for i in range:
    print(i)
    constant = ((1+0.1*i)*10**-15)
    command_line = 'mpiexec -n 8 ~/projects/moose/modules/combined/combined-opt -i model_pellets.i --allow-unused constant=' + str(constant) + " Outputs/file_base=output_" + str(i) 
    os.system(command_line)

data1 = pd.read_csv('model_pellets_out.csv')
data2 = pd.read_csv('experimental_data.csv')
square_error = (np.square((data1['pellet-inlet-p']-data2['inlet-p'])))
mean_square_error = np.mean(square_error)
RMSE = math.sqrt(mean_square_error)
mean_square_value = np.mean(np.square(data1['inlet-p']))

RRMSE = math.sqrt(mean_square_error/mean_square_value)*100




