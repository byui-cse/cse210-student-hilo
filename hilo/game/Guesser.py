import random
class Guesser:
    """The responsibility of this class of objects is to play the game - choose the card, add or subtract points from the total, guess whether the next card will be lower or higher, and determine whether the player can guess again.
    
    Attributes: 
        points (number): The number of points added or taken away per round
    """
    points = 300
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


    def __init__(self):
        """Class constructor. Decares and initializes instance attributes.

        Args:
            self (Guesser): An instance of Guesser.
        """
        self.cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    def deal_first_card(self):
        """Deals (prints) a random card to the user.
        Args:
            self (Dealer): An instance of Dealer.
        Returns:
            int: Value representing the integer representation of the card for comparison.
        """
        randomCardIndex = random.randint(0,12)
        print(f'The card is: {self.cards[randomCardIndex]}')
        return randomCardIndex

    def deal_second_card(self):
        """Deals (prints) a random card to the user.
        Args:
            self (Dealer): An instance of Dealer.
        Returns:
            int: Value representing the integer representation of the card for comparision.
        """
        randomCardIndex = random.randint(0,12)
        print(f'The next card was: {self.cards[randomCardIndex]}')
        return randomCardIndex
    def choose_card(self):
        card1 = self.dealer.deal_first_card()
        guess = input(f'High or Low? (h/l)').lower

        guess = input(f'High or Low? (h/l)').lower()
        card2 = self.dealer.deal_second_card()
        if guess == 'l':
            if card2 <= card1:
                return True
            else:
                return False
        elif guess == 'h':
            if card2 >= card1:
                return True
            else:
                return False

    def get_points(self):
    

    def can_guess(self):

