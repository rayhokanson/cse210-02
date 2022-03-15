from game.actors import Actor
from game.constants import Constant

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        parachute (Parachute): display the parachute
        word (Word): pick a random word
        is_playing (boolean): Whether or not the game is being played.
        terminal_service (TermianalService): get all the prompts
    """
    #code for moving the leftpaddle
    def leftpaddleup():
        y=Actor.leftpaddle.ycor()
        y=y+90
        Actor.leftpaddle.sety(y)
    
    def leftpaddledown():
        y=Actor.leftpaddle.ycor()
        y=y-90
        Actor.leftpaddle.sety(y)
    
    #code for moving the rightpaddle
    def rightpaddleup(): # move right paddle up
        y=Actor.rightpaddle.ycor()
        y=y+90
        Actor.rightpaddle.sety(y)
    
    def rightpaddledown(): # Move right paddle down
        y=Actor.rightpaddle.ycor()
        y=y-90
        Actor.rightpaddle.sety(y)

    #Assign keys to play
    Actor.window.listen()
    Actor.window.onkeypress(leftpaddleup,'w') # Left player up
    Actor.window.onkeypress(leftpaddledown,'s') # Left player down
    Actor.window.onkeypress(rightpaddleup,'Up') # Right player up
    Actor.window.onkeypress(rightpaddledown,'Down') # Right player down
    
    while True:
        Actor.window.update()
    
        #moving the ball
        Actor.ball.setx(Actor.ball.xcor()+ballxdirection)
        Actor.ball.sety(Actor.ball.ycor()+ballydirection)
    
        #border set up
        if Actor.ball.ycor()>290:
            Actor.ball.sety(290)
            ballydirection=ballydirection*-1
            Actor.ball.sety(Actor.ball.ycor()+ballxdirection) #bounce off the wall?

        if Actor.ball.ycor()<-290:
            Actor.ball.sety(-290)
            ballydirection=ballydirection*-1
            Actor.ball.sety(Actor.ball.ycor()+ballxdirection) #bounce off the wall?

        if Actor.ball.xcor() > 390:
            Actor.ball.goto(0,0)
            ballxdirection = ballxdirection*-1
            playerAscore = playerAscore + 1
            Actor.pen.clear()
            Actor.pen.write("Player A: {}                    Player B: {} ".format(playerAscore,playerBscore),align="center",font=('Monaco',24,"normal"))
    
    
        if(Actor.ball.xcor()) < -390: # Left width paddle Border
            Actor.ball.goto(0,0)
            ballxdirection = ballxdirection * -1
            playerBscore = playerBscore + 1
            Actor.pen.clear()
            Actor.pen.write("Player A: {}                    Player B: {} ".format(playerAscore,playerBscore),align="center",font=('Monaco',24,"normal"))
    
        # Handling the collisions with paddles. 
        if(Actor.ball.xcor() > 340) and (Actor.ball.xcor() < 350) and (Actor.ball.ycor() < Actor.rightpaddle.ycor() + 40 and Actor.ball.ycor() > Actor.rightpaddle.ycor() - 40):
            Actor.ball.setx(340)
            ballxdirection = ballxdirection * -1
    
        if(Actor.ball.xcor() < -340) and (Actor.ball.xcor() > -350) and (Actor.ball.ycor() < Actor.leftpaddle.ycor() + 40 and Actor.ball.ycor() > Actor.leftpaddle.ycor() - 40):
            Actor.ball.setx(-340)
            ballxdirection = ballxdirection * -1