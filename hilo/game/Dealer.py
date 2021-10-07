import random
class Dealer:
    def __init__(self):
        self.first_card = None
        self.second_card = None
        self.score = 0

    def First_card(self):
        """
        This is where we will create the first random card
        """
        pass

    def Second_card(self):
        """
        This is where we will create the second random card
        """
        for i in range(1):
         result = random.randint(1,13)
         self.second_card = result

    def get_points(self):
        """
        This is where we will calculate the points. If the second card is
        higher, the user gets 100 points. If the user is wrong, they lose
        75 points.

        Returns:
        If the second card is bigger than the first, return score + 100. If not, 
        return score -75
        """
        if self.second_card > self.first_card:
            return self.score + 100
        else:
            return self.score - 75
    def can_deal(self):
        """
        This function tells the user if they can get dealt another card or not,
        and that is based on the score they get. If the score is equal to or below 
        zero, they can't play again. Other than that, they can continue to play as
        they wish.

        Returns:
        Boolean. True if the score is greater than 0. False if otherwise.
        """
        return (self.score > 0)