from game.dealer import Player
import random

class Dealer:
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.keep_playing = True
        self.score = 300
        self.player = Player()
        self.card1 = 0
        self.card2 = 0
        

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.cardsobtain()
            print(f"The first card is: {self.card_name(self.card1)}")
            self.compare_guess()
            self.display_points()
            self.can_play_again()
    
    
    def cardsobtain(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means flipping the first two cards.

        Args:
            self (Director): An instance of Director.
        """
        self.card1 = random.randint(1, 13)
        self.card2 = random.randint(1, 13)
        while self.card1 == self.card2:
            self.card2 = random.randint(1, 13)
   
    def compare_guess(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Director): An instance of Director.
        """
        print()
        self.player.user_guess()
        print(f"Next card was: {self.card_name(self.card2)}")
        if (self.card1 > self.card2 and self.player.guess == "l") or (self.card1 < self.card2 and self.player.guess == "h"):
            self.score += 100
            print("You guessed wisely and earned 100 points")
        else:
            self.score += -75
            print("You guessed poorly and lost 75 points")

    def card_name(self, card):

        """
        Converts 11,12,13,1 to J,Q,K,A
        """
        if (card < 11 and card != 1):
            return(str(card))
        elif(card == 1):
            return("A")
        elif(card == 11):
            return("J")
        elif(card == 12):
            return("Q")
        elif(card == 13):
            return("K")
                
            
    def display_points(self):
        print(f"Score: {self.score}")
        print ()

    def can_play_again(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the final score of the game
        Args:
            self (Director): An instance of Director.
        """
        if self.score <= 0:
            self.keep_playing = False
            print(f"Game over you lose and are bad at this game!")

        else:
            self.player.continuation()
        if self.player.again == "n":
            print(f"Thanks for playing! Your final score is: {self.score}")
            self.keep_playing = False
 