from game.TerminalService import TerminalService

class Parachute:
    def __init__(self):
        self.terminalService = TerminalService()
        self.glider = [
        '     ___  ',
        '    /___\ ',
        '    \   / ',
        '     \ /  ',
        '      0   ',
        '     /|\  ',
        '     / \  '

        ]

    def print_parachute(self):
        for i in self.glider:
            self.terminalService.write_text(i)

    def remove_parachute_piece(self):
        self.glider.pop(0)

    # check if they have parachute