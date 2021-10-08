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
            dealer(Dealer): an instance of Dealer.
        """
        print('---------------------------------------------------------------------------')
        print('Welcome to the Hilo Card Game.')
        print('How to play:')
        print('1. The dealer draws a card.')
        print('2. You decided if the next card will be higher or lower than the current')
        print('card. Guess correctly and you win the round. Guess incorrectly and you')
        print('lose the round.')
        print('Win a round and get 100 points. Lose a round and lose 75 points.')
        print('3. You start the game with 300 points. If you get to 0 points or')
        print('the 51 cards run out - the game ends!')
        print('GOOD LUCK & HAVE FUN')
        print('---------------------------------------------------------------------------')

        self.keep_playing = True
        self.dealer = Dealer()
        self.score = self.dealer.initial_points
        
    
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
            dealer(Dealer): an instance of Dealer
        Attributes:
            shuffle deck: shuffles the deck of cards
            current card: calls the function get_card() that deals a card from the deck
            keep_playing: 
        """
        self.dealer.shuffle_deck()
        self.current_card = self.get_card()
        while self.keep_playing:
            self.next_card = self.get_card()
            self.calculate_points()
            self.show_results()
            self.current_card = self.next_card
        
        self.final_message()
    
    
    def final_message(self):
        """
        """
        print(f"\nGame Over")
        if self.score <= 0:
            print(f"You lost all of your points.")
        print(f"Your final score was: {self.score}")
        exit(0)


    def get_card(self):
        """Gets a card from the dealer.
        Args:
            self (Director): An instance of Director.
            dealer (Dealer): An instance of Dealer.
        """
        if self.dealer.can_throw(self.score):
            return self.dealer.throw_card()
        else:
            self.final_message()
        
    
    def calculate_points(self):
        """Updates the score for each round of play.
        Args:
            self (Director): An instance of Director.
        """
        points = self.dealer.get_points(self.current_card, self.next_card)
        self.score += points

        
    def show_results(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the score at this point of the game, the next card,
        and asks the player to continue the game.
        Args:
            self (Director): An instance of Director.
        """
        print(f"Your score so far is: {self.score}")

        print(f"The next card was: {self.next_card[0]}")
        while True:
            print(f"The number of cards left: {len(self.dealer.deck)}")
            if self.score <= 0:
                self.keep_playing =  False
                break
            answer = input("Keep playing? [y/n] ")
            if answer.lower() == "y" or answer.lower() == "n":
                if answer.lower() == "n":
                    self.keep_playing = False
                break
            else:
                print("\nPlease, enter a valid answer [y/n]")