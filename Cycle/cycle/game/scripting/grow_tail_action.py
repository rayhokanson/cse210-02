from game.scripting.action import Action


class GrowTailAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of GrowTailAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self):
        """Constructs a new GrowTailAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._times = 0 #added timer

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        cycles = cast.get_actors("cycles")
        cycle1 = cycles[0]
        cycle2 = cycles[1]

        #Add segment over time
        if self._times == 5:
            cycle1.grow_tail(1)
            cycle2.grow_tail(1)
            self._times = 0 #reset timer
        else:
            self._times+=1



