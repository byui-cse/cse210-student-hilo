from random import choice
from typing import Match
from game.player import Player

class Dealer:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        player (Player): An instance of the class of objects known as Player.
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Dealer): An instance of Dealer.
        """
        self.keep_playing = True
        self.player = Player()
    
    def start_dealing(self):
        # For fun
        print("\n------ Welcome to Hilo Game ------")
        print("Deal...")

        # Self explanatory
        card = self.player.generate_card()
        self.player.populate_cards_set(card)

        while self.keep_playing:
            self.next_card()

    def next_card(self):
        # Control the game giving the next card and printing important info about it.
        current_card = self.player.generate_card()
        last_card = self.player.get_last_card()
        print(f"\nThe card is: {last_card}")

        choice = input("Higher or lower? [h/l] ")
        answer = ''

        if current_card > last_card:
            answer = 'h'
        elif current_card < last_card:
            answer = 'l'
        
        # Compute score based on player's answer
        if choice.lower() == 'h' or choice.lower() == 'l':
            if choice.lower() == answer:
                self.player.compute_points('add')
            else:
                self.player.compute_points('remove')
        else:
            print(f"Sorry, '{choice}' is not an option. GAME OVER!")
            quit()

        print(f"The card was: {current_card}")

        self.player.populate_cards_set(current_card)
        self.present_points()
      
    def present_points(self):
        # Display the points and verify if the player want to keep playing.
        points = self.player.points
        print(f"Your score is: {points}")

        play = input("Keep playing? [y/n] ")

        # Act on the dession to keep playing or not, and check if it's possible to do so.
        if len(self.player.card_set) == 0 or points <= 0 or play == "n":
            self.keep_playing = False

        elif play == "y":
            self.keep_playing = True

        # In case of a typo
        elif play != "y" and play != "n":
            print(f"Sorry, '{play}' is not an option. GAME OVER!")
            self.keep_playing = False

        # Just to be sure it is exhaustive
        else:
            self.keep_playing = False
