from game.Guesser import Guesser

class Dealer():

    def __init__(self):

        """ Class constructor.
        
        Args:
            self(Dealer): an instance of Dealer"""
        self.keep_playing = True
        self.score = 300
        self.guesser = Guesser()


    def start_game(self):
        """Starts the game loop to control the game
        
        Args:
            self (Dealer): an instance of Dealer.
        """

        while self.keep_playing:
            self.guesser.random_card()
            print(f'The card is {self.guesser.card}')
            #self.get_inputs()
            self.do_updates()
            self.do_outputs()
            


    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. 
        Args:
            self (Dealer): An instance of Dealer.
            guesser (Guesser): An instance of Guesser.
        """
        self.guesser.get_input_high_Low()

    def do_updates(self):
        """Updates the score.
        Args:
            self (Dealer): An instance of Dealer.
        """
        points = self.guesser.calculate_score()
        self.score += points

    def can_play(self):
        if self.score <= 0:
            return False
        else:
            return True

    def do_outputs(self):
        """the value of the card
        Args:
            self (Dealer): An instance of Dealer.
        """
        print(f"Next card was: {self.guesser.new_card}")
        print(f'Your score is: {self.score}')
        if self.can_play():
            play_again = input("Keep playing? [y/n] ").strip().lower()
            if play_again == "y":
                self.keep_playing = True
            else:
                quit()
    


