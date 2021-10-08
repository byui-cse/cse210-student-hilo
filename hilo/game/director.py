from game.player import Player
from game.dealer import Dealer
from game.style import *


class Director:
    """
    The Director class handles the game play for High Low.
    """
    def __init__(self):
        """Initializes the Dealer, Player, keep_playing bool, points, and round_number"""
        self.dealer = Dealer()
        self.player = Player()
        self.keep_playing = True
        self.points = 300
        self.round_number = 0

    def start_game(self):
        """Starts the game loop to control the sequence of play.

        Args:
            self (Director): an instance of Director.
        """
        print_green("Welcome to HIGH LOW!")
        # Outputs instructions.
        print_yellow("""
Instructions:
    You start with 300 points. 
    The dealer will deal a card & you must choose if the next card will be higher or lower.
    If you guess incorrectly, you will lose 75 points.
    If you guess correctly, you will gain 100 points. 
    If you lose all your points, you lose.
        """)
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
        # Game ending output
        print_green("Thank you for playing!")
        print_yellow(f"Your points were {self.points}")
        if self.points <= 0:
            print_red("You lose.")

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case, that means getting drawing cards and
        getting the user's guess.
        Args:
            self (Director): An instance of Director.
        """
        self.dealer.draw_card()
        self.player.get_high_low_guess()
        self.dealer.draw_card()

    def do_updates(self):
        """Updates the important game information for each round of play. In
        this case, that means updating the score.
        Args:
            self (Director): An instance of Director.
        """
        round_points = self.player.calculate_points(self.dealer.current_card, self.dealer.last_card)
        if round_points > 0:
            print_green("\t+100")
        else:
            print_red("\t-75")
        self.points = sum([self.points, round_points])

    def get_play_another_round(self):
        """Gets validated user input for if they want to play another round.
        Args:
            self (Director): An instance of Director.
        """
        answer = input("Play Another Round? [Y/N]: ")
        if answer not in ["y", "Y", "n", "N"]:
            print_red("Please Choose Y/N!")
            print_reset()
            return self.get_play_another_round()
        return answer

    def do_outputs(self):
        """Outputs the important game information for each round of play. In
        this case, that means the card stats and the score.
        Args:
            self (Director): An instance of Director.
        """
        print_yellow(f"\tLast Card: {self.dealer.last_card}")
        print_yellow(f"\tCurrent Card: {self.dealer.current_card}")
        print_yellow(f"\tRemaining Cards: {sorted(self.dealer.deck)}")
        
        if len(self.dealer.deck) >= 2 and self.points > 0:
            print_reset()
            play_another_round = self.get_play_another_round()
            self.keep_playing = play_another_round in ["Y", "y"]
        else:
            self.keep_playing = False


if __name__ == '__main__':
    director = Director()
    director.start_game()
