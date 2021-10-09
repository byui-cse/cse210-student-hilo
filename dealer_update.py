from random import choice
import random
from player_update import Player

class Dealer:

    def __init__(self):
        self.player = Player()
        
        self.keep_playing = "y"
        self.new_point = 0
        # For fun
        print("Deal...")

        # Self explanatory
        while self.keep_playing == "y": # This suppose repeat all the program until player says No.
            self.score = self.player.show_point() # To show the player's first piont......not really neccessary in the program
            while self.new_point != self.score:  # This will keep repeating the program as along as player still want to play
                self.new_card = self.generate_cards() # Deal first card
                self.prompt = self.player.player_guess("Higher or lower? [h/l] ") # player's guess'
                self.old_card = self.next_card() # Second card to deal

                # this will make some decisions based on the player's choice and card number and calculate the new point.
                if self.prompt == "h" and self.old_card > self.new_card:
                    point = self.score + 100
                    self.new_point == point
                    print(f"Your score is {self.new_point}")
                elif self.prompt == "l" and self.old_card < self.new_card:
                    point = self.score - 75
                    self.new_point == point
                    print(f"Your score is {self.new_point}")
                else:
                    print("You need to input h or l lowercases")
                self.keep_playing = input("Do you want to keep playing? [y/n] ")
                print()
           

    # Generates random cards for first deal
    def generate_cards(self): 
        self.card = random.randint(1, 13)
        print(f"The card is: {self.card}")
        return self.card
    # Generates random cards for second deal
    def next_card(self):
        self.card = random.randint(1, 13)
        print(f"The card was: {self.card}")
