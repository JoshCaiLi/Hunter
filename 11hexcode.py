
#Name: Joshua Li
#Email: j.caili@aol.com
#Date: 3/1/2022
#This program is the color assignment
import turtle
turtle.colormode(255)
jesh=turtle.Turtle()

jesh.backward(100)
for i in range(0,255,10):
    jesh.forward(10)
    jesh.pensize(i)
    jesh.color(0,0,i)