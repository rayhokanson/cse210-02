import random
from game.termainal_service import TermainalService # Ray from meeting

class Word:

    def __init__(self):
        self.TerminalService = TermainalService() # Ray from meeting
        self._current_word = ""
        self._words = ["aloha", "crazy", "jumpy", "pizza", "grape", "jokes", "water"]
        self._word_guess = [" "] * len(self.pick_a_word()) # Ray from meeting

    def pick_a_word(self):
        self._current_word = random.choice(self._words)

    def get_current_word(self):
        return self._current_word

    def draw_word_guess(self): # Ray from meeting to draw parts of word above jumper
        for i in self._word_guess:
            self.TerminalService.write_text_no_new_line(i + " ")