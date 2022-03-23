#Name: Joshua Li
#Email: j.caili@aol.com
#Date: 3/2/2022
#This program is easy assignment
from ensurepip import version
import matplotlib.pyplot as plt
import numpy as np


img = plt.imread('csBridge.png')   #Read in image from csBridge.png
plt.imshow(img)		                 #Load image into pyplot
plt.show()                         #Show the image (waits until closed to continue)

img2 = img.copy()        #make a copy of our image
img2[:,:,0] = 0         #Set the red channel to 0
img2[:,:,1] = 0          #Set the gdreen channel to 0         #Set the blue channel to 0

img3 = img.copy()        #make a copy of our image
img3[:,:,0] = 0         #Set the red channel to 0
img3[:,:,1] = 0          #Set the green channel to 0         #Set the blue channel to 0


plt.imshow(img2)         #Load our new image into pyplot
plt.show()      
plt.imshow(img3)
plt.show()               #Show the image (waits until closed to continue)
