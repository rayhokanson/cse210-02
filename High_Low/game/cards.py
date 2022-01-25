import random


class Cards:
    """The responsibility of Cards is to keep track of the card value.
   
    Attributes:
        value (int): The number value of the card drawn.
    """

    def __init__(self):
        """Constructs a new instance of Cards.

        Args:
            self (Cards): An instance of Cards.
        """
        self.card = 0

    def Deal(self):
        """Generates a new random value and provides card amount.
        
        Args:
            self (card): An instance of Cards.
        """
        self.card = random.randint(1, 13)

