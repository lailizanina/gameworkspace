#This is a programm to a game like spaceship arcade
import turtle
import os

#Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Warriors")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

player.speed = 15

#Move the player left and right
def move_left():
   x = player.xcor()
   x -= player.speed
   if x < -280:
       x = -280
   player.setx(x)

def move_right():
    x = player.xcor()
    x += player.speed
    if x > 280:
        x = 280
    player.setx(x)

#Create keyboar buildings
turtle.listen()
turtle.onkey( move_left , "Left" )
turtle.onkey( move_right , "Right" )



turtle.done()

delay = input("Press enter to finish")