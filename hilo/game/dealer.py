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

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.
        Attributes:
            self (Dealer): An instance of Dealer.
            self.initial_points: The initial points is 300. This is the point given to the player at the start of the game.
            self.winning_hand_points: The winning hand points is 100. It is the point the player gets when he guess right or when he/she wins.
            self.losing_hand_points: The losing hand points is 75. This a player loses when he/she loses in the game.
            ranks: The cards ranging from 1 (Ace) to 13 (King).
            suits: The four suits forming the deck (Spades, Clubs, Hearts, Diamonds)
        """
        self.initial_points = 300
        self.winning_hand_points = 100
        self.losing_hand_points = 75

        self.deck = []

        ranks = ["Ace", "2", "3", "4", "5", "6", "7",
                 "8", "9", "10", "Jack", "Queen", "King"]
        suits = {"Spades": "\u2664", "Clubs": "\u2667",
                 "Hearts": "\u2661", "Diamonds": "\u2662"}
        value = 1
        for rank in ranks:
            for suit in suits:
                self.deck.append([rank + " of " + suits[suit], value])
            value = value + 1

            
    def shuffle_deck(self):
        """
        This function suffle the initial deck.

        Attributes:
            self (Dealer): An instance of Dealer.
        """
        random.shuffle(self.deck)
        

    def can_throw(self, score):
        """Determines whether or not the Dealer can throw again according to 
        the rules. 
        Attributes:
            self (Dealer): An instance of Dealer.
        Args: 
            score: the accumulated score of the play.
        
        Returns:
            boolean: True if the score is higher than 0 and there are still
            cards left in the deck; false if otherwise.
        """
        if score > 0 and len(self.deck) > 0:
            return True
        else:
            return False


    def get_points(self, current_card, next_card):
        """Ask the user for a guess (h or l), and calculates the total number of 
        points for the current throw. 
        Attributes:
            self (Dealer): An instance of Dealer.
        Args:
            current_card: the atrtibute that represent the card
                          which the dealer is displaying in real time.
            next_card:  attribute that represent the card that the dealer
                        is going to display next.
        
        Returns:
            number: The total points for the current round.
        """
        while True:
            print(f"\nThe current card is: {current_card[0]}")
            self.answer = input("Higher or lower? [h/l] ")
            if self.answer.lower() == "h" or self.answer.lower() == "l":
                break
            else:
                print("Please, enter a valid answer [h/l]")

        if self.answer.lower() == "h" and next_card[1] > current_card[1]:
            print("You Won!")
            return self.winning_hand_points

        elif self.answer.lower() == "h" and next_card[1] < current_card[1]:
            print("You Lost!")
            return -self.losing_hand_points

        elif self.answer.lower() == "l" and next_card[1] < current_card[1]:
            print("You Won!")
            return self.winning_hand_points

        elif self.answer.lower() == "l" and next_card[1] > current_card[1]:
            print("You Lost!")
            return -self.losing_hand_points

        else:
            print("Draw!")
            return int(0)


    def throw_card(self):
        """Pick a card from the bottom of the deck and returns it.
        Attributes: 
            self (Dealer): An instance of Dealer.
        """
        return self.deck.pop()
