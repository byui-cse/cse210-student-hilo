import random

class table:
    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (draw): An instance of draw.
        """
        self.card_num = 0
    
    def first_draw(self):
        """Determines whether or not the Player has been dealt cards yet.
        Args: 
            self (Dealer): An instance of Deal.
        
        Returns:
            boolean: True if the the Player has not been dealt cards yet. False if the Player has been dealt cards.
        """
        if self.card_num == 0:
            self.card_num += 1
            return True
            
        else:
            self.card_num += 1
            return False   
        
    def draw_card(self):
        """Draws random number attributed to card. 

        Args: 
            self (Dealer): An instance of Dealer.
        """
        card = random.randint(1, 14)
        return card
        
