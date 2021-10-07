from game.dealer import Dealer

class Director:
    '''
    The resonsibility of this class is to keep track of the score and
    control the squence of play.

    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        score (number): The total number of points earned ot lost
        dealer (Dealer): An instance of the objects known as Blank
    '''

    def __init__(self):
        '''
        The class constructor.

        Args:
            self (Director): an instance of the Director.
        '''

        self.keep_playing = True
        self.score = 300
        self.dealer = Dealer()