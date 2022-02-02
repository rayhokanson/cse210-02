import random

class Word:

    def __init__(self):
        self._current_word = ""
        self._words = ["aloha", "crazy", "jumpy", "pizza", "grape", "jokes", "water"]

    def pick_a_word(self):
        self._current_word = random.choice(self._words)

    def get_current_word(self):
        return self._current_word