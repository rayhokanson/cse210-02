import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycles collide
    with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast, script)

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycle collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """

        cycles = cast.get_actors("cycles")
        cycle1 = cycles[0]
        cycle2 = cycles[1]
        
        head1 = cycle1.get_segments()[0]
        segments1 = cycle1.get_segments()[1:]
        head2 = cycle2.get_segments()[0]
        segments2 = cycle2.get_segments()[1:]

        for segment in segments1:
            if head1.get_position().equals(segment.get_position()):
                self._is_game_over = True
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True

        
        for segment in segments2:
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
            if head1.get_position().equals(segment.get_position()):
                self._is_game_over = True
        
        
    def _handle_game_over(self, cast, script):
        """Shows the 'game over' message and turns the cycles white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycles = cast.get_actors("cycles")
            cycle1 = cycles[0]
            cycle2 = cycles[1]

            segments1 = cycle1.get_segments()
            segments2 = cycle2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments1:
                segment.set_color(constants.WHITE)

            for segment in segments2:
                segment.set_color(constants.WHITE)

            growTailAction = script.get_actions("update")[1]
            script.remove_action("update", growTailAction)