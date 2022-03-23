#Name: Joshua Li
#Email: j.caili@aol.com
#Date: 3/23/2022
#This program is 

import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv('nycHistPop.csv',skiprows=5)
pop['Fraction'] = pop[input("Enter borough")].max()



