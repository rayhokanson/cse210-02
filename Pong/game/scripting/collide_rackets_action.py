from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideRacketsAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        racket1 = cast.get_first_actor(RACKET1_GROUP)
        racket2 = cast.get_first_actor(RACKET2_GROUP)
        
        ball_body = ball.get_body()
        racket1_body = racket1.get_body()
        racket2_body = racket2.get_body()

        if self._physics_service.has_collided(ball_body, racket1_body) or \
                self._physics_service.has_collided(ball_body, racket2_body):
            ball.bounce_x()
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)
