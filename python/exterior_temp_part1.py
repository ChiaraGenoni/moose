import csv
import numpy as np
import pandas as pd

# number of directories
noDirectories= 201
# I assume headers do not vary for csv files in each directories
noColumn= 4 # you can define this
df = pd.DataFrame()
# finalFile= open('interior_temp.csv', "w")

for idir in range(noDirectories):
    output= pd.read_csv('outputs/exterior_part1_out_exterior_temp_'+str(format(idir,'04'))+'.csv')
    df[idir]= output.temperature

df.to_csv('exterior_temp_part1.csv')
# Close the .csv file
