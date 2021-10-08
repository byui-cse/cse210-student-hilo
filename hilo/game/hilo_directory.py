from game.card import Card

class Directory():


    def __init__(self):
        self.keep_playing = True
        self.score = 300
        self.card = Card()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        
        while self.keep_playing:
            #self.get_inputs()
            #self.do_updates()
            self.do_outputs()
            self.card = Card()

    def get_inputs(self):
        pass
    """def do_updates(self):
        add_points = self.card.add_points()
        self.score = add_points 
        sub_points = self.card.sub_points()
        self.score = sub_points"""

        

    def do_outputs(self):
        print(f"\nThe card is: {self.card.display}")
        fchoice = input('Higher or lower? [h/l] ')
        next_card = self.card.guess_card
        if fchoice =='h' and self.card.guess_high() or fchoice =='l' and not self.card.guess_high():
            self.score = self.score + 100
            '''elif fchoice =='l' and self.card.guess_low():
            self.score = self.score + 100'''
        else:
            self.score = self.score -75      
        print(f'\nNext card was:  {next_card}')
        print(f"your score is: {self.score}")
        user = input("Keep playing? [y/n] ")
        self.keep_playing = (user.lower() == "y")
        '''if self.keep_playing:
            self.keep_playing = (user == "y")
            print(f"\nThe card is: {self.card.displayed_card}")
            fchoice = input('Higher or lower? [h/l] ')
            next_displayed_card = self.card.next_displayed_card
            if fchoice=='h' and self.card.next_guess_high():
                self.score = self.score + 100
            elif fchoice =='l' and self.card.next_guess_low():
                self.score = self.score + 100
            else:
                self.score = self.score -75  
            print(f'\nNext card was:  {next_displayed_card}')
            print(f"your score is: {self.score}")
        else:
            print("Thanks for playing")
            self.keep_playing = False
            
        if self.score > 0 :
             user = input("Keep playing? [y/n] ")'''
             
            
        # else:
        #     self.score <= 0
        #     self.keep_playing= False