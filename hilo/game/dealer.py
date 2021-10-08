import random
from typing import NewType

class Dealer:
    '''The responsibilites of the dealer is to track and generate cards, determine score for the guess.

    Attributes:
        previous_card (int): previous card value
        new_card (int): the new card value

    '''

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        self.previous_card = 7
        self.new_card = 7


    def deal_card(self):
        '''Will reassign previous card value and genrate new card value

        Args:
            self (Dealer): an instance of Dealer.
        '''


    def compare_card(self, guess):
        '''Will compare previous card with new card and will return score.

        Args:
            self (Dealer): an instance of Dealer.
            guess (str): player guess
        
        '''