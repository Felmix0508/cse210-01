from game.hilo import Hilo


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.game = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0

        for i in range(5):
            hilo = Hilo()
            self.game.append(hilo)

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
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        player_card = input("Higher or lower? [h/l] ")
        self.is_playing = (player_card == "h" or player_card == "l")
        if player_card != "h":
            self.score = 100 - self.total_score
        elif player_card != "l":
            self.score = 75 - self.total_score
    def do_updates(self):
        if not self.is_playing:
            return True

        for i in range(len(self.game)):
            hilo = self.game[i]
            hilo.roll()
            self.score += hilo.points 
        self.total_score += self.score

    def do_outputs(self):
        
        if not self.is_playing:
            return False
        
        values = ""
        for i in range(len(self.game)):
            hilo = self.game[i]
            values += f"{hilo.value} "

        print(f"Next card was: {values}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)