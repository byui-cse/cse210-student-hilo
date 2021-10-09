import random

class Player:
  """The player class, who guesses cards and determines points"""
  def __init__(self):
    """The class constructor.

    Args:
      self (Player): an instance of Player.
    """
    self.points = 300
    self.guess = False # False for low, True for high
    self.newcard = 1 # Newly drawn card
    self.oldcard = 1 # Last card (to determine if player's guess was right)
    self.is_done = False # Does the player want to be done?
    pass
  def draw_card(self):
    """Draw a card.

    Args:
      self (Player): an instance of Player.
    """
    self.oldcard = self.newcard # Store old card value
    self.newcard = random.randint(1,13)
  def get_points(self):
    """Get points from player guess

    Args:
      self (Player): an instance of Player.
    """
    self.points = 0
    if(self.guess == True and ((self.newcard - self.oldcard) >= 0)):
      self.points += 100
    elif(self.guess == False and ((self.newcard - self.oldcard) <= 0)):
      self.points += 100
    else:
      self.points -= 75
    return self.points
  def can_play(self):
    """Can the player play (points > 0)?

    Args:
      self (Player): an instance of Player.
    """
    return ((self.points > 0) or self.is_done)