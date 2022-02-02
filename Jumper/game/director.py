# Created on Feb , 2022 by:
# * Ray Hokanson
# * Gabriel Guerrero
# * Matt Shannon
# * Nathan Ornaghi Kutomi
# * Pierre Aguirre

from game.parachute import parachute

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card1 (int): first card
        card2 (int): Second card
        is_playing (boolean): Whether or not the game is being played.
        score (int): game score
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card1 = 0
        self.card2 = 0
        self.is_playing = True
        self.score = 300

