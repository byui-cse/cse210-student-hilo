"""
The game package contains the classes for playing Hilo.
"""
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
        Args:
            self (Dealer): An instance of Dealer.
            Artributes: 
            The initial points is 300. This is the point given to the player at the start of the game.
            The winning hand points is 100. It is the point the player gets when he guess right or when he/she wins.
            The losing hand points is 75. This a player loses when he/she loses in the game.
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
            

   

    
    
        
