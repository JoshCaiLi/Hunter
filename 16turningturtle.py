#Name: Joshua Li
#Email: j.caili@aol.com
#Date: 3/4/2022
#This program is easy assignment
import turtle
wn = turtle.Screen()
jesh = turtle.Turtle()
for i in range(5):
    inp = int(input("Enter a number:"))
    jesh.left(inp)
    jesh.forward(100)

wn.exitonclick()