

class Player:
    
    def __init__(self):
        self.points = 300
    # This part is for the player and everything concerning the player should be recorded in this class.
    def show_point(self):
        self.point = self.points
        print(f"Your current points: {self.point}")
        return self.point
        
    def player_guess(self, guess):
        self.prompt = input(guess)
        return self.prompt
    
    # def calculate_points(self):
    #     # TODO
    #     pass