import random

class Dealer:
    """A code template for a person who deals cards in the game. The responsibility of 
    this class is to keep an arrauy of cards and deal the cards to the player.

    Attributes:
        cards (string array): Array of 13 strings representing card values.
    """

    #eber
    def __init__(self):
        pass

    #tyson
    def deal_first_card(self):
        """Deals (prints) a random card to the user.

        Args:
            self (Director): An instance of Dealer.
        Returns:
            int: Value representing the integer representation of the card for comparison.
        """
        randomCardIndex = random.randint(0,12)
        print(f'The card is: {self.cards[randomCardIndex]}')
        return randomCardIndex

    #tyson
    def deal_second_card(self):
        """Deals (prints) a random card to the user.

        Args:
            self (Director): An instance of Dealer.
        Returns:
            int: Value representing the integer representation of the card for comparision.
        """
        randomCardIndex = random.randint(0,12)
        print(f'The next card was: {self.cards[randomCardIndex]}')
        return randomCardIndex