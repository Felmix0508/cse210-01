import random

# TODO: Implement the Die class as follows...

# 1) Add the class declaration. Use the following class comment.
class Dealer:
    
    
# 2) Create the class constructor. Use the following method comment.
    def __init__(self):
       
        self.first_card = 0
        self.second_card = 0
        self.points = 0
# 3) Create the roll(self) method. Use the following method comment.
    def deal(self):
        self.first_card = random.randint(1, 13)
        self.second_card = random.randint(1, 13)
    def get_points(self,higher_or_lower):
        if self.higher_or_lower == "h":
            self.first_card >= self.second_card
            self.points += 100
        elif self.higher_or_lower == "l":
            self.first_card <= self.second_card
            self.points -= 75
        else:
            0
    