# pong

import turtle as t
import os

# Starting scores
playerAscore=0
playerBscore=0
 
#create a window and declare a variable called window and call the screen()
window=t.Screen() # create screen object
window.title("The Pong Game") # Screen title
window.bgcolor("green") # Screen color
window.setup(width=800,height=600) # Screen size
window.tracer(0)
 
#Creating the left paddle
leftpaddle=t.Turtle() # Create paddle object
leftpaddle.speed(0) # Paddle speed.
leftpaddle.shape("square") # Paddle shape
leftpaddle.color("white") # Paddle color
leftpaddle.shapesize(stretch_wid=5,stretch_len=1) # Paddle size
leftpaddle.penup() # So it does not draw a line when it moves.
leftpaddle.goto(-350,0)
 
#Creating the right paddle
rightpaddle=t.Turtle() # Create paddle object
rightpaddle.speed(0) # Paddle speed
rightpaddle.shape("square") # Paddle shape
rightpaddle.color("white") # Paddle color
rightpaddle.shapesize(stretch_wid=5,stretch_len=1) # Paddle size
rightpaddle.penup()  # So it does not draw a line when it moves.
rightpaddle.goto(350,0) # Paddle position
 
#Code for creating the ball
ball=t.Turtle() # Create object
ball.speed(0) # ball speed
ball.shape("turtle") # Ball character
ball.color("red") # Ball color
ball.penup()  # So it does not draw a line when it moves.
ball.goto(5,5)
ballxdirection=0.2 # Ball x direction
ballydirection=0.2 # Ball y direction
 
#Code for creating pen for scorecard update
pen=t.Turtle()
pen.speed(0)
pen.color("Blue") # Scoreboard color
pen.penup()  # So it does not draw a line when it moves.
pen.hideturtle()
pen.goto(0,260)
pen.write("score",align="center",font=('Arial',24,'normal'))
 
#code for moving the leftpaddle
def leftpaddleup():
    y=leftpaddle.ycor()
    y=y+90
    leftpaddle.sety(y)
 
def leftpaddledown():
    y=leftpaddle.ycor()
    y=y-90
    leftpaddle.sety(y)
 
#code for moving the rightpaddle
def rightpaddleup(): # move right paddle up
    y=rightpaddle.ycor()
    y=y+90
    rightpaddle.sety(y)
 
def rightpaddledown(): # Move right paddle down
    y=rightpaddle.ycor()
    y=y-90
    rightpaddle.sety(y)
 
#Assign keys to play
window.listen()
window.onkeypress(leftpaddleup,'w') # Left player up
window.onkeypress(leftpaddledown,'s') # Left player down
window.onkeypress(rightpaddleup,'Up') # Right player up
window.onkeypress(rightpaddledown,'Down') # Right player down
 
while True:
    window.update()
 
    #moving the ball
    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballydirection)
 
    #border set up
    if ball.ycor()>290:
        ball.sety(290)
        ballydirection=ballydirection*-1
        ball.sety(ball.ycor()+ballxdirection) #bounce off the wall?

    if ball.ycor()<-290:
        ball.sety(-290)
        ballydirection=ballydirection*-1
        ball.sety(ball.ycor()+ballxdirection) #bounce off the wall?

    if ball.xcor() > 390:
        ball.goto(0,0)
        ballxdirection = ballxdirection*-1
        playerAscore = playerAscore + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(playerAscore,playerBscore),align="center",font=('Monaco',24,"normal"))
 
 
    if(ball.xcor()) < -390: # Left width paddle Border
        ball.goto(0,0)
        ballxdirection = ballxdirection * -1
        playerBscore = playerBscore + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(playerAscore,playerBscore),align="center",font=('Monaco',24,"normal"))
 
     # Handling the collisions with paddles.
 
    if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() - 40):
        ball.setx(340)
        ballxdirection = ballxdirection * -1
 
    if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40):
        ball.setx(-340)
        ballxdirection = ballxdirection * -1