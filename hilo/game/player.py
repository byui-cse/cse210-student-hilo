import random

class Player:
    
    def __init__(self):
        self.points = 300
        self.card_set = []

    def generate_cards(self):
        # Populates `self.card_set` with 7 new cards
        for i in range(7):
            card = random.randint(1, 13)
            self.card_set.append(card)

        # In case of wanting to cheat, uncomment that below
        # print(self.card_set)
    
    def calculate_points(self):
        # TODO
        pass