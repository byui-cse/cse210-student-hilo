from game.gambler import Gambler

class Dealer:
    """A part of the code for the person that deals the cards
    The responsibility of the dealer is to give out cards and 
    to keep track of the score and call out the end of the game
    
    Atr.
    score 
    """


    def __init__(self):
        """The class constructor."""
        self.score = 300
        self.keep_playing = True
        self.gambler = Gambler()
        self.choice = ""
    
    def start_game(self):
        """this method leads the game start each loop"""
        while self.keep_playing:
            self.initial_input()
            self.update_score()
            self.final_input()

    def initial_input(self):
        """"""
        print(f"The card is: {self.gambler.old_card}")
        h_o_l = input("Higher or lower? [h/l] ")
        self.choice = h_o_l


    def update_score(self):
        """update the gambler score"""
        if self.gambler.get_points(self.choice):
            self.score += 100
        else:
            self.score -= 75

    def final_input(self):
        print(f"Next card was: {self.gambler.new_card}")
        if self.score <= 0:
            print("your score is: 0")
            self.keep_playing = False
        
        if self.keep_playing:
            print(f"Your score is: {self.score}")
            deal = input("Keep playing? [y/n] ")
            print()
            self.keep_playing = (deal == "y")
        else:
            self.keep_playing = False

        

