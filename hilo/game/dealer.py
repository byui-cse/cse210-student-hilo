import random

class Dealer:
    def __init__(self):
        # Initialize random object to use for randomly drawing a "card"
        self.rand = random()
        # Initialize deck to create a more user friendly view of the "card" drawn
        self.deck = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

    def getCard(self):
        # Returning a random Int for the director to handle for comparison, then access the dealer's deck for display.
        return self.rand.randInt(0, 12)

