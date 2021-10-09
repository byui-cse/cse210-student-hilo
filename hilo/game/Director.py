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
        self.number_of_plays = 0

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.update_score()
            self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means throwing the dice.

        Args:
            self (Director): An instance of Director.
        """
        # Random number between 1-13 is generated and returned. 
        self.player.get_card()
        print(f'The current card is: {self.player.cards[0]}')

        
    def update_score(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Director): An instance of Director.
        """
        # Gets input from user ('h'/'l')
        guess = self.player.get_guess()
        assert type(guess) == type('string')

        # If this is the first turn, a second card needs to be drawed.
        # If it is not, a second card does not need to be drawed as there 
        # is already one in the list.
        if self.number_of_plays == 0:
            assert self.number_of_plays == 0 
            self.player.get_card()  

        # Points from 1 turn are saved in the points variable which are then 
        # added/substracted to the total score.
        points = self.player.get_points(guess)
        assert type(points) == type(1)
        
        self.score += points
        
    def do_outputs(self):

        print(f"The new card is: {self.player.cards[1]}")
 
        print(f"Your score is: {self.score}")

        # Based on game rules and user input, game loop will continue or get
        # turned off. 
        if self.score != 0:
            keep_playing = input("Keep playing? [y/n] ")
            if keep_playing == "y":
                self.player.clear_list()
                self.keep_playing = True
                print ("")
            else:
                print ("")
                print (f"Your final score was: {self.score}")
                if self.score > 300:
                    print ("Great job, see you next time!")
                elif self.score <= 300:
                    print ("Better luck next time...")
                self.keep_playing = False

        else:
            print ("")
            print (f"Your final score was: {self.score}")
            if self.score > 300:
                print ("Great job, see you next time!")
            elif self.score <= 300:
                print ("Better luck next time...")
            self.keep_playing = False
