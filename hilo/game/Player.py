"""
The game package contains the classes for playing Hilo.
"""
import random

# TODO: Define the Thrower class here.
class Player:
    """A code template for the player that will throw the decide and
    keep track of the points gained during each throw. Will also decide
    if they want to keep playing or not, assuming they can according to
    the game rules."""
    
    def __init__(self):
        """The class constructor.

        Args:
            Self(Thrower): An instance of Thrower.
        """
        self.dice = []
        self.num_throws = 0
    
    def throw_dice(self):
        """Represents the 5 dice the user will roll each turn. 
        Will return 5 numbers which will be added to dice list."""

        self.dice = []
        
        for num in range(0,5):
            self.dice.append(random.randrange(1,7))

    def can_throw(self):
        """Determines if the user can throw again. Returns True or False.
        Args:
            Self(Thrower): An instance of Thrower.
        """
        if self.dice.count(5)>0 or self.dice.count(1)>0:
            return True
        else:
            return False
    

    def get_points(self):
        """Calculates the number of points for each turn. Returns an integer.
        Args:
            Self(Thrower): An instance of Thrower."""
        if self.get_guess == 'h':
            if self.get_guess > self.get_card:
                return 100
            else:
                return (-75)
        
        if self.get_guess == 'l':
            if self.get_guess < self.get_card:
                return 100
            else:
                return (-75) 
