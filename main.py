import turtle
import math
import random

w = turtle.Screen()
w.bgcolor("DarkGray")
w.setup(1000, 1000)

player = turtle.Turtle()
player.color("black")
player.shape("triangle")
player.turtlesize(0.5,0.5,0.5)
player.penup()
player.speed(0)

goal = turtle.Turtle()
goal.color("yellow")
goal.shape("circle")
goal.penup()
goal.speed(0)
goal.setposition(-180, -80)

speed = 1
score = 0
highestscore = 0

mypen = turtle.Turtle()
mypen.speed(100)
mypen.hideturtle()
mypen.penup()
mypen.setposition(-300, -300)
mypen.color("red")
mypen.down()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)

def Turnleft():
    player.left(30)
def Turnright():
    player.right(30)
def SpeedInc():
    global speed
    speed += 1
def SpeedDec():
    global speed
    speed -= 1

text = turtle.Turtle()
text.hideturtle()
text.speed(100)
text.penup()
text.setposition(0, 450)
text.write("Score:"+str(score), font=("Arial", 20, "normal"))

highest = turtle.Turtle()
highest.hideturtle()
highest.speed(100)
highest.penup()
highest.setposition(50, 430)
highest.write("Highest Score:"+str(score), font=("Arial", 15, "normal"), align="center")

turtle.listen()
turtle.onkey(Turnleft, "a")
turtle.onkey(Turnright, "d")

while True:
    player.forward(speed)

    if player.xcor() > 300 or player.xcor() < -300:
        player.setposition(0, 0)
        score = 0
        text.clear()
        text.write("Score: " + str(score), font=("Arial", 20, "normal"))
        speed = 1

    if player.ycor() > 300 or player.ycor() < -300:
        player.setposition(0, 0)
        score = 0
        text.clear()
        text.write("Score: " + str(score), font=("Arial", 20, "normal"))
        speed = 1

    d = math.sqrt(math.pow(player.xcor()-goal.xcor(),2) + math.pow(player.ycor()-goal.ycor(),2))
    if d < 15:
        goal.setposition(random.randint(-250, 250), random.randint(-250, 250))
        score += 1
        text.clear()
        text.write("Score: " + str(score), font=("Arial", 20, "normal"))
        speed += 0.5
    
    if highestscore < score:
        highestscore += 1
        highest.clear()
        highest.write("Highest Score:"+str(highestscore), font=("Arial", 15, "normal"), align="center")