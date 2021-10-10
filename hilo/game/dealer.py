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
        self.new_card = 0
        self.current_card = 0
    
    def get_points(self, highlow):
        """Gets the total number of points earned from a guess.

        Args:
            self (Dealer): An instance of Dealer.
            highlow (string): The user's choice of higher or lower
        Return:
            Integer
        """
        points = 0

        if highlow.lower() == "h":
            if self.new_card > self.current_card:
                points = 100
            else:
                points = -75
        elif highlow.lower() == "l":
            if self.new_card < self.current_card:
                points = 100
            else:
                points = -75
        
        return points

    def draw_card(self):
        """Draws two random cards, each with a value in the range of 1-13.
        
        Args:
            self (Dealer): An instance of Dealer.
        """
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        if self.num_draws == 0:
            self.current_card = random.choice(numbers)
        else:
            self.current_card = self.new_card
        self.new_card = random.choice(numbers)

        self.num_draws += 1