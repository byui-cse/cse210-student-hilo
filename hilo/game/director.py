from dealer import Dealer

class Director:

    #pedro
    def __init__(self):
        self.dealer = Dealer()
        self.score = 300
        self.isRunning = True

    #alex
    def play_round(self):
        self.get_cards()
        if  self.blank == True:
            self.score += 100
        else:
            self.score =+ 75
        return self.score

    #chase
    def get_cards(self):
        pass

    #alex
    def run_game(self):
        while (self.isRunnning):
            Keep_playing= input("Keeping playing [y/n] ")
            if Keep_playing.lower() == "n" or self.score == 0:
                self.isRunnning = False
            