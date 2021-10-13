import random 
#this could be totally wrong
# change as needed
class Dealer:

    def __init__(self):
        self.cards = list(range(1,14)) #cards are held in a list from numbers 1-14
        self.first_card = None
        self.second_card = None

    def draw(self): # draws the first card from deck (this one less card than before)
        card = random.choice(self.cards)
        self.cards.remove(card)

        #card = self.cards.pop(self.card.index(indextopop))
        #this takes a card out of the deck and removes it from the list. it is a random card and it is gone once it is drawn.
        #this idea came from reece. 
        print(f"Dealer has drawn first card {card}")
       
        self.second_card = self.first_card #this should make the second card drawn equal to the current card on the table
        self.first_card =card # this makes the card being used the card
        return card
         #this should be all the dealer needs to do. just turn cards and take them out of the list. 


