import random
class Player:
    def __init__(self):
        self.guess = None
        self.again = 0

    def user_guess(self):
        self.guess = input("Higher or Lower? [H/L]: ").lower()

    def continuation(self):
        self.again = input("Another round? [Y/N]: ").lower()



