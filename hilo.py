import random

# TODO: Implement the Die class as follows...

# 1) Add the class declaration. Use the following class comment.
class Hilo:
    

# 2) Create the class constructor. Use the following method comment.
    def __init__(self):
        """Constructs a new instance of Die with a value and points attribute.

        Args:
            self (Die): An instance of Die.
        """
        self.value = 0
        self.points = 0
# 3) Create the roll(self) method. Use the following method comment.
    def roll(self):
        """Generates a new random value and calculates the points.
        
        Args:
            self (Die): An instance of Die.
        """
        self.points = 300 if self.value == 100 else 75 if self.value == 1 else 0
        self.value = random.randint(1, 13) 