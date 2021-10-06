from game.style import *


class Player:
    """
    The Player Class represents the player in the game.
    """
    def __init__(self):
        self.points = 300
        self.current_guess = None

    def get_high_low_guess(self):
        """Gets user input from the player for their H / L guess.
        Args:
            self (Player): An instance of Player.
        """
        guess = input("Higher or Lower? [H/L]: ")
        if guess not in ["H", "h", "L", "l"]:
            # Validates the input
            print_red("Please Choose H/L!")
            print_reset()
            return self.get_high_low_guess()
        # sets current guess
        self.current_guess = guess
        return guess

    def calculate_points(self, last_card, current_card):
        """Calculates the points, positive or negative, from a given card pair.
        Args:
            self (Player): An instance of Player.
            last_card (int)
            current_card (int)
        """
        if self.current_guess in ["H", 'h']:
            return 100 if last_card > current_card else -75
        return 100 if last_card < current_card else -75
