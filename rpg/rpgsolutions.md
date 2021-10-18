### In class today we had a list of challenges to attempt with our RPG!

• Add additional rooms.

• Find a way to add a description of each room that describes every direction you can go.

• Find a way to have multiple items inside the same room.

• Find a way to add descriptions to items that display when the item is picked up.

• Create alternate win/loss scenarios. 

• Make a trapdoor. Once you go through it you can't go back that way!

• Make a "teleport to" command that will put you in any room!

• Find a way to survive your encounter with the monster!

### Below is Chad's solutions to these challenges (and as always, Chad's solutions are not necessarily the best!)

```
#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live
import subprocess

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
  teleport [room]
  q (quit)
''')

def clear():
    subprocess.call('clear')

clear()

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom] and len(rooms[currentRoom]['item']) != 0:
    print('You see a ' + str(rooms[currentRoom]['item']))
  directions= []
  for x in rooms[currentRoom].keys():
      if x != "item":
          directions.append(x)
  print("You can go", ", ".join(directions)) 

  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
descriptions= {"key":"This is a gleaming brass key.", 
               "sword":"This rusty sword has seen better days.", 
               "potion":"The potion glows with magic!",
               "cookie":"Yum! Chocolate chip!", 
              }

rooms = {

            'Hall' : { 
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : ['key','sword'],
                  'down'  : 'Dungeon'
                },
            'Dungeon' : {
                  'east' : 'Dining Room',
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : ['monster'],
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : ['potion','cookie']
               },
            'Garden' : {
                  'north' : 'Dining Room'
            }
         }

#start the player in the Hall
currentRoom = 'Hall'


move= ""

showInstructions()

#loop forever
while True and move != ["q"]:
  showStatus()
  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')

  clear()
  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if move[0].lower() == 'clear':
      #clear()

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  if move[0] == "teleport":
      if move[1].capitalize() in rooms:
          currentRoom= move[1].capitalize()
      else:
          print("You can't teleport there!")

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(len(descriptions[move[1]])*"*")
      print(descriptions[move[1]])
      print(len(descriptions[move[1]])*"*")
      #delete the item from the room
      rooms[currentRoom]['item'].remove(move[1])
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break
  
  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and "sword" in inventory and "cookie" not in inventory:
    print("You swing your rusty sword!... and it breaks in half. The monster gobbles you up anyway. GAME OVER!")
    break

  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and "sword" in inventory and "cookie" in inventory:
    print("You swing your rusty sword!... and it breaks in half. The monster is about to eat you when it sees the cookie in your pocket. It eats the cookie instead and runs away!")
    del rooms["Kitchen"]["item"]

  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and "cookie" in inventory:
    print("The monster is about to eat you when it sees the cookie in your pocket. It eats the cookie instead and runs away!")
    del rooms["Kitchen"]["item"]

  ## If a player enters a room with a monster
  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break
```
