import random

class Player:
    """A code template for a player who guesses if the next card drawn 
    by the dealer will be higher or lower than the previous one. 
    The responsibility of this class of objects is can play, 
    get points, and displays the cards
    
    Attributes:
        
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.
        Args:
            self (Player): An instance of Player.
        """
        self.card_guess = False

        self.num_points = 300

    def can_play(self):
        """Determines whether or not the Player can play again according to 
        the rules. 
        Args: 
            self (Player): An instance of Player.
        
        Returns:
            boolean: True if the number of points is 300; false if otherwise.
        """
        return (self.num_points == 0)

    def get_points(self):
        """Calculates the total number of points for the current display. 
        The player earns 100 points if they guessed correctly.
        The player loses 75 points if they guessed incorrectly.
        Args: 
            self (Player): An instance of Player.
        
        Returns:
            number: The total points for the current play.
        """
        if self.card_guess == True:
            self.num_points += 100
        else:
            self.num_points -= 75

        return self.num_points

    def displays_cards(self):
        """Displays cards by randomly generating a new value from 1 to 13. 
        Args: 
            self (Player): An instance of Player.
        """

        result = random.randint(1, 13)
