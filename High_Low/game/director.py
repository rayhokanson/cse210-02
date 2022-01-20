from game.cards import Cards


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
        #self.total_score = 0


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        # loop through game while self.is_playing is true.
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """

        # stop game if player chooses
        if self.is_playing == False:
            return

        #stop game of score is 0    
        if self.score == 0:
            return

        # Create instance of card
        card = Cards()

        # run deal to get card
        card.Deal()

        # assign card to card1
        self.card1 = card.card

        # run deal to get card
        card.Deal()

        # assign card to card2
        self.card2 = card.card

        # display current card
        print(f"The card is: {self.card1}")

        # prompt for hi or lo
        self.high_low = input("Higher or lower? [h/l] ")
      
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        # stop game if player chooses
        if not self.is_playing:
            return 
        
        #stop game of score is 0    
        if self.score == 0:
            self.is_playing = False
            return

        # check cards and assign points.
        if self.high_low == "l" and self.card2 < self.card1:
            self.score += 100
        elif self.high_low == "l" and self.card2 > self.card1:
            self.score -= 75
        elif self.high_low == "h" and self.card2 > self.card1:
            self.score += 100
        elif self.high_low == "h" and self.card2 < self.card1:
            self.score -= 75

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        # stop game if player chooses
        if self.is_playing == False:
            return

        #stop game of score is 0    
        if self.score == 0:
            self.is_playing = False
            #return

        # print results
        print(f"Next card was: {self.card2}. Your score is: {self.score}")
        
        # prompt to play again
        self.is_playing = input("Play again? [y/n] ")

        # stop game if player chooses
        if self.is_playing == "n":
            self.is_playing = False
            return