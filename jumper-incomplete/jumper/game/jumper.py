from game.terminal_service import TerminalService
class Jumper:
    
    def __init__(self):
        self.terminalService = TerminalService()
        self._jumper = [
            "   ____",
            "   /___\\",
            "   \\   /",
            "    \\ /",
            "      O",
            "     /|\\",
            "     / \\",
            "",
            "^^^^^^^"
        ]
    
    def draw_jumper(self):
        for drawing in self._jumper:
            self.terminalService.write_letters(drawing)
    
    def deleting_jumper(self):
        self._jumper.pop(0)
        
    def middle_parachute(self):
        return len(self.middle_parachute) >= 6
    
    def parachute_end(self):
        self._jumper[0] = " x"
    