class Dealer:
    """The person who deals the cards and directs the game. Keeps track of the total score.
    
    Attributes: 
        again (boolean): Whether or not the player wants to keep playing
        score (number): Total points
        guesser (Guesser): An instance of the class of objects known as Guesser.
    """
    

    def __init__(self):
        """The class constructor.

        Args: 
            self (Dealer): an instance of Dealer.
        """
        self.again = True
        self.score = 300
        self.guesser = Guesser()

    def make_deck(self):
        """Creates a deck of 13 cards, starts loop of play

        Args: 
            self (Dealer): an instance of Dealer.
        """
        while self.again:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()


    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case, it means choosing a new card.

        Args:
            self (Dealer): An instance of Dealer.
        """
        self.guesser.choose_card()


    def do_updates(self):
        """Updates the important game information for each round of play. In this case, that means updating the score. 
        
        Args:
            self (dealer): An instance of Dealer.
        """
        points = self.guesser.get_points()
        self.score += points


    def do_outputs(self):
        """Outputs the important game information for each round of play. In this case, that means the card that was picked, the score, and whether it matched the player's guess.
        
        Args:
            self (Dealer): An instance of Dealer. 
        """
        print(f"\nThe next card was: {self.guesser.card}")
        print(f"Your score is: {self.score}")
        if self.guesser.can_guess():
            choice = input("Roll again? (y/n) ")
            self.again = (choice == "y")
        else:
            self.keep_playing = False