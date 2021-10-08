from game.dealer import Dealer
import random

class Table:

    def __init__(self):
        self.cards = random.randint(1-13)# this isn't correct, just thinking it through
        self.count_guesses = 0

#we need a method  that is called 
# it needs to decide if your score is 0 
# it needs to add 100 if you quessed correctly
# it needs to subtract 75 if you guessed wrong.
    def get_points(self):

        