from game.scripting.action import Action


class GrowTailAction(Action):
    """
    An update action that keeps tails growing.
    
    The responsibility of GrowTailAction is to grow cycles tails.
    """

    def __init__(self):
        """
        Constructs a new GrowTailAction.
        """
        self._times = 0 #added timer

    def execute(self, cast, script):
        """Executes the grow cycles tails.

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



