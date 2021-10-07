from random import randint

class Dealer():
    def __init__(self):
        self.card_active = 0
        self.points = 0
        self.choice = ""
        self.card_next = randint(1, 13)

    def get_user_choice(self):
        self.choice = input("Higher or lower? [h or l] ")  


    def get_points(self):
        """
        Keeps track of the number of points.
        """
        self.points = 0
        print(self.card_active)
        print(self.card_next)
        if self.card_active > self.card_next and self.choice.lower() == "l":
            self.points -= 75
        elif self.card_active < self.card_next and self.choice.lower() == "h":
            self.points -= 75
        elif self.card_active < self.card_next and self.choice.lower() == "l":
            self.points += 100
        elif self.card_active > self.card_next and self.choice.lower() == "l":
            self.points += 100
        else:
            self.points += 0
        return self.points

    def get_card(self):
        """
        Generates a random number between 1 and 13 for the card number.
        """
        self.card_active = self.card_next
        self.card_next = randint(1,13)
