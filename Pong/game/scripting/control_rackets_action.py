from constants import *
from game.scripting.action import Action


class ControlRacketsAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        # racket1
        racket1 = cast.get_first_actor(RACKET1_GROUP)
        if self._keyboard_service.is_key_down(UP1):
            racket1.swing_up()
        elif self._keyboard_service.is_key_down(DOWN1):
            racket1.swing_down()
        else: 
            racket1.stop_moving()

        #racket2
        racket2 = cast.get_first_actor(RACKET2_GROUP)
        if self._keyboard_service.is_key_down(UP2):
            racket2.swing_up()
        elif self._keyboard_service.is_key_down(DOWN2):
            racket2.swing_down()
        else:
            racket2.stop_moving()