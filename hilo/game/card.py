import random       
    
class Card():

    def __init__(self):
        self.display = random.randint(1,13)
        #self.score = 300
        self.guess_card = random.randint(1,13)
        self.displayed_card = random.randint(1,13)
        self.next_displayed_card = random.randint(1,13)

    

    def guess_high(self):
        return self.guess_card > self.display
    def next_guess_high(self):
        return self.next_displayed_card > self.displayed_card

    def guess_low(self):
        return self.guess_card < self.display
    def next_guess_low(self):
        return self.next_displayed_card < self.displayed_card
        
    """def add_points(self):
        return  100
    def sub_points(self):
        return  75"""
    