import random

class Dealer:
    def __init__(self):
        self.rand = random()
        self.deck = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

    def getCard(self):
        return self.rand.randInt(0, 12)

