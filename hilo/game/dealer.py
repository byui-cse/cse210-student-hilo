import random

class Dealer():

    def __init__(self):
        '''
        The class constructor.

        Args:
            self (Dealer): an instance of Dealer
        '''

        self.deck = [1,2,3,4,5,6,7,8,9,10,11,12,13]

    def dealer_card(self):
        '''
        Draws a two random cards
        '''
        deck = self.deck.copy()
        deck_size = len(deck)

        rand_card = random.randint(0,deck_size)
        first_card = deck.pop(rand_card)
        
        deck_size = len(deck)
        rand_card = random.randint(0,deck_size)
        second_card = deck.pop(rand_card)

        return first_card, second_card