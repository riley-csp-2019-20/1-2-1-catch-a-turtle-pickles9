# a121_catch_a_turtle.py
#-----import statements-----
import turtle as turtle

#-----game configuration----
color = "white"
shape = "triangle"
speed = int(3)
size = int(1)
#-----initialize turtle-----
dead = turtle.Turtle(shape = shape)
dead.turtlesize(size)

#-----game functions--------
while True:
    dead.right(500000000)

#-----events----------------
wn = turtle.Screen()
wn.mainloop()