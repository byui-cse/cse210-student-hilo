from random import randint

class Dealer():
    def __init__(self):
        self.card_active = 0
        self.points = 300
        self.choice = ""
        self.card_next = 0
    def get_user_choice(self):
        self.choice = input("Higher or lower? [h or l] ")  


    def get_points(self):
        """
        Keeps track of the number of points.
        """
        
    def can_play_again(self):
        """
        Checks to see if the player can play again.
        """
        if self.points <= 0:
            return False
        else:
            return True
    def get_card(self):
        """
        Generates a random number between 1 and 13 for the card number.
        """
        self.card_active = randint(1,13)
        self.card_next = randint(1,13)