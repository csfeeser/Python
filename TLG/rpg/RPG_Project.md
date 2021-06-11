# RPG CHALLENGE

![Image description](https://github.com/csfeeser/images/blob/master/pythondragon.png?raw=true)

As a conclusion to our week of Python Fundamentals, we're putting the FUN in FUNdamen- ugh.

Your challenge is to (either solo or part of a group) develop additional features into the RPG script that Chad demonstrated to you. Ideally, ALL the class's implementations will be included in one script!
Some suggestions for implementations are provided below- you're also encouraged to come up with your own ideas!
- Add additional rooms.
- Find a way to add a description of each room that describes every direction you can go.
- Find a way to have multiple items inside the same room.
- Find a way to add descriptions to items that display when the item is picked up.
- Create alternate win/loss scenarios.
- Make a trapdoor. Once you go through it you can't go back that way!
- Make a "teleport to" command that will put you in any room!
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
