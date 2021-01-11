Interested in creating a method that affects another class object? Here is a solution!

```
from random import randint
class Player:
  def __init__(self):
    self.dice = []
  def roll(self):
    self.dice = [] # clears current dice
    for i in range(3):
      self.dice.append(randint(1,6))
  def get_dice(self):
    return self.dice
class Cheat_Swapper(Player):
  def cheat(self):
    self.dice[-1] = 6
class Cheat_Loaded_Dice(Player):
  def cheat(self):
    i = 0
    while i < len(self.dice):
      if self.dice[i] < 6:
        self.dice[i] += 1
      i += 1
  def switcharoo(self, other_player: Player):
    other_player.dice = [randint(1,3) for i in range(3)]
p1 = Player()
p2 = Cheat_Loaded_Dice()
p1.roll()
p2.roll()
print(p1.dice)
p2.switcharoo(p1)
print(p1.dice)
```
