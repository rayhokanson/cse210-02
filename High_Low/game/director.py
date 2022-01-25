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


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        # Introduce Game
        print("\nHilo is a game in which the player guesses if the next card drawn by the dealer will be higher or lower than the previous one.\n")
        print("You start with 300 points")
        print("The current card is displayed and you guess if the next one is higher (h) or lower (l)")
        print("You get 100 points if guessed correctly")
        print("You lose 75 points if guessed incorrectly")
        print("The game is over when you reach 0 points or choose to stop playing")
        print("Good Luck!")

        # loop through game while self.is_playing is true.
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to play.

        Args:
            self (Director): An instance of Director.
        """

        # prompt to play again
        play_again = input("\nPlay again? [y/n] ")
        self.is_playing = (play_again == "y")

        # stop game if player chooses
        if play_again == "n":
            print("\nGreat Game. Thanks for playing!\n")
        
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
        print(f"\nThe card is: {self.card1}")

        # prompt for high or low
        self.high_low = input("Higher or lower? [h/l] ")
        
        
      
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        # stop game if player chooses
        if not self.is_playing:
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
        """Displays the card and the score.

        Args:
            self (Director): An instance of Director.
        """
        # stop game if player chooses
        if not self.is_playing:
            return
        
        # print results
        print(f"\nNext card was: {self.card2}. Your score is: {self.score}")
        self.is_playing = (self.score > 0)

        #stop game of score is 0
        if self.score <= 0:
            print("\nGame Over. Thanks for playing!\n")