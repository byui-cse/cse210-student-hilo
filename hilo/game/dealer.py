import random

class Dealer():
    def __init__(self):
        self.card_num = 0
        self.points = 0

    def get_points(self):
        pass
    def can_play_again(self):
        
        pass
    def get_card(self):
        """
        Generates a random number between 1 and 13 for the card number.
        """
        self.card_num = random.randint(1,13)
