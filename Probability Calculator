import copy
import random

class Hat():
  def __init__(self, **kwargs):
    # initialize the array we want to make
    self.contents = []

    # Loop through keyword arguments
    for ball, amount in kwargs.items():

      # append all the balls to list
      for i in range(amount):
        self.contents.append(ball)

    # We want to make sure we have atleast 1 ball in the hat
    if len(self.contents) < 1:
      print("No balls in hat!")

  def draw(self, value):
    if value > len(self.contents):
      return self.contents

    balls = random.sample(self.contents, k=value)
    for i in balls:
      self.contents.remove(i)
    return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  copy_hat = copy.deepcopy(hat)
  occurances = num_experiments

  for _ in range(num_experiments):
    balls = copy_hat.draw(num_balls_drawn)
    for key, value in expected_balls.items():
      if balls.count(key) < value:
        occurances -= 1
        break
    copy_hat = copy.deepcopy(hat)
    
  return occurances / num_experiments
