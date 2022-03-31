#Name: Joshua Li
#Email: j.caili@aol.com
#Date: 3/2/2022
#This program is easy assignment
import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('csBridge.png')    #Read in image from csBridge.png
img2 = img.copy()        #make a copy of our image
img2[:,:,0] = 0         #Set the red channel to 0
img2[:,:,1] = 0          #Set the green channel to 0         #Set the blue channel to 0

imgin = plt.imread('acTree.png')
img3 = imgin.copy()        #make a copy of our image
img3[:,:,0] = 0         #Set the red channel to 0
img3[:,:,1] = 0          #Set the green channel to 0         #Set the blue channel to 0


plt.imsave('out1.png', img2)  #Save the image we created to the file: reds.png

plt.imsave('out2.png', img3)
