# a121_catch_a_turtle.py
#-----import statements-----
import turtle as turtle
import random

#-----game configuration----
color = "white"
shape = "triangle"
speed = int(0)
size = int(1)
score = 0
#-----initialize turtle-----
dead = turtle.Turtle(shape = shape)
dead.turtlesize(size)
dead.speed(speed)
dead.pencolor("red")

scoreman = turtle.Turtle()
scoreman.ht()
scoreman.pu()
scoreman.goto(-370, 270)
scoreman.write(score)
scoreman.pencolor("white")


#-----game functions--------
def dead_clicked(x,y):
    global score
    score += 1
    score_change(score)
    #print(score)
    dead.dot(25)
    change_loc()
def change_loc():
    dead.ht()
    dead.pu()
    randx = random.randint(-400, 400)
    randy = random.randint(-300, 300)
    dead.goto(randx, randy)
    dead.pd()
    dead.st()
def score_change(score):
    scoreman.dot(15)
    print(score)
    scoreman.write(score)
#-----events----------------

dead.onclick(dead_clicked)
wn = turtle.Screen()
wn.mainloop()