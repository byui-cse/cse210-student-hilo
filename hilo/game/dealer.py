from random import choice
from typing import Match
from game.player import Player

class Dealer:

    def __init__(self):
        self.player = Player()
        self.keep_playing = True
        self.cards = self.player.card_set
    
    def start_dealing(self):
        # For fun
        print("Deal...")

        # Self explanatory
        self.player.generate_cards()

        while self.keep_playing:
            self.current_card = self.enhance_cards(self.cards)
            self.next_card(self.current_card)
            self.present_points(self.current_card)

    def next_card(self, current_card):
        print(f"The card is: {current_card}")

        choice = input("Higher or lower? [h/l] ")
        self.player.calculate_points(choice)

        # Remove the used card from the list and checks if there are still cards to play
        self.cards.pop(0)
        
    def present_points(self, current_card):
        print(f"The card was: {current_card}")

        points = self.player.points
        print(f"Your score is: {points}")

        play = input("Keep playing? [y/n] ")

        # Act on the dession to keep playing or not, and check if it's possible to do so
        if len(self.cards) == 0 or points <= 0 or play == "n":
            self.keep_playing = False

        elif play == "y":
            self.keep_playing = True

        # In case of a typo
        elif play != "y" and play != "n":
            print(f"Sorry, '{play}' is not an option. GAME OVER!")
            quit()

        # Just to be sure it is exhaustive
        else:
            self.keep_playing = False

    def enhance_cards(self, cards):

        current_card = cards[0]
        # Simple enhancer, could be commented out without affecting anything else
        if current_card == 1:
            current_card = "A"
        elif current_card == 11:
            current_card = "J"
        elif current_card == 12:
            current_card = "Q"
        elif current_card == 13:
            current_card = "K"

        return current_card
