# RPG CHALLENGE

![Image description](https://github.com/csfeeser/images/blob/master/pythondragon.png?raw=true)

[CLICK HERE FOR A VIDEO LECTURE ON THIS CODE!](https://labs.alta3.com/courses/api/vid/7-list-and-dict-modeling.mp4)

As a conclusion to our week of Python Fundamentals, we're putting the FUN in FUNdamen- ugh.

Your challenge is to (either solo or part of a group) develop additional features into the RPG script that Chad demonstrated to you. 

Some suggestions for implementations are provided below- you're also encouraged to come up with your own ideas!
<details>
<summary>Add additional rooms.</summary>
  
   ```
   Copy/paste the dictionary for "Hall"; change the values. Add directions to point to your new room(s).
  
   'Bathroom' : {
                  'south' : 'Hall',
                  'item'  : 'deodorant'
                }
   ```
  
</details>
<details>
<summary>Count how many "moves" the player has made.</summary>
  
   ```
   Near the beginning of the code, create a counter.
   
   counter= 0
  
   At the beginning of the while loop, have counter increase by one.
  
   counter += 1
  
   Inside the def showStatus() function, print this value so that it displays after every move.
  
   print("Moves made:", counter)
   ```
  
</details>
<details>
<summary>Find a way to add a description of each room that describes every direction you can go.</summary>
  
   ```
   Add a new key/value to your room's dictionary. Maybe something like this:
  
   'Bathroom' : {
                  'south' : 'Hall',
                  'item'  : 'deodorant',
                  'desc'  : 'You are in a small bathroom. No soap, yuck."
                }
  
   Inside the def showStatus() function, print this value so that it displays after every move.
  
   print(rooms[currentRoom]["desc"])
   ```
  
</details>
<details>
<summary>Find a way to have multiple items inside the same room.</summary>
  
   ```
   You would have to have the value of "item" be a list!
  
   'Bathroom' : {
                  'south' : 'Hall',
                  'item'  : ['deodorant', 'toilet paper', 'tooth brush']
                }
   
   You will also have to edit how items are removed from the room. I suggest the
   .remove() method, which removes an element from a list by name instead of index number.
  
   rooms[currentRoom]['item'].remove(move[1])
   ```
  
</details>
</details>
<details>
<summary>Find a way to add descriptions to items that display when the item is picked up.</summary>
  
   ```
   Ideally this would be done in the rooms dictionary.
  
   'Bathroom' : {
                  'south' : 'Hall',
                  'item'  : {'name'  : 'deodorant',
                             'desc'  : 'Old Spice. A classic.'}
                }
   
   This would display the item's description:
   print(rooms[currentRoom]['item']['desc']  
   ```
  
</details>
</details>
<details>
<summary>Make a "teleport to" command that will put you in any room!</summary>
  
   ```
   if move[0] == 'teleport' :
         if move[1].capitalize() in rooms:
              currentRoom= move[1].capitalize()
   ```
  
</details>
<details>
<summary>Make a trapdoor. Once you go through it you can't go back that way!</summary>
  
   ```
   A trapdoor would mean that once you go from one room to the next, you can't come back that way.
   You can go "down" in the Bathroom, but you can't go back "up" in the Pit.
  
   'Bathroom' : {
                  'south' : 'Hall',
                  'down'  : 'Pit'
                }
   'Pit' : {
                  'east' : 'Basement',
                }
   ```
  
</details>

- Create alternate win/loss scenarios.
- Add more verbs! What else can your player do besides "get" and "go"?
- Find a way to survive your encounter with the monster!
- **Labyrinth**- use the `rooms` list/dict model to create a maze! Life-threatening traps are always a plus.
- **Combat**- create a function that, when triggered, enters combat mode. Player/monster health & damage must be calculated and win/lose conditions created!
- **Riddles**- create a function that, when triggered, asks the player a series of riddles that may return some reward or punishment upon failure!
- **Crushing Walls**- create a function that, when triggered, puts our hero in a room with gradually closing walls. Implement a timer that will run out unless they find the escape solution!
- **All-knowing Sphinx**- create a function that, when triggered, a cat statue gives you a random cat fact from the cat facts API!
- **Puzzle**- create a function that, when triggered, engages the player in some manner of diabolical puzzle where failure is... unhealthy!
- **Class**- build a Player class object to internalize (and therefore replace) existing procedural player characteristics: inventory, health, spells, etc. BUT ALSO implement player stats that `def __init__(self)` upon creation. Create a method that triggers a level-up message where users can allocate points to  strength, intelligence, and speed.

### Requirements:

- Implement at least 3 **significant** changes to the code. They can be taken from the suggestions above or you can come up with your own!
- Comment your code well! Others are going to be reading your code.
- Follow PEP8 standards where appropriate. Use """multi-line doc strings""" at the top of your module and all functions to announce their purpose. Cite the names of who wrote that code. No "spaghetti code."
