from game.player import Player

class Dealer:
  """A code template for a person who directs the game. The resposibility of this class of objects is to keep of the score and control the sequence of play.

  Attributes:
    keep_playing (boolean): Whether or not the player wants to keep playing.
    score (number): The total number of points earned.
    player (Player): An instance of the class of objects known as Player.
  """

  def __init__(self):
    """The class constructor.

    Args:
      self (Dealer): an instance of Dealer.
    """
    self.keep_playing = True
    self.score = 0
    self.player = Player()
    self.string_guess = "h"

  def start_game(self):
    """Starts the game loop to control the sequence of play.

    Args:
      self (Dealer): an instance of Dealer.
    """
    while self.keep_playing:
      self.get_inputs()
      self.do_updates()
      self.do_outputs()

  def get_inputs(self):
    """Gets the inputs at the beginning of each round of play. In this case,
    that means drawing a card.

    Args:
      self (Dealer): an instance of Dealer.
    """
    self.player.draw_card()

  def do_updates(self):
    """Updates the important game information for each round of play. In 
    this case, that means updating the score.

    Args:
      self (Dealer): an instance of Dealer.
    """
    points = self.player.get_points()
    self.score += points

  def do_outputs(self):
    """Outputs the important game information for each round of play. In 
    this case, that means the card that were drawed and the score.

    Args:
      self (Dealer): an instance of Dealer.
    """

    """
    choosing = 'yes'
    
    while choosing == 'yes':
      self.guess = input("Higher or lower? [h/l] ")
      if self.guess == "h" or self.guess == "l":
        self.do_updates()
        choosing = 'no'
      else:
        print('Invalid input')
    """

    print(f"\nThe card is: {self.player.oldcard}")
    choosing = 'yes'
    
    while choosing == 'yes':
      self.guess = input("Higher or lower? [h/l] ")
      if self.guess == 'h' or self.guess == 'l':
        self.choice = self.string_guess
        self.player.guess = True if self.choice == "h" else False
        choosing = 'no'
      else:
        print('Invalid input')
    print(f"Next card was: {self.player.newcard}")
    print(f"Your score is: {self.score}")
    if self.player.can_play():
      play_more = 'maybe'
      while play_more == 'maybe':
        choice = input("Keep playing? [y/n] ")
        if choice == 'y':
          self.keep_playing = (choice == "y")
          play_more = 'no'
        elif choice == 'n':
          self.keep_playing = False
          play_more = 'no'
        else:
          print('Invalid input')
    else:
      self.keep_playing = False