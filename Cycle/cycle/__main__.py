import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.cycle import Cycle #Updated
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.grow_tail_action import GrowTailAction #added grow_tail_action class
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("cycles", Cycle(constants.RED)) # Added two cycles
    cast.add_actor("cycles", Cycle(constants.GREEN)) # Added two cycles
    cast.add_actor("scores", Score())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", GrowTailAction()) #added grow_tail_action class
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()