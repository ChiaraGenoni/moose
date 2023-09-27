

import matplotlib as mpl
import numpy as np #library to import csv data
import matplotlib.pyplot as plt #library for visualization
import pylab
import pandas as pd

# data = np.genfromtxt('model_pellets.csv', delimiter=',', skip_header = 1)
data1 = pd.read_csv('test_tube_1.csv')
data2 = pd.read_csv('control_tube_1.csv')
data3 = pd.read_csv('test_tube_2.csv')




# plt.plot(data1['time'], data1['608_test_tube_1_psi'], '.', color='g', label = '600 psi')
# plt.plot(data1['time'], data1['612_test_tube_1_psi'], '.', color='r', label = '612 psi')
# plt.plot(data1['time'], data1['815_test_tube_1_psi'], '.', color='k', label = '800 psi')
# plt.plot(data1['time'], data1['812_test_tube_1_psi'], '.', color='b', label = '812 psi')
# plt.plot(data1['time'], data1['1000_test_tube_1_psi'], '.', color='y', label = '1000 psi')
# plt.plot(data1['time'], data1['990_test_tube_1_psi'], '.', color='C1', label = '990 psi')

# plt.grid(which = 'major', axis = 'both', linestyle = '--')
# plt.xlabel('time (s)')
# plt.ylabel('inlet_pressure') n
# plt.xlim([0, 40])
# plt.legend()


# plt.savefig('test_tube_1_pressure_decay')

# plt.show()


# plt.plot(data2['time'], data2['517_control_tube_1'], '.', color='C1', label = '517 psi')
# plt.plot(data2['time'], data2['531_control_tube_1'], '.', color='g', label = '531 psi')
# plt.plot(data2['time'], data2['602_control_tube_1_psi'], '.', color='r', label = '600 psi')
# plt.plot(data2['time'], data2['613_control_tube_1'], '.', color='b', label = '613 psi')
# plt.plot(data2['time'], data2['804_control_tube_1_psi'], '.', color='g', label = '800 psi')
# plt.plot(data2['time'], data2['811_control_tube_1'], '.', color='k', label = '811 psi')
# plt.plot(data2['time'], data2['996_control_tube_1'], '.', color='C1', label = '996 psi')
# plt.plot(data2['time'], data2['1004_control_tube_1_psi'], '.', color='y', label = '1000 psi')
# plt.plot(data2['time'], data2['998_control_tube_1'], '.', color='C3', label = '998 psi')


# plt.grid(which = 'major', axis = 'both', linestyle = '--')
# plt.xlabel('time (s)')
# plt.ylabel('inlet_pressure')
# plt.xlim([0, 40])
# plt.legend()


# plt.savefig('control_tube_1_pressure_decay')

# plt.show() 


plt.plot(data1['time'], data1['608_test_tube_1'], '.', color='g', label = '4.3 MPa')
plt.plot(data1['time'], data1['612_test_tube_1'], '.', color='g', label = '4.3 MPa')
plt.plot(data1['time'], data1['815_test_tube_1'], '.', color='k', label = '5.7 MPa')
plt.plot(data1['time'], data1['812_test_tube_1'], '.', color='k', label = '5.7 MPa')
plt.plot(data1['time'], data1['1000_test_tube_1'], '.', color='y', label = '7.0 MPa')
plt.plot(data1['time'], data1['990_test_tube_1'], '.', color='y', label = '7.0 MPa')



plt.grid(which = 'major', axis = 'both', linestyle = '--')
plt.xlabel('time (s)')
plt.ylabel('pressure (MPa)')
plt.xlim([0, 40])
plt.ylim([0, 7300000])

plt.legend()


plt.savefig('comparison_test_tube')

plt.show()





# comparison on pressure decay frsh vs crushed


plt.plot(data1['time'], data1['608_test_tube_1'], '.', color='g', label = 'crushed')
plt.plot(data1['time'], data1['612_test_tube_1'], '.', color='g', label = 'crushed')
plt.plot(data2['time'], data2['602_control_tube_1'], 'v', color='g', label = 'fresh')
plt.plot(data2['time'], data2['613_control_tube_1'], 'v', color='g', label = 'fresh')



plt.grid(which = 'major', axis = 'both', linestyle = '--')
plt.xlabel('time (s)')
plt.ylabel('pressure (MPa)')
plt.xlim([0, 40])
plt.ylim([0, 7300000])

plt.legend()


plt.savefig('comparison_fuel_state_600')

plt.show()

plt.plot(data1['time'], data1['815_test_tube_1'], '.', color='k', label = 'crushed')
plt.plot(data1['time'], data1['812_test_tube_1'], '.', color='k', label = 'crushed')
plt.plot(data2['time'], data2['811_control_tube_1'], 'v', color='k', label = 'fresh')
plt.plot(data2['time'], data2['804_control_tube_1'], 'v', color='k', label = 'fresh')

plt.grid(which = 'major', axis = 'both', linestyle = '--')
plt.xlabel('time (s)')
plt.ylabel('pressure (MPa)')
plt.xlim([0, 40])
plt.ylim([0, 7300000])

plt.legend()


plt.savefig('comparison_fuel_state_800')

plt.show()



plt.plot(data1['time'], data1['1000_test_tube_1'], '.', color='y', label = 'crushed')
plt.plot(data1['time'], data1['990_test_tube_1'], '.', color='y', label = 'crushed')
plt.plot(data2['time'], data2['996_control_tube_1'], 'v', color='y', label = 'fresh')
plt.plot(data2['time'], data2['1004_control_tube_1'], 'v', color='y', label = 'fresh')
plt.plot(data2['time'], data2['998_control_tube_1'], 'v', color='y', label = 'fresh')
plt.plot(data2['time'], data2['1001_control_tube_1'], 'v', color='y', label = 'fresh')
plt.plot(data2['time'], data2['1006_control_tube_1'], 'v', color='y', label = 'fresh')
plt.plot(data2['time'], data2['997_control_tube_1'], 'v', color='y', label = 'fresh')

plt.grid(which = 'major', axis = 'both', linestyle = '--')
plt.xlabel('time (s)')
plt.ylabel('pressure (MPa)')
plt.xlim([0, 40])
plt.ylim([0, 7300000])

plt.legend()


plt.savefig('comparison_fuel_state_1000')

plt.show()




# Comparison of pressure decay with different number of pellets

plt.plot(data1['time'], data1['608_test_tube_1'], '.', color='g', label = '4 pellets')
plt.plot(data1['time'], data1['612_test_tube_1'], '.', color='g', label = '4 pellets')
plt.plot(data3['time'], data3['618_test_tube_2'], 'v', color='g', label = '8 pellets')
plt.plot(data3['time'], data3['608_test_tube_2'], 'v', color='g', label = '8 pellets')

plt.grid(which = 'major', axis = 'both', linestyle = '--')
plt.xlabel('time (s)')
plt.ylabel('pressure (MPa)')
plt.xlim([0, 40])
plt.ylim([0, 7300000])

plt.legend()


plt.savefig('comparison_pellets_number_600')

plt.show()


plt.plot(data1['time'], data1['815_test_tube_1'], '.', color='k', label = '4 pellets')
plt.plot(data1['time'], data1['812_test_tube_1'], '.', color='k', label = '4 pellets')
plt.plot(data3['time'], data3['802_test_tube_2'], 'v', color='k', label = '8 pellets')
plt.plot(data3['time'], data3['816_test_tube_2'], 'v', color='k', label = '8 pellets')
plt.plot(data3['time'], data3['808_test_tube_2'], 'v', color='k', label = '8 pellets')

plt.grid(which = 'major', axis = 'both', linestyle = '--')
plt.xlabel('time (s)')
plt.ylabel('pressure (MPa)')
plt.xlim([0, 40])
plt.ylim([0, 7300000])
plt.legend()


plt.savefig('comparison_pellets_number_800')

plt.show()


plt.plot(data1['time'], data1['1000_test_tube_1'], '.', color='y', label = '4 pellets')
plt.plot(data1['time'], data1['990_test_tube_1'], '.', color='y', label = '4 pellets')
plt.plot(data3['time'], data3['1013_test_tube_2'], 'v', color='y', label = '8 pellets')
plt.plot(data3['time'], data3['1004_test_tube_2'], 'v', color='y', label = '8 pellets')

plt.grid(which = 'major', axis = 'both', linestyle = '--')
plt.xlabel('time (s)')
plt.ylabel('pressure (MPa)')
plt.xlim([0, 40])
plt.ylim([0, 7300000])
plt.legend()


plt.savefig('comparison_pellets_number_1000')

plt.show()





