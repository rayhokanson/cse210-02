from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveRacketsAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        # racket1
        racket1 = cast.get_first_actor(RACKET1_GROUP)
        body1 = racket1.get_body()
        velocity1 = body1.get_velocity()
        position1 = body1.get_position()
        y1 = position1.get_y()
        
        position1 = position1.add(velocity1)

        if y1 < 0:
            position1 = Point(position1.get_x(), 0)
        elif y1 > (SCREEN_HEIGHT - RACKET1_HEIGHT):
            position1 = Point(position1.get_x(), SCREEN_HEIGHT - RACKET1_HEIGHT)
            
        body1.set_position(position1)

        #racket2
        racket2 = cast.get_first_actor(RACKET2_GROUP)
        body2 = racket2.get_body()
        velocity2 = body2.get_velocity()
        position2 = body2.get_position()
        y2 = position2.get_y()

        position2 = position2.add(velocity2)

        if y2 < 0:
            position2 = Point(position2.get_x(), 0)
        elif y2 > (SCREEN_HEIGHT - RACKET2_HEIGHT):
            position2 = Point(position2.get_x(), SCREEN_HEIGHT - RACKET2_HEIGHT)

        body2.set_position(position2)

