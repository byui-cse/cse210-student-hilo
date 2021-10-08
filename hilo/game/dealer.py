from game.table import Table
#Im adapting most of this from the dice game.
#this could be totally wrong
# change as needed
class Dealer:

    def __init__(self):
        self.keep_playing = True
        self.score = 300
        self.table = Table

    def start_game(self):
        while self.keep_playing :
            self.get_inputs()
            self.do_update()
            self.do_outputs()

    def do_updates(self):
        """ Updates game information each round. 
        score 
        
        args: self (Dealer): an instance of Dealer 
        I dont know what that means but it is in  the last game so I put it here. 
        """
        points = self.table.get_points()
        self.score =+ points

    def get_inputs(self):
        """ gets the inputs from the begining of each round of play. 
        we need to have a turn of the card. 
        we also need to have a guess high or low.
        then the dealer has to lay another card to complete the round

         this has an  Args: self (Dealer): space again like the last one . 
         in the last game it was Args: self(Director) if someone knows what this means i need to know. """

        self.table.lay_card()# names are negotiable

    def get_outputs(self):

        """ These are the outputs from each round. 
        What was the card turned
        what is your current score
        is the game over.
        
        Arge: self(Dealer) An instance of Dealer """
        print( f" Your card is {self.table.card}")
        print(f" Your current score is {self.score} ")
        if self.table.lay_card():
            choice = input(" Do you coose High or Low?  H/L ")
            self.keep_playing = (choice ==  # what ever the card and score end up being. )
        else: self.keep_playing += False

#this is an outline. I would like input and help putting it all together. this dealer.py is how we construct table.py 
 

