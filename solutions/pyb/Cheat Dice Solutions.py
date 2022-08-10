class Cheat_Mulligan(Player):
    def cheat(self):
       if sum(self.dice) <= 9:
           self.dice = []
           for i in range(3):
              self.dice.append(random.randint(1,6))

class Cheat_Extra_Die(Player):
    def cheat(self):
        self.dice.append(random.randint(1,6))

class Cheat_Lucky_Die(Player):
    def cheat(self):
        if self.dice[0] < 3:
           self.dice[0]= random.randint(3,6)
            
class Cheat_Saboteur(Player):
  def cheat(self, other_player):
    other_player.dice = [random.randint(1,3) for i in range(3)] 
                        # ^ this is a list comprehension;
                        # a handy way to generate list contents
                        # in one line of code
