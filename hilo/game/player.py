import random

class Player:
    
    def __init__(self):
        self.points = 300
        self.card_set = []

    def generate_cards(self):
        # Populates `self.card_set` with 7 new cards
        for i in range(7):
            card = random.randint(10, 13)
            self.card_set.append(card)

        # In case of wanting to cheat, uncomment that below
        print(self.card_set)
    
    def calculate_points(self, choice):

        # Add points
        # Gives freeby points if the next card is the same as the previous
        if (choice == "h" and self.card_set[1] >= self.card_set[0]) or (choice == "l" and self.card_set[1] <= self.card_set[0]):
            self.points += 100

        # Subtract points
        elif choice == "l" or choice == "h":
            self.points -= 75

        # In case of a typo
        else:
            print(f"Sorry, '{choice}' is not an option. GAME OVER!")
            quit()