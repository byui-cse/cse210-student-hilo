import random

class Player:
    
    def __init__(self):
        self.points = 300
        self.card_set = []

    def generate_cards(self):
        
        # Makes a list form 1 to 13 to choose from
        card_range = list(range(1, 14))
        
        for i in range(7):
            # Checks if the `self.card_set` to avoid filtering it
            try:
                n = self.card_set[-1]
            except IndexError:
                n = 0

            # Filters the last card or the array to avoid having the same number twice in a row
            filtered_card_range = list(filter(lambda exc: exc != n, card_range))

            # Populates `self.card_set` with 7 new cards
            card = random.choice(filtered_card_range)
            self.card_set.append(card)

        # In case of wanting to cheat, uncomment that below
        # print(self.card_set)
    
    def calculate_points(self, choice):

        # Add points
        if (choice == "h" and self.card_set[1] >= self.card_set[0]) or (choice == "l" and self.card_set[1] <= self.card_set[0]):
            self.points += 100

        # Subtract points
        elif choice == "l" or choice == "h":
            self.points -= 75

        # In case of a typo
        else:
            print(f"Sorry, '{choice}' is not an option. GAME OVER!")
            quit()