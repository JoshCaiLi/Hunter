#Name:  Your name
#Date:  March 2022
#Account name for my github account
#Modify the program from Lab 7 that displays shelter population over time to:




#Name: Joshua Li
#Email: j.caili@aol.com
#Date: 3/23/2022
#This program is

import pandas as pd
import matplotlib.pyplot as plt

pop= pd.read_csv(input('Enter an input:'))
pop['Fraction Children'] = pop['Total Children in Shelter']/pop['Total Individuals in Shelter']
pop.plot(x = "Date of Census", y = "Fraction Children")

fig = plt.gcf()
fig.savefig(input('enter an output'))