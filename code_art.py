
import turtle
import random
# Speed
t = turtle.Turtle()
t.speed(10)

# Random triangles
colors = ["red", "black", "blue", "green", "yellow", "purple"]  
angles = [0, 60, 120, 180, 240, 300] 
# Movement
for i in range(999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
    t.color(colors[i % 6]) 
    t.forward(10) 
    t.left(random.choice(angles)) 

turtle.exitonclick() 