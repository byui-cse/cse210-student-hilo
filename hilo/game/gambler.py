import random

class Gambler:
    """The player."""

    def __init__(self):
        """The class constructor."""
        self.new_card = random.randint(1,13)
        self.old_card = self.new_card
    
    def get_points(self,choice):
        self.sort_card()
        if self.new_card > self.old_card:
            point = "h"
        else:
            point = "l"
        self.old_card = self.new_card
        return (choice == point)
        

    def sort_card(self):
        self.new_card = random.randint(1,13)
        while self.new_card == self.old_card:
            self.new_card = random.randint(1,13)

    
