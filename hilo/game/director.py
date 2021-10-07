from game.dealer import Dealer

class Director:

    def __init__(self) -> None:
        self.score = 300
        self.keep_playing = True
        self.dealer = Dealer()

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
        that means flipping the next card.

        Args:
            self (Director): An instance of Director.
        """
        self.dealer.flip_card()

    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Director): An instance of Director.
        """
        points = self.dealer.score_round()
        self.score += points


    def can_flip():
        pass

    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means a card was flipped and show the card and current score.

        Args:
            self (Director): An instance of Director.
        """
        
        print(f"\nThe card is: {self.dealer.card}")
        print(f"Your score is: {self.score}")

        if self.thrower.can_throw():
            choice = input("Roll again? [y/n] ")
            self.keep_playing = (choice == "y")
        else:
            if self.score == 0:
                print("Better Luck Next Time!")
            self.keep_playing = False