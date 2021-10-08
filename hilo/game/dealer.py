import random

class Dealer:
    """A code template for a person who deals the card. This class of objects is in charge of 
    drawing the card, asking if the user wants to guess higher or lower, and recording the number
    drawn, and keeping track of the score at each instance of a draw.

    Attributes:
        draw_card (integer): Takes the user's guess and returns an integer representing the card pulled.
        get_points (number): The total number of points earned from a round.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Dealer): An instance of Dealer.
        """
        self.num_draws = 0
    
    def get_points(self):
        """Gets the total number of points earned from a draw.

        Args:
            self (Dealer): An instance of Dealer.
            rolled_numbers (list): The list containing the numbers of the dice.
        Return:
            Integer
        """
        points = 0

        for die in self.dice:
            if die == 1:
                points += 100
            elif die == 5:
                points += 50
            else:
                points += 0
        
        return points

    def draw_card(self):
        """Displays current card, gets guess from the user, gets a random number between 1 and 13
        for the new card.
        
        Args:
            self (Dealer): An instance of Dealer.
        """
        numbers = [1, 2, 3, 4, 5, 6]
        self.dice = []
        self.num_throws += 1

        for _ in range(5):
            self.dice.append(random.choice(numbers))