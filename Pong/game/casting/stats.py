from constants import *
from game.casting.actor import Actor


class Stats(Actor):
    """The game stats."""

    def __init__(self, debug = False):
        """Constructs a new Stats."""
        super().__init__(debug)
        self._score1 = 0
        self._score2 = 0
        # self._level = 1
        # self._lives = DEFAULT_LIVES
        # self._score = 0

    def add_points(self, points, player):
        """Adds the given points to the score of a player.
        
        Args:
            points: A number representing the points to add.
            player: The player's number, either 1 or 2.
        """
        if player == 1:
            self._score1 += points
        elif player == 2:
            self._score2 += points
  
    def get_score(self, player):
        """Gets the players score.

        Args:
            player: The player's number, either 1 or 2.

        Returns:
            A number representing the score.
        """
        if player == 1:
            return self._score1
        elif player == 2:
            return self._score2


    def reset(self):
        """Resets the stats back to their default values."""
        self._score1 = 0
        self._score2 = 0
