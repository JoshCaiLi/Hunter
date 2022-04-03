#Name:  Your name
#Date:  March 2022
#Account name for my github account
#Modify the program from Lab 7 that displays shelter population over time to:
import pandas as pd

csvFile = input('Enter CSV file name: ')         #Name of the CSV file
tickets = pd.read_csv(csvFile)  
attribute = input('enter a attribute: ')
print("The 10 worst offenders are:")
print(tickets[attribute].value_counts()[:10]) #Print out the dataframe

