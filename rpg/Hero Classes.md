Hi guys!

Here is the code that we wrote together in class today to get more examples of how CLASS works in Python.

    ```python
    import random

    class Hero():

        def read_inv(self):
            return self.inv

        def add_inv(self, item):
            self.inv.append(item)

        def choose_name(self, choice):
            self.name= choice

        def return_name(self):
            return self.name

        def hurt(self, dam):
            self.hp -= dam
            print(f"Ouch! The hero was hurt and now has {self.hp} hit points remaining!")

        def powerkick(self):
            if self.mana >= 3:
                damage= random.randint(10,18) + self.strength
                print(f"{self.name} lashes out with a powerful KICK!")
                self.mana -= 3
                return damage
            else:
                print("You don't have enough mana to use this move!")
                return 0

        def equip(self, item):
            if item in self.inv:
                armor= {"helmet": 5,"shield": 5,"breastplate": 10}
                if item in armor.keys():
                    self.hp += armor[item]
            else:
                print("You don't have " + item)

    class Rogue(Hero):

        def __init__(self):
            self.strength= 1
            self.dexterity= 10
            self.intelligence= 5
            self.hp= 7
            self.mana= 12
            self.name= "Sneakly McSneakerson"
            self.inv= ["lockpick","dagger"]

    class Warrior(Hero):

        def __init__(self):
            self.strength= 10
            self.dexterity= 5
            self.intelligence= 1
            self.hp= 15
            self.mana= 6
            self.name= "H.P. McHack'n'slash"
            self.inv= ["sword","shield"]
    ```

Here was the first script we wrote to test the methods. **WARNING**- this script won't work as written because we moved the stats down to the Warrior and Rogue subclasses.

    ```python
    import heroclass
    import random

    # define an object (player) as the Hero() class
    player= heroclass.Hero()

    # add an item
    player.add_inv("bacon")
    player.add_inv("pokedex")
    player.add_inv("potion")

    # display inventory
    print(player.read_inv())

    # display the default name
    print(player.return_name())

    # choose a different name
    name= input("Choose a different name: ")
    player.choose_name(name)

    # display the changed name
    print(player.return_name())

    print("COMBAT BEGINS")
    ogre_hp= 20

    ogre_hp -= player.powerkick()

    print(f"The ogre now has {ogre_hp} hit points!")

    if ogre_hp <= 0:
        print("That ogre ded!")

    else:
        print("The ogre is still kicking!")
        player.hurt(random.randint(5,15))
    ```

And here is the test script we wrote for the final version of the classes.

    ```python
    import heroclass
    import random

    # define an object (player) as the Hero() class
    warrior= heroclass.Warrior()

    rogue= heroclass.Rogue()

    print(f"{rogue.return_name()} has in their inventory: {rogue.read_inv()}")

    print(f"{warrior.return_name()} has in their inventory: {warrior.read_inv()}")

    warrior.equip("shield")

    warrior.hurt(0)
    ```

