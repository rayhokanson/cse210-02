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
        self._parachute = Parachute()
        self._word = Word()
        self._is_playing = True
        self._terminal_service = TerminalService()
        self._guess = ""

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
    
        # Introduce Game
        print("\nJumper is a game in which the player seeks to solve a puzzle by guessing the letters of a secret word one at a time.")
        print("Start guessing letters! Good Luck!")

        # loop through game while self.is_playing is true.
        while self._is_playing:
            self.do_outputs()
            self.get_inputs()
            self.do_updates()


    def get_inputs(self):
        """Ask the user for a letter.

        Args:
            self (Director): An instance of Director.
        """
        # ask for input
        self._guess = self._terminal_service.ask_guess("\nGuess a letter [a-z]: ")

    def do_updates(self):
        """Check if guess is correct

        Args:
            self (Director): An instance of Director.
        """

        guess = self._guess
        if self._word.check_letter(guess):
            if self._word.check_word():
                self._is_playing = False
                print("You win!!!")
        else:
            self._parachute.remove_parachute_piece()
            if not self._parachute.has_parachute():
                self._parachute.parachute_gone()
                self._parachute.print_parachute()
                self._is_playing = False
                print("\nYou lost! That's a bummer...\n")

    def do_outputs(self):
        """Output the parachute, and the results from the guess

        Args:
            self (Director): An instance of Director.
        """
        self._parachute.print_parachute()
        self._word.draw_word_guess()
