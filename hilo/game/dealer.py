import random
from game.style import *


class Dealer:
    """
    The Dealer Class represents the dealer in the High Low game.
    """
    def __init__(self):
        """Initializes the deck, current_card and last_card"""
        self.deck = list(range(1, 14))
        self.current_card = None
        self.last_card = None

    def draw_card(self):
        """Gets a random card from the remaining cards & removes it from the deck.
        Args:
            self (Dealer): An instance of Dealer.
        """
        card = self.deck.pop(self.deck.index(random.choice(self.deck)))
        print_white(f"\nDealer Drew The Card: {card}")
        print_reset()
        # Sets last card to the current card before the current card it set to the card just drawn
        self.last_card = self.current_card
        # Sets the current card to the one just drawn
        self.current_card = card
        return card
