"""
The game package contains the classes for playing Hilo.
"""
from game.Player import Player

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        score (number): The total number of points earned.
        thrower (Thrower): An instance of the class of objects known as Thrower.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.keep_playing = True
        self.score = 300
        self.player = Player()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means throwing the dice.

        Args:
            self (Director): An instance of Director.
        """
        self.player.throw_dice()
        
    def update_score(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Director): An instance of Director.
        """
        points = self.player.get_points()
        self.score += points
        
    def do_outputs(self):
        print(f"The card is{self.player.cards[0]}")
        self.player.get_points()
        print(f"Next card was: {self.player.cards[1]}")
        print(f"Your score is: {self.score}")
        if self.score != 0:
            keep_playing = input("Keep playing? [y/n] ")
            if keep_playing == "y":
                return True
            else:
                return False
