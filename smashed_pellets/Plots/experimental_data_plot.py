
import pandas as pd
import matplotlib.pyplot as plt

var = pd.read_excel("test_tube_1.xlsx")
print(var)
x = list(var['time'])
y = list(var['pressure'])

plt.figure(figsize=(10,10))
plt.style.use('seaborn')
plt.scatter(x,y,marker="*",s=100,edgecolors="black",c="yellow")
plt.title("Pressure Decay")
plt.xlabel('Time (s)')
plt.ylabel('Pressure (Pa)')
plt.show()