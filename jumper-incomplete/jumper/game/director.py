from game.terminal_service import TerminalService
from game.word import Word
from game.jumper import Jumper

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
        self._word.terminalService.write_text("Enter a letter from [a-z]: ")
        letter = self._word.terminalService.read_letters(self._jumper.draw_jumper()) 
        
        
    def _do_updates(self):
        letter = self._get_inputs()
        self._word._word_guess = letter
        
        
             
    def _do_ouputs(self):
        self._word.draw_word_guess()
        self._jumper.draw_jumper()