from random import choice
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
            self.next_card(self.cards)
            self.present_points(self.cards)

    def next_card(self, cards):
        # cards = self.player.card_set
        print(f"The card is: {cards[0]}")

        choice = input("Higher or lower? [h/l] ")
        self.player.calculate_points(choice)

        # Remove the used card from the list and checks if there are still cards to play
        cards.pop(0)
        
    def present_points(self, cards):
        print(f"The card was: {cards[0]}")

        points = self.player.points
        print(f"Your score is: {points}")

        play = input("Keep playing? [y/n] ")

        # Act on the dession to keep playing or not, and check if it's possible to do so
        if len(cards) == 0 or points <= 0 or play == "n":
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