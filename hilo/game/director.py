from .table import Table
from .dealer import Dealer

class Director:

    def __init__(self):
        self.dealer =Dealer()
        self.table =Table()# I should have named this player
        self.keep_playing = True
        self.points =300

    def start_game(self):
        """ this starts the game . it should be a loop
        
        Args: self (Director): an instance of Director
        I still dont' know what that means but every file ive looked at has it so it stays
        
        """
        print("welcome to the game. ")
        print(""" Game play is as follows:
        Guess correctly and you get 100 points
        Guess incorrectly you lose 75 points. 
        If you lose all your points the game ends""")


        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_updates()#These are from the original dice game.

        
        print(f"your points {self.points}") 

        if self.points <= 0:
            print("game over")
    
    def get_inputs(self):
        """ gets all inputs from each round. draw cards, user guess
        
        Args: self (Director) An istance of Director.  (again)"""

        self.dealer.draw()
        self.table.get_guess()
        self.dealer.draw()
    
    def do_updates(self):
        """ updates information from each round.  the score.
        Args: self (Director) An instance of Director """

        add_points = self.table.calculate_points(self.dealer.first_card, self.dealer.second_card)
        if add_points >0:
            print( "+100")
        else: 
            print("-75")
        self.points = sum([self.points ,add_points])#this adds all the points in the list everything from self.points 

    def play_again(self):
        answer = input("do you want to play again? Y/N")
        if answer.lower() not in ["Y", "y", "N","n"]:#just incase they answer something silly
            print("please anser Y/N")
        
            return answer

    def do_outputs(self):

        """ outputs game iformation. cards and score.
        
        Args: self (Director) An Instance of Director
           """
        print(f"last card {self.dealer.second_card}")
        print(f"current card {self.dealer.first_card}")
        print(f"current points {self.points}")
        print(f"cards left {sorted(self.dealer.deck)}")

        if len(self.dealer.deck) >= 2 and  self.points > 0:
            
            play_another_round = self.play_again()
            self.keep_playing = play_another_round in {"Y", "y"}
        else:
            self.keep_playing = False

if __name__ =="__main__":
    director = Director()
    director.start_game()

