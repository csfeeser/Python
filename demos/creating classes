```python
class Hero(): # name of the class we are making
    def __init__(self):
      self.health= 10   # Attributes
      self.strength= 4  # Attributes
      self.magic= 2     # Attributes

# the object "harry" now represents a new Hero!
harry= Hero()

# display the "health" attribute from the "harry" object!
print("Harry Potter's current hitpoints are:", harry.health)
```

The output should be `10`.

```python
class Hero():
    def __init__(self):
      self.health= 10   
      self.strength= 4  
      self.magic= 2 

    def potion(self):    # Method!
      self.health += 5   # drinking a potion adds 5 
                         # to the hero's "health" attribute

harry= Hero()

# display the "health" attribute from the "harry" object!
print("Harry Potter's hitpoints are:", harry.health)

# drink a potion
harry.potion()

# display the "health" attribute again!
print("Harry Potter's hitpoints are:", harry.health)
```

The output should be `10` and then `15`. See how the `health` attribute for `harry` has increased!


```python
class Hero():
    def __init__(self):
      self.health= 10   
      self.strength= 4  
      self.magic= 2 

    def potion(self):
      self.health += 5 
      
      
                                      # the first arg, self, is who is executing the method
    def fireball(self, other_wizard): # the second arg, other_wizard, is the other Hero getting nuked
        other_wizard.health -= self.magic
        # reduce the other_wizard's health attribute integer by the Hero's magic attribute integer
        
harry= Hero()
dumbledore= Hero()

print("Harry Potter's hitpoints are:", harry.health)

print("Dumbledore chucks a fireball at Harry!")
dumbledore.fireball(harry)

print("Harry Potter's hitpoints are now:", harry.health)

print("Harry is rushed to the infirmary to drink a healing potion.")
harry.potion()

print("Harry Potter's hitpoints are now:", harry.health)
```

<!--
```python
class Hero():
    def __init__(self):
        self.magic= 10
        self.hp = 15

class Mage(Hero):
    def __init__(self):
        super(Mage, self).__init__()
        self.magic = 20

hero= Hero()
mage= Mage()

print(hero.magic)
print(hero.hp)
print(mage.magic)
print(mage.hp)
```

>> 10
>> 15
>> 20
>> 15
