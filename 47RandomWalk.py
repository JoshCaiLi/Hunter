#Name: Joshua Li
#Email: j.caili@aol.com
#Date: 3/14/2022
#This program is km
import turtle
import random

trey = turtle.Turtle()
trey.speed(10)

for i in range(100):
  trey.forward(10)
  a = random.randrange(0,360)
  trey.right(a)