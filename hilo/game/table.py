from .dealer import Dealer

import random

class Table:

    def __init__(self):
        self.points = 300
        self.currrent_guess = None
    

    def get_guess(self):
        guess = input("Higher or Lower? H/L ")
        if guess not in ["H","h","L","l"]:
            print("Choose H/L")
            
            return self.get_guess()

        self.current_guess = guess
        return guess    

    def calculate_points(self, last_card, first_card):
        if self.current_guess in ["h","H"]:
            return 100 if last_card > first_card else -75
        else:    
            return 100 if last_card <first_card else -75 # this is cool, but I dont know why it works found in reeses game


