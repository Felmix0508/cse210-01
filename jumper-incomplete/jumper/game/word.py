from game.terminal_service import TerminalService

class Word:
    
    def __init__(self):
        self.terminalService = TerminalService()
        self._word_list = ["tacos", "progress", "marvel", "ring"]
        self._word_selected = "nest"
        self.select_words()
        self._word_guess = ["_"] * len(self._chosen_words)
    
    def select_words(self):
        self.select_words = self._word_selected
        
    
    def draw_word_guess(self):
        for i in self._word_guess:
            self.terminalService.write_letters(i + " ")
    
    def process_guess(self,guess_letter):
        self.guess_letter = self._word_guess.append(self._word_list)
    
    def can_keep_guessing(self):
        self._word_guess