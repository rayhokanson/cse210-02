import random
from game.TerminalService import TerminalService

class Word:

    def __init__(self):
        self.TerminalService = TerminalService()
        self._current_word = ""
        self._words = ["anger", "apple", "beach", "earth", "avoid"]
        self.pick_a_word()
        self._word_guess = ["_"] * len(self._current_word)

    def pick_a_word(self):
        self._current_word = random.choice(self._words)

    def get_current_word(self):
        return self._current_word

    def draw_word_guess(self):
        for i in self._word_guess:
            self.TerminalService.write_text_no_new_line(i + " ")
        print()

    def check_letter(self, letter):
        if letter in self._current_word :
            guess_index = self._current_word.index(letter)
            new = list(self._word_guess)
            new[guess_index] = letter    
            self._word_guess = ''.join(new)
            return True
        else:
            return False
            

    def check_word(self):
        if self._current_word == self._word_guess:
            return True
        else:
            return False

