from game.player import Player

class Dealer():
    def __init__(self):
  
        self.keep_playing = True
        self.score = 0
        self.player = Player()

    def start_game(self):

        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()