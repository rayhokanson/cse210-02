from constants import *
from game.scripting.action import Action


class DrawRacketsAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        racket1 = cast.get_first_actor(RACKET1_GROUP)
        body = racket1.get_body()

        if racket1.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        animation = racket1.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)

        racket2 = cast.get_first_actor(RACKET2_GROUP)
        body = racket2.get_body()

        if racket2.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)

        animation = racket2.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)
