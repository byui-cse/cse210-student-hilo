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
        # Array to hold 2 card numbers.
        self.cards = []
    
    def get_card(self):
        """Draws card number
        
        Args:
            Self(Player): An instance of Player."""
        # random number between 1-13 is generated and added to the list.
        self.cards.append(random.randrange(1,14))

    
    def get_guess(self):
        """Determines if the user can throw again. Returns True or False.
        Args:
            Self(Thrower): An instance of Thrower.
        """
        guess = input('Higher or lower? [h/l] ')

        assert type(guess) == type('string')
        return guess
    

    def get_points(self, guess):
        """Calculates the number of points for each turn. Returns an integer.
        Args:
            Self(Player): An instance of Player."""

        assert type(guess) == type('string')
        # Points are returned according to user input
        if guess == 'h':
            if self.cards[1] > self.cards[0]:
                return 100
            else:
                return (-75)
        
        if guess == 'l':
            if self.cards[1] < self.cards[0]:
                return 100
            else:
                return (-75) 

    def clear_list(self):
        """Clears the card list.
        Args:
            Self(Player): An instance of Player."""
        
        # Clears first item of the array.
        self.cards.pop(0)
        