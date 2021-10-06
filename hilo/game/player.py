from game.style import *


class Player:
    def __init__(self):
        self.points = 300
        self.current_guess = None

    def get_high_low_guess(self):
        guess = input("Higher or Lower? [H/L]: ")
        if guess not in ["H", "h", "L", "l"]:
            print_red("Please Choose H/L!")
            print_reset()
            return self.get_high_low_guess()
        self.current_guess = guess
        return guess

    def calculate_points(self, last_card, current_card):
        if self.current_guess in ["H", 'h']:
            return 100 if last_card > current_card else -75
        return 100 if last_card < current_card else -75
