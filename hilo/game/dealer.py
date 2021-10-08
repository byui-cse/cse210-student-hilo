from game.player import Player
import random

class Dealer:
    def __init__(self):
        self.keep_playing = True
        self.firstCard = 0

    def start_game(self):
        while self.keep_playing:
            self.firstCard = self.get_card
            print(f"The card is: {self.firstCard}")
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        pass

    def do_updates(self):
        pass

    def do_outputs(self):
        pass

    def higher_or_lower(self):
        pass

    def get_card(self):
        # Returns a card between 1 - 13
        return random.randrange(1,13)