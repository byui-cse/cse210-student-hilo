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
        print('------------------------------------------------------------------------')
        print('\t\tWelcome to the Hilo Card Game!')
        print('\nHow to play:')
        print('\n1. The dealer draws a card.')
        print('\n2. You decided if the next card will be higher or lower than the \ncurrent card. Guess correctly and you win the round. Guess incorrectly\nand you lose the round. \nWin a round and get 100 points. Lose a round and lose 75 points.')
        print('\n3. You start the game with 300 points. If you get to 0 points or\nthe 51 cards run out - the game ends!')
        print('\n\t\tGOOD LUCK & HAVE FUN')
        print('------------------------------------------------------------------------')
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
            current card: calls the method get_card that deals a card from the deck
            keep_playing: while keeping playing is true run the other methods else display final message
            next_card: calls the method get_card that deals a card from the deck
            calculate_points: calculates the points earned or deducted
            show_results: shows the total points
            current_card:  calls the method next_card that deals a card from the deck
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
        """Displays message when game is over and ends the game
        Args:
            self (Director): An instance of Director.
        Attributes:
            score: if score is equal or lower than 0 then display message. Display final score.
        """
        print(f"\nGame Over")
        if self.score <= 0:
            print(f"You lost all of your points.")
        elif len(self.dealer.deck) <=0:
            print(f"Sorry, there are no cards left.")
        print(f"Your final score was: {self.score}")
        exit(0)

    def get_card(self):
        """Gets a card from the dealer.
        Args:
            self (Director): An instance of Director.
            dealer (Dealer): An instance of Dealer.
        Attributes:
            can_throw: determines whether a player can continue with the game
            throw_card: removes card from deck
            final_message: display the message at end of game
        """
        if self.dealer.can_throw(self.score):
            return self.dealer.throw_card()
        else:
            self.final_message()

    def calculate_points(self):
        """Updates the score for each round of play.
        Args:
            self (Director): An instance of Director.
            dealer (Dealer): An instance of Dealer.
        Attributes:
            points: gets the score from the get_points method
            score: adds or deducts points to score
        """
        points = self.dealer.get_points(self.current_card, self.next_card)
        self.score += points

    def show_results(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the score at this point of the game, the next card,
        and asks the player to continue the game.
        Args:
            self (Director): An instance of Director.
            dealer (Dealer): An instance of Dealer.
        Attributes:
            while(Loop): continues game if score is greater than 0
            answer: asks player if they want to continue playing
            answer: continues game if yes and ends game if no
            else: prevents user from entering invalid input
        """
        print(f"Your score so far is: {self.score}")

        print(f"The next card was: {self.next_card[0]}")
        while True:
            print(f"The number of cards left: {len(self.dealer.deck)}")
            if self.score <= 0:
                self.keep_playing = False
                break
            answer = input("Keep playing? [y/n] ")
            if answer.lower() == "y" or answer.lower() == "n":
                if answer.lower() == "n":
                    self.keep_playing = False
                break
            else:
                print("\nPlease, enter a valid answer [y/n]")
