
# Create a dictionary of values: "two" '2', "11", "Jack"
# Create tuple of suits
# Create a tuple of ranks
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
        'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12,'King':13,'Ace':14}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')

class Card:
    """
    A code template that facilitates the creation of cards.

    Attributes:
    suit = tuple
    rank = tuple
    value = values[rank]
    """
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit