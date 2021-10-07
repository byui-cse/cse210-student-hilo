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
        deck = self.deck.copy

        rand_card = random.randint(0,len(deck))

        first_card = deck.pop[rand_card]
        second_card = deck.pop[rand_card]

        print( deck )
        print( first_card )
        print( second_card )
        print( deck )

        return first_card, second_card

dealer = Dealer()
dealer.dealer_card()