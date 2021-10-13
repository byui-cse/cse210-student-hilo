import random

class Player:
    """A code template for a person who plays the game. The responsibility of this 
    class of objects is to play the game, keep track of the cards and the score.
    
    Attributes:
        points: The current score in the game.
        card_set: The list of cards being played.
    """
    
    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Player): An instance of Player.
        """
        self.points = 300
        self.card_set = []

    def generate_card(self):
        """Generates a random card. 

        Returns:
            A card as an integer.
        """
        return random.randint(1, 13)

        # In case of wanting to cheat, uncomment that below
        # print(self.card_set)
    
    def populate_cards_set(self, current_card):
        """Populates the cards list for the game.

        Args: 
            current_card: Receives an integer as a card to store in the list.
        
            Verifies if the card was alredy in the list, and resets the list
            when it has 13 cards, saving only the last one.
        """
        card = current_card

        if len(self.card_set) < 13:
            while card in self.card_set:
                card = self.generate_card()
            else:
                self.card_set.append(card)
        else:
            last_card = self.get_last_card()
            self.card_set.clear()
            self.card_set.append(last_card)

    def get_last_card(self):
        """Returns the las card that was played. 

        Returns:
            A card as an integer.
        """
        index = len(self.card_set) - 1
        return self.card_set[index]
    
    def compute_points(self, result):
        """Computes the score of the player. 

        Returns:
            An integer with the sum of the points.
        """
        # Add points
        if result == 'add':
            self.points += 100

        # Subtract points
        elif result == 'remove':
            self.points -= 75
