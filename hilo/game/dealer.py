import random
from game.style import *


class Dealer:
    def __init__(self):
        self.deck = list(range(1, 14))
        self.current_card = None
        self.last_card = None

    def draw_card(self):
        """Gets a random card from the remaining cards & removes it from the deck."""
        card = self.deck.pop(self.deck.index(random.choice(self.deck)))
        print_white(f"\nDealer Drew The Card: {card}")
        print_reset()
        self.last_card = self.current_card
        self.current_card = card
        return card
