from game.Card import Card

class Director:

    def __init__(self):
        self.card = Card()
        self.another+""
        # self.Q = self.question(self)
        self.chioce = ""
        self.score = 0
        self.keep_playing = True
        # self.random_card1 = self.card_draw(self)
        # self.random_card2 = self.card_draw(self)
    
    def start_playing(self):
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
    
    def get_inputs(self):
        self.card.card_number1

    def do_updates(self):
        if self.choice == "low":
            self.points += self.card.low(self)

        elif self.choice == "high":
            self.points += self.card.high(self)

    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the dice that were rolled and the score.
        Args:
            self (Director): An instance of Director.
        """
        print(f"\nYour new card is: {self.card.card_number2}")
        print(f"Your score is: {self.score}")
        self.another = input("would you like another card (y/n):")
        if self.another == "y":
            self.choice = input("High or Low? [high/low]:")
            self.do_updates
            #self.keep_playing = (self.choice == "y")
        else:
            self.keep_playing = False
    


    # def question(self):
    #     self.choice = input("high or low:")
    #     self.answer


    # def card_draw(self):
    #     return self.card.card(self)

    # def in_or_out(self):
    #     choice = input("keep playing?")

