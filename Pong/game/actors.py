import turtle as t
import os

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