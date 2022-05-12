from dealer import Dealer
import random
class Director:
    

    def __init__(self):
        self.game = []
        self.is_playing = True
        self.score = 300
        self.first_card = 0
        self.second_card = 0
        self.points = 0
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            
    def get_inputs(self):
        self.cards = random.randint(1, 13)
        self.number_card = random.randint(1, 13)
        for i in range(1):
            print(f"The card is: {self.number_card}")
        self.higher_or_lower = input("Higher or lower? [h/l] ")
        if self.higher_or_lower == "h":
            self.first_card >= self.second_card
            self.points += 100
        elif self.higher_or_lower == "l":
            self.first_card <= self.second_card
            self.points -= 75
        else:
            0
        print(f"Next card : {self.cards}")
        print(f"Your score is: {self.points}")
        play_again = input("Play again? [y/n]")
        self.is_playing = (play_again == 'y')
        print()
        
    def do_updates(self):

        None
    def do_outputs(self):
        
        None
