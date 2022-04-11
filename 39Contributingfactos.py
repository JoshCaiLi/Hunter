#Name: Joshua Li
#Email: j.caili@aol.com
#Date: 3/14/2022
#This program is km



import pandas as pd
file = input ('Enter .csv file:')
pop = pd.read_csv(file)
print(pop["CONTRIBUTING FACTOR VEHICLE 1"].value_counts()[:3])