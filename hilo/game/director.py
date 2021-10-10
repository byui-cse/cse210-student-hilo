from game.dealer import Dealer

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        score (number): The total number of points earned.
        dealer (Dealer): An instance of the class of objects known as Dealer.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.keep_playing = True
        self.score = 300
        self.dealer = Dealer()
        self.highlow = None

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
        that means drawing a card and asking for a guess.

        Args:
            self (Director): An instance of Director.
        """
        invalid_input = True
        
        self.dealer.draw_card()
        print(f"\nThe current card is: {self.dealer.current_card}")
        while invalid_input:
            self.highlow = input("Higher or lower? [h/l]: ")

            if self.highlow.lower() == "h" or self.highlow.lower() == "l":
                invalid_input = False
            else:
                print('\nInvalid input.\n')

        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Director): An instance of Director.
        """
        points = self.dealer.get_points(self.highlow)
        self.score += points
        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the second card drawn and the score.

        Args:
            self (Director): An instance of Director.
        """

        print(f"\nThe new card is: {self.dealer.new_card}")
        print(f"Your score is: {self.score}")
        if self.score > 0:
            choice = input("\nPlay again? [y/n]: ")
            self.keep_playing = (choice == "y")
        else:
            self.keep_playing = False
            print("\nBetter luck next time!")