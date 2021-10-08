import random

class Guesser:
    def __init__(self):
        self.card = 0
        self.new_card = 0

    def random_card(self):
        self.card = random.randint(1, 13)
        self.new_card = random.randint(1, 13)


    def get_input_high_Low(self):
        guess = input('Will the next card be higher or lower? [h/l]')
        return guess

    def calculate_score(self):
        answer = self.get_input_high_Low()
        if answer == 'h':
            if self.new_card > self.card:
                return 100
            else:
                return(-75)
        elif answer == 'l':
            if self.new_card < self.card:
                return 100
            else:
                return(-75)
        else:
            print('invalid value')
