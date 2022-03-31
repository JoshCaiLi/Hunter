#Name:  Your name
#Date:  March 2022
#Account name for my github account
#Modify the program from Lab 7 that displays shelter population over time to:

import matplotlib.pyplot as plt
import numpy as np 
inF = input("Enter file name: ")
img = plt.imread(inF) #Read in image from inF
height = img.shape[0] #Get height
width = img.shape[1] #Get width

img2 = img[height//2:, :width//2] #Crop to lower left corner
plt.imsave(input("Enter output: "), img2)