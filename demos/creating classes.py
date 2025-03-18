class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 10   
        self.strength = 4  
        self.magic = 2 

    def potion(self):
        self.health += 5
        print(f"🍷 {self.name} drank a potion! Health is now {self.health}.")

    def take_damage(self, damage):
        """Reduces health when taking damage."""
        self.health -= damage
        print(f"💥 {self.name} took {damage} damage! Health is now {self.health}.")
        if self.health <= 0:
            print(f"💀 {self.name} has fallen!")

class Wizard(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.magic = 10  # Wizards have stronger magic

    def fireball(self, target):
        if self.magic >= 3:
            self.magic -= 3
            print(f"🔥 {self.name} casts Fireball at {target.name}!")

            # If target is an instance of Hero (including Wizards), deal damage
            if isinstance(target, Hero):
                target.take_damage(5)  # Fireball does 5 damage
        else:
            print(f"❌ {self.name} does not have enough magic to cast Fireball!")

# Example Usage
gandalf = Wizard("Gandalf")
saruman = Wizard("Saruman")
warrior = Hero("Aragorn")

gandalf.fireball(saruman)  # Saruman takes 5 damage
gandalf.fireball(warrior)  # Warrior takes 5 damage
saruman.potion()  # Saruman drinks a potion
