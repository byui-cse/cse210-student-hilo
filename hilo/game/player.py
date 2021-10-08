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
    self.newcard = random.randint(1,14)
  def get_points(self):
    """Get points from player guess

    Args:
      self (Player): an instance of Player.
    """
    if(guess == True and (self.newcard - self.oldcard) > 0):
      points += 100
    elif(guess == False and (self.newcard - self.oldcard) < 0):
      points += 100
    else:
      points -= 75
  def can_play(self):
    """Can the player play (points > 0)?

    Args:
      self (Player): an instance of Player.
    """
    return ((points > 0) or self.is_done)