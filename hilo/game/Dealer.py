# %%
import random

class Dealer:
    def __init__(self):
        self.first_card = None
        self.second_card = None

    def First_card():
        options = [i for i in range(13)]
        return random.choice(options)


    def Second_card():
        """
        This is where we will create the second random card
        """
        pass

# %%
prac = Dealer.First_card()
print(prac)

# %%
