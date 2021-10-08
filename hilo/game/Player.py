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
            Self(Player): An instance of Player.
        """
        self.cards = []
    
    def get_card(self):
        """Draws card number
        
        Args:
            Self(Player): An instance of Player."""
        self.cards.append(random.randrange(1,14))


    def get_guess(self):
        """Determines if the user can throw again. Returns True or False.
        Args:
            Self(Thrower): An instance of Thrower.
        """
        guess = input('Higher or lower? (h/l) ')

        return guess
    

    def get_points(self, guess):
        """Calculates the number of points for each turn. Returns an integer.
        Args:
            Self(Player): An instance of Player."""
        if guess.lower() == 'h':
            if self.cards[1] > self.cards[0]:
                return 100
            else:
                return (-75)
        
        if guess.lower() == 'l':
            if self.cards[1] < self.cards[0]:
                return 100
            else:
                return (-75) 

    def clear_list(self):
        """Clears the card list.
        Args:
            Self(Player): An instance of Player."""
        self.cards.pop(0)


#hola
        