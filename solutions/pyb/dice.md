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

class Cheat_Switcher(Player):
  def cheat(self, other_player: Player):
    other_player.dice = [randint(1,3) for i in range(3)]

p1 = Player()
p2 = Cheat_Switcher()

p1.roll()
p2.roll()

print("Other player's original dice:")
print(p1.get_dice())
print(sum(p1.get_dice()))

p2.cheat(p1)

print("\nOther player's SWITCHED dice:")
print(p1.get_dice())
print(sum(p1.get_dice()))
```
