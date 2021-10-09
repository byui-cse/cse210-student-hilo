from game.Table import table 

class dealer:
    
    def __init__(self):
        """The class constructor.
     
        Args:
        self (Director): an instance of Director.
        """
        self.keep_playing = True
        self.score = 300
        self.table = table()
        self.card1 = 0
        self.card2 = 0
        

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            if self.keep_playing:
                self.do_updates()
                self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means Dealing the card.

        Args:
        self (Director): An instance of Director.
        """
        if self.table.first_draw == False:
            draw_again = input('Draw again? y/n')
            self.keep_playing = (draw_again == "y")
            if self.keep_playing:
                print('You Died')

    def get_guess(self):
        guess = input("Higher or Lower? h/l ")
        if self.card1 < self.card2 and guess == 'h':
            self.score += 100
        elif self.card1 > self.card2 and guess == 'l':
            self.score +=100
        else:
            self.score -= 75



    def do_updates(self):
        self.card1 = table.draw_card(self)
        self.card2 = table.draw_card(self)
        print(f'The card is: {self.card1}')
        self.get_guess()
        if self.score <= 0:
            self.score = 0 
            self.keep_playing = False


    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the cards that were dealt and the score.

        Args:
        self (Director): An instance of Director.
        """
        print(f"The next card was: {self.card2}")
        print(f"Your score is: {self.score}")
        if self.keep_playing == False:
            print('You Died')
        
            
