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
            number: The total points for the current throw.
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
            
