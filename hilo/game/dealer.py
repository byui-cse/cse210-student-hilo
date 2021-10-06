from random import choice
from game.player import Player

class Dealer:

    def __init__(self):
        self.player = Player()
        self.keep_playing = True
    
    def start_dealing(self):
        # For fun
        print("Deal...")

        # Self explanatory
        self.player.generate_cards()
        self.present_points()

        while self.keep_playing:
            self.next_card()

    def present_points(self):
        print(f"Your current points: {self.player.points}")

    def next_card(self):
        cards = self.player.card_set
        print(f"The card is: {cards[0]}")

        choice = input("Higher or lower? [h/l] ")

        # TODO the whole point system needs to be built

        if choice == "h":
            # Add points
            print("+ points")

        elif choice == "l":
            # Subtract points
            print("- points")

        else:
            print("Sorry, that's not an option. GAME OVER!")
            quit()

        # Remove the used card from the list and checks if there are still cards to play
        cards.pop(0)
        if len(cards) == 0:
            self.keep_playing = False
