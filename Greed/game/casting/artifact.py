from game.casting.actor import Actor
from game.shared.point import Point
import random


class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._message = ""
        self._type = random.choice([True, False])
        self._text = "*" if self._type == True else "O"
        self._velocity = Point(0, 3)

        
    def get_message(self):
        """Gets the artifact's message.
        
        Returns:
            string: The message.
        """
        return self._message
    
    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message

    def get_type(self):
        """Gets the artifact's type.
        
        Returns:
            boolean: The type.
        """
        return self._type
