import random
from game.TerminalService import TerminalService # Ray from meeting

class Word:

    def __init__(self):
        self.TerminalService = TerminalService() # Ray from meeting
        self._current_word = ""
        self._words = ["crazy"] #["aloha", "crazy", "jumpy", "pizza", "grape", "jokes", "water"]
        self.pick_a_word()
        self._word_guess = ["_"] * len(self._current_word) # Ray from meeting

    def pick_a_word(self):
        self._current_word = random.choice(self._words)

    def get_current_word(self):
        return self._current_word

    def draw_word_guess(self): # Ray from meeting to draw parts of word above jumper
        for i in self._word_guess:
            self.TerminalService.write_text_no_new_line(i + " ")

    def check_letter(self, letter):
        if letter in self._current_word :
            guess_index = self._current_word.index(letter)
            new = list(self._word_guess)
            new[guess_index] = letter    
            self._word_guess = ''.join(new)
            print(self._word_guess)
            return True
        else:
            return False
            

    def check_word(self):
        if self._current_word == self._word_guess:
            return True
        else:
            return False

