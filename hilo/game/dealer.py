import random

class Dealer:
    """A code template for a person who throws the cards. The responsibility 
    of this class of objects is to get the initial deck, shuffle it, throw the 
    cards, compare the cards, score for each draw, and determine whether 
    or not it can throw again.
    
    Attributes:
        deck (list): A list of all the cards of a deck, with all the four 
                    suits(Spades, Club, Hearts, Diamonds) ranging from 1
                    to 13 (Ace through the King).
    """

    def shuffle_deck(self):
        """
        This function suffle the initial deck.

        Attributes: None
        """
        random.shuffle(self.deck)

    def can_throw(self, score):
        """Determines whether or not the Dealer can throw again according to 
        the rules. 
        Args: 
            self (Dealer): An instance of Dealer.
        
        Returns:
            boolean: True if the list of dice has at least a five, or a one, or 
            the number of throws is zero; false if otherwise.
        """
        if score > 0 and len(self.deck) > 0:
            return True
        else:
            return False
        #return (score > 0 and len(self.deck) > 0)

    
    def throw_card(self):
        """Pick a card from the bottom of the deck and returns it.
        Args: 
            self (Dealer): An instance of Dealer.
        """
        return self.deck.pop()