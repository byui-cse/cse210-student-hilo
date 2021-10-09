class Guesser:
    """The responsibility of this class of objects is to play the game - choose the card, add or subtract points from the total, guess whether the next card will be lower or higher, and determine whether the player can guess again.
    
    Attributes: 
        points (number): The number of points added or taken away per round
    """
    points = 300
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


    def __init__(self):
        """Class constructor. Decares and initializes instance attributes.

        Args:
            self (Guesser): An instance of Guesser.
        """
        self.cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        



choose_card()
get_points()
card
can_guess()
