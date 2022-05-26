from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.word import Word

class Director:
    
    def __init__(self):
        
        self._isplaying = True
        self._jumper = Jumper()
        self._word = Word()
        
    def start_game(self):
        
        while self._isplaying:
            self._do_ouputs()
            self._get_inputs()
            self._do_updates()
            self._isplaying = False
            
    
    def _get_inputs(self):
        
        pass
    def _do_updates(self):
        pass
        
    def _do_ouputs(self):
        self._word.draw_word_guess()
        self._jumper.draw_jumper()