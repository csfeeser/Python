# List and Dict Modeling

### Lab Objective

Learning how to work with functions and Python's data structures (lists and dictionaries) is unbelievably important. Why? Well, Network Devices are real world objects that need to be modeled before they can be automated.

A real world example might be to consider YANG (IETF RFC 6020). YANG is a data modeling structure that is used to model interfaces and configuration data of routers and switches. The protocol agnostic YANG model can then be transformed into data structures things like XML, JSON, or even Python data structures. Being able to look at and understand the relationship of data sets is a muscle we need to keep exercising.

In this lab we'll practice using Python data structures to model real-world objects. Our goal will be to practice the following basic skill sets: functions, dictionaries, lists, loops, and conditionals.


### Procedure

0. Imagine two rooms in the real world. Could we model them with a Python data structure?

    ![Two Rooms](https://static.alta3.com/images/python/rpg01.png)

0. Consider the following dictionary, it describes the relationship of our two rooms:

    ```python
    ## A dictionary linking a room to other rooms
    rooms = {
    
                'Hall' : { 
                      'south' : 'Kitchen'
                    },
    
                'Kitchen' : {
                      'north' : 'Hall'
                    }
    
             }
    ```

0. Make a new directory to work in.

    `student@beachhead:~$` `mkdir -p /home/student/pyapi/`

0. Move into `/home/student/pyapi/`

    `student@beachhead:~$` `cd /home/student/pyapi/`
    
    `student@beachhead:~/pyapi$` `vim ~/pyapi/mygame01.py`

0. Create the following script:

    ```python
    #!/usr/bin/python3
    
    # Replace RPG starter project with this code when new instructions are live
    
    def showInstructions():
      #print a main menu and the commands
      print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    ''')
    
    def showStatus():
      #print the player's current status
      print('---------------------------')
      print('You are in the ' + currentRoom)
      #print the current inventory
      print('Inventory : ' + str(inventory))
      #print an item if there is one
      if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
      print("---------------------------")
    
    #an inventory, which is initially empty
    inventory = []
    
    #a dictionary linking a room to other rooms
    rooms = {
    
                'Hall' : { 
                      'south' : 'Kitchen'
                    },
    
                'Kitchen' : {
                      'north' : 'Hall'
                    }
    
             }
    
    #start the player in the Hall
    currentRoom = 'Hall'
    
    showInstructions()
    
    #loop forever
    while True:
    
      showStatus()
    
      #get the player's next 'move'
      #.split() breaks it up into an list array
      #eg typing 'go east' would give the list:
      #['go','east']
      move = ''
      while move == '':  
        move = input('>')
      
      # split allows an items to have a space on them
      # get golden key is returned ["get", "golden key"]          
      move = move.lower().split(" ", 1)
    
      #if they type 'go' first
      if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
          #set the current room to the new room
          currentRoom = rooms[currentRoom][move[1]]
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')
    
      #if they type 'get' first
      if move[0] == 'get' :
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
          #add the item to their inventory
          inventory += [move[1]]
          #display a helpful message
          print(move[1] + ' got!')
          #delete the item from the room
          del rooms[currentRoom]['item']
        #otherwise, if the item isn't there to get
        else:
          #tell them they can't get it
          print('Can\'t get ' + move[1] + '!')
    ```
              
0. So our goal isn't to write an RPG game, but there is the skeleton of one. Currently, our real world object is `rooms`. Review the code until you're certain you understand it. Ask the instructor for some help if anything is unclear.

0. Change permissions on your code so it runs.

    `student@beachhead:~/pyapi$` `chmod u+x ~/pyapi/mygame01.py`

0. Run your code, you should be able to `go south` and `go north`, but that's it. For 'fun', try to `go west`. You'll get a failure message.

0. As we discussed, if you find the `rooms` variable, you'll find that the map is a dictionary of rooms.

0. Let's alter the dictionary so that our map looks like the following:

    ![Three Rooms](https://static.alta3.com/images/python/rpg02.png)
    
0. You need to add a third room called the dining room. You also need to link it to the hall to the west. You also need to add data to the hall so that you can move to the dining room to the east. Edit the room dictionary so it looks like the following.

    ```python
    ## A dictionary linking a room to other rooms
    rooms = {
    
                'Hall' : { 
                      'south' : 'Kitchen',
                      'east'  : 'Dining Room'
                    },
    
                'Kitchen' : {
                      'north' : 'Hall'
                    },
                'Dining Room' : {
                      'west' : 'Hall'
                 }
              }
    ```

0. Try out the new game with your changes. See the instructor if you're having trouble when you `go east` from the hall.

0. Let's try to add an item laying in the hall, that item will be a `key`.

    ```python
    ## A dictionary linking a room to other rooms
    rooms = {
    
                'Hall' : { 
                      'south' : 'Kitchen',
                      'east'  : 'Dining Room',
                      'item'  : 'key'
                    },
    
                'Kitchen' : {
                      'north' : 'Hall'
                    },
                'Dining Room' : {
                      'west' : 'Hall'
                 }
              }
    ```

0. After this change you should be able to use the command `get key` when 'You see a key'.

0. So far, working with data structures seems pretty easy. So, let's add a monster in the kitchen.

    ```python
    ## A dictionary linking a room to other rooms
    rooms = {
    
                'Hall' : { 
                      'south' : 'Kitchen',
                      'east'  : 'Dining Room',
                      'item'  : 'key'
                    },
    
                'Kitchen' : {
                      'north' : 'Hall',
                      'item'  : 'monster',
                    },
                'Dining Room' : {
                      'west' : 'Hall'
                 }
              }
    ```

0. Let's make the game end if a user enters a room with a monster. Add the following code to the very bottom of your script.

    ```python
    ## If a player enters a room with a monster
      if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break
    ```

0. Confirm that the game works 'as designed' so far. For help, here's a map! Be careful, it's dangerous out there!

    ![Three Rooms and Icons](https://static.alta3.com/images/python/rpg03.png)
    
0. If your program is still working, let's wrap up our code. First add a garden south of the dining room- link the dining room to it and add a potion to the dining room.

    ```python
    ## A dictionary linking a room to other rooms
    rooms = {
    
                'Hall' : { 
                      'south' : 'Kitchen',
                      'east'  : 'Dining Room',
                      'item'  : 'key'
                    },
    
                'Kitchen' : {
                      'north' : 'Hall',
                      'item'  : 'monster',
                    },
                'Dining Room' : {
                      'west' : 'Hall',
                      'south': 'Garden',
                      'item' : 'potion'
                   },
                'Garden' : {
                      'north' : 'Dining Room'
                }
             }
    ```

0. Just to be clear, the following is what you have built:

    ![Four Rooms and Icons](https://static.alta3.com/images/python/rpg04.png)

0. Add the following code snippet to the end of the game. This will allow the user to win when they reach the garden with the potion and the key.

    ```python
    ## Define how a player can win
      if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
    ```
            
0. Edit the function `showInstructions()` to include more information on how to win the game, something like, "Get to the Garden with a key and a potion to win! Avoid the monsters! Commands include go *direction* and get *item*.

0. Save your code as `/home/student/pyapi/mygame01.py`

0. Run your code and ensure it works. You might have to run a few times to ensure there are not any bugs.

0. **CODE CUSTOMIZATION 01** - Add *at least* one more room to the game (dictionary). This is much easier if you draw out what you're trying to do before you start doing.

0. If you're tracking your code in GitHub, issue the following commands:
    - `cd ~/pyapi/`
    - `git add *`
    - `git commit -m "your commit message"`
    - `git push origin master`
    - Type in username & password
