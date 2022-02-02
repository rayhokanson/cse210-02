class TerminalService:

    def __init__(self):
        pass

    def ask_guess(self):
        guess = "123"
        while not guess.isalpha(): 
            guess = input("Guess a letter [a-z]: ")
            
        return guess