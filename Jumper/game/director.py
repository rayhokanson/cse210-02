# Created on Feb , 2022 by:
# * Ray Hokanson
# * Gabriel Guerrero
# * Matt Shannon
# * Nathan Ornaghi Kutomi
# * Pierre Aguirre

from game.parachute import Parachute
from game.word import Word
from game.TerminalService import TerminalService

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        parachute (Parachute): display the parachute
        word (Word): pick a random word
        is_playing (boolean): Whether or not the game is being played.
        terminal_service (TermianalService): get all the prompts
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.parachute = Parachute()
        self.word = Word()
        self.is_playing = True
        self.terminal_service = TerminalService()
        self.guess = ""
        self.lives = 4

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
    
        # Introduce Game
        print("\nJumper is a game in which the player seeks to solve a puzzle by guessing the letters of a secret word one at a time.")
        print("Start guessing letters! Good Luck!")

        # prints out parachute glider
        self.parachute.print_parachute()

        # pick a random word 
        self.word.pick_a_word()

        # loop through game while self.is_playing is true.
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            # self.do_outputs()


    def get_inputs(self):
        """Ask the user for a letter.

        Args:
            self (Director): An instance of Director.
        """
        # ask for input
        self.guess = self.terminal_service.ask_guess("\nGuess a letter [a-z]: ")


    def do_updates(self):
        """Check if guess is correct

        Args:
            self (Director): An instance of Director.
        """
        self.parachute.remove_parachute_piece()



    def do_outputs(self):
        """Output the parachute, and the results from the guess

        Args:
            self (Director): An instance of Director.
        """
        pass
