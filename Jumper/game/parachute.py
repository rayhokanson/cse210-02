from game.TerminalService import TerminalService

class Parachute:
    def __init__(self):
        self.terminalService = TerminalService()
        self._glider = [
        '     ___  ',
        '    /___\ ',
        '    \   / ',
        '     \ /  ',
        '      0   ',
        '     /|\  ',
        '     / \  ',
        '',
        '^^^^^^^'
        ]

    def print_parachute(self):
        print()
        for i in self._glider:
            self.terminalService.write_text(i)

    def remove_parachute_piece(self):
        self._glider.pop(0)
    
    # check if they have parachute
    def has_parachute(self):
        return len(self._glider) >= 6

    def parachute_gone(self):
        self._glider[0] = "      X"

