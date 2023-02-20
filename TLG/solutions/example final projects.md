## Final Project Examples

These are projects submitted by prior TLG students. Take a look through them to get a sense of the kinds of code most folks turn in!

<details>
<summary>Magic 8-Ball</summary>
  
```python
"""Magic 8 Ball with ASCII text header"""

#loads modules for code to function
import http.client #loads HTTP modules for API pull
import sys
import json

 #credit to figlet and termcolor documentation
from termcolor import cprint 
from pyfiglet import figlet_format

#ASCII text generator
cprint(figlet_format('MAGIC 8 BALL!', font='starwars'),
       'yellow', attrs=['bold'])

#connection to API for random answers
conn = http.client.HTTPSConnection("magic-8-ball1.p.rapidapi.com") #credit to magic 8 ball documentation

#API key to access the API
headers = {'X-RapidAPI-Key': "7bf30cb820msh711ff8544fffe8fp1e7edcjsn5a63168314fa",'X-RapidAPI-Host': "magic-8-ball1.p.rapidapi.com"}


#user interface script
def main():
    
    print('')
    print('Hello, I am the Magic 8 Ball, What is your name?')
    name = input()
    print('hello ' + name)

    print('Ask me a question.')
    input()
    print("Hmmm..... Thinking")

    #getting response from API site to question

    conn.request("GET", "/my_answer/?question=I%20will%20succeed%20%3F", headers=headers)

    res = conn.getresponse()
    data = res.read()

    answer = (data.decode("utf-8"))
    answer = json.loads(answer) #credit to Chad
    
   
    print (answer["answer"])

main()
```
  
</details>

- script asks for your name
- makes an API call to retrieve a "magic 8 ball" answer
- prints it out colorfully and with ASCII art  

<details>
<summary>Mortgage/Car Payment Calculator</summary>
  
```python
#!/usr/bin/env python3
#python project

def financial_calculator():
    """ Calculate your Car or Mortgage payment"""
    try:
        price = float(input(" What is the total price of your car or home? Please enter the numeric value:\n>"))
        downpayment = float(input( "How much money you would like to put as downpayment? Please enter the numeric value:\n>"))
        loan_amount = price - downpayment

        loanterm = int(input("What is the length of the loan in years? Please enter the numeric value:\n>"))
        #Claculate the loan length in months
        loanterm_month = loanterm * 12
        
        #print(monthly_payment)
        interestrate = float(input("What is the yearly interest rest?\n>"))
        monthly_rate = interestrate / 12 /100
        #    print(monthly_rate)     
        #Calculate the monthly payment
        monthly_payment = (monthly_rate * loan_amount * pow((1 + monthly_rate), loanterm_month))  / (pow((1 + monthly_rate), loanterm_month) - 1)
        monthly_payment = "{:.2f}".format(monthly_payment)
    #    print(f'Your monthly payment is: {monthly_payment}') 
        return  f'Your monthly payment is: {monthly_payment}'
    #except OverflowError:
        #return "The error occurred because xyz"
    except ValueError:
        return "That was not a number. Please put a number."
    except:
        return "There was an error!"

def another_payment():
    wrong_input = 0    
    while True:
        another_pay = input("Do you have another payment to calculate? Answer Y/N")
        another_pay = another_pay.strip().lower()
        if another_pay == "y":
            print(financial_calculator()) 
        elif another_pay == 'n':
            print ("Thank you. Have a nice day.")
            break
        else:
            wrong_input += 1
            if wrong_input > 3:
                print("Wrong input entered too many times. Please contact customer service")
                break
            print("That wasn't one of the options!")

def main():
    print(financial_calculator())
    #print("Your monthly payment is...")
    #print("There was an error!")
    another_payment()

if __name__ == "__main__":
    main()
```
  
</details>

- script asks for financial input
- does calculations, returns payment amount
- prompts user if they'd like to calculate another amount 

<details>
<summary>Date Night Idea Generator</summary>
  
```python
#!/usr/bin/env python3
"""Dinner Date Night Idea Generator | Author: Keriise Griffin-Marner

   Description:
   A script to utilize user input to generate the perfect date night 
   
   documentation for the API is available at https://docs.developer.yelp.com/docs/getting-started

   date_night_inspiration.py

   """


# to choose random answer from various results based on user input
import os
import random
import requests
import datetime
from pprint import pprint

# Welcome

def intro ():
    name = input("Welcome to the date night dinner idea generator! What's your name?\n")
    print("Hey {}! I know trying to make a last minute decision for dinner ccan really bring down the mood of a date night. So let's take some of the stress out of preparing for your upcoming date.\n".format(name))

# API Authorization
api_key = os.environ.get("YELP_API")

def parameters(location, term, api_key): # diet, price
    print(location, term)

    headers = {'Authorization': f'Bearer {api_key}'}
    
   
    url='https://api.yelp.com/v3/businesses/search'


    # In the dictionary, term can take values like food, cafes or businesses like McDonalds
    params = {'term': term,'location':location, 'limit': 50}

    response=requests.get(url, params=params, headers=headers)

    # Response verification
    if response.status_code == 200:
        data = response.json()
        businesses = data["businesses"]
        random.shuffle(businesses) # Shuffle API call results
       
        # Choose 6 businesses from shuffled results to display
        for i in range(6):
            business = businesses[i]
            for x in data["businesses"]:
                # Format output: Name/Address/Phone Number/URL
                display_address = " ".join(x["location"]["display_address"])
                display_address = display_address.replace(",","").replace(".","")
                print("Business Name: {} \nAddress: {} \nPhone Number: {} \nUrl: {}".format(x["name"], display_address, x["phone"], x["url"]))
                print()



    # If no business matches are found
    else:
        print(f'Hmmmm... I can\'t seem to find anything that fits those exact responses. Would you like to try again?')
        print(response.text)


    # Provide user option to have selection made for them

    while True:

        print ("These seem like some amazing places. If you're still having strouble making a selection, I can make it for you. Would you like me to? (y/n)")

        user_input = input()


        if user_input == "y":

            # Format output
            random_item = random.choice(data["businesses"])
            display_address = " ".join(random_item["location"]["display_address"])
            display_address = display_address.replace(",","").replace(".","")
            print("\nBusiness Name: {} \nAddress: {} \nPhone Number: {} \nUrl: {}".format(random_item["name"], display_address, random_item["phone"], random_item["url"]))
            print()
            print("This is going to be great! Now all you have to do is make a wardrobe selections and you're ready to go!")

            break

        elif user_input == "n":
            print("Perfect! Now all you need to do is make a few wardrobe selections and you're ready to go!")

            break

        else:
            print("That's not working. Let's keep it simple, please enter y or n")

# Main function to run the code/Request user input
def main():

    # Input for API search
    
    location = input("Let's start by telling me where you are. You can give me a zip code or a city & state. Which ever works best for you.\n")
    term = input("What is a type of food you've always wanted to try, but never went for?\n")
    parameters(location, term, api_key) 

intro()
main()
```
  
</details>

- prompts for location and date preferences
- makes an API call and returns matches  

<details>
<summary>RPG Game</summary>
  
```python
#!/usr/bin/python3

#imports time for time.sleep
import time

# an inventory, which is initially empty
inventory = []
#checks commands move[1] and move[2] for accuracy
commands = ['go' , 'get', 'look' , 'quit', 'exit'] 
commands2= [inventory, 'north', 'south','east','west', 'up', 'down' , 'in' , 'out']
counter = 1
# a dictionary linking a room to other rooms
rooms =  {

            'dark woods' : {
			    'south' : 'small clearing' ,
			    'north' : 'foothills',
                'description' : '''
        Dark Woods

        You are standing in a dark, wooded forest. The air is cold, and though it is still, it seems to seep into your light clothing, and you shiver.  To the [south] you see a small clearing of trees, and to the [north] you see the ground start to rise.  East and west are blocked by trees.
                ''', 
			    'item' : 'map',
                },
            'Castle of Knowledge' : {
                'south' : 'foothills' , 
                'port2' : 'master bedroom',
                'description' : '''
        Castle of Knowledge

        You are standing before a beautiful castle.  Somehow you know that this is your way out of here. Maybe you should return when you have more of an idea of what to do...you can procede no further and can only go back [south].
                ''',
            },

            'foothills' : {
                'south' : 'dark woods',
                'north' : 'Castle of Knowledge',
                'description' : '''
        Foothills

        You are in the foothills.  Your breathing becomes labored (and your hangover doesn\'t help) as you climb. To the [south] lies the dark woods, and to the [north] you see a majestic castle.
                ''',
            },

            'small clearing' : {
                  'north' : 'dark woods' ,
                  'west' : 'house courtyard' ,
                  'description' : '''
        Small Clearing

        You are standing in a small clearing of trees.  The open air allows you to catch your breath.  You see woods to the [north], and a small house to the [west]. The other ways are blocked.
                  ''' , 

                },
            'house courtyard' : {
                'east' : 'small clearing',
                'west' : 'house' ,
                'description' : '''
        House Courtyard
                
        You are in the courtyard of a decrepit house.  Broken bottles, like your programming hopes and dreams, lay strewn about and discarded.  Further [west] is the house entrance. The small clearing is to the [east], and the other ways are blocked.
                ''',
                
            
                },
            'house' : {
                'up' : 'second floor',
                'east' : 'house courtyard',
                'description' : '''
        House

        You are inside the decrepit house. It smells musty and rotten.  Discarded many old books sit on a broken table.  Going [up] you see a staircase.  [east] takes you back outside.
                ''' ,
                'item' : 'programming manual' ,
           },
            'second floor' : {
                'down' : 'house',
                'in' : 'master bedroom' , 
                'description' : '''
        Second Floor Hallway
                
        at the top of the staircase you emerge into a hall. The entire area smells like piss and bad decisions.  There is a single closed door at the end of the hall.  Go [in] or go [down]?
                ''',

                
            },
            'master bedroom' : {
                'out' : 'second floor',
                'port1' : 'Castle of Knowledge',
                'description' : '''
        Master Bedroom
                
        you have entered the master bedroom.  The smell of decay immediately hits your nostrils.  As your eyes adjust to the dark, you are shocked to see a lifeless body on the center of the bed.  You see a nametag and title pinned to the corpse\'s body.  It reads "Smith - TLG Learning Student".  In the corpse\'s hand is a piece of [paper]  The only exit is [out]
                ''' , 

                'item' : 'paper',
            },
        }

items = {
            
            'map' : {
                'description' : 
                '''
                                            [ castle    ]
                                                  |
                [master]                    [ foothills ] 
                    |                             |
                [hall  ]                    [ dark woods]
                    |                             |
                [house ]  -  [courtyard] -  [small clear]
                '''

                },

            'sword' : {
                'description' : 'the sword is razor sharp, like the margin you had passing previous certification tests',
                },
            
            'paper' : {
                 'description' : '''on the paper is printed: 
                 
                 I should have studied!

                 practice is the key!'''
                },
            
            'programming manual' : {
                'description' : 'the manual is dusty but unused.  Why didn\'t the previous owner practice?',
            }, 
        }


def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
      look [item]
      quit/exit
    ''')

def showStatus():
    """determine the current status of the player"""
     # print the player's current location
    print('---------------------------')
    print(rooms[currentRoom]['description'])
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    #checks to see if player is in the final room to trigger win function
    if rooms[currentRoom] == rooms['Castle of Knowledge']:
        if 'paper' and "programming manual" in inventory :
            win()
    print("---------------------------")

#function for winning game
def winquit():
    print (f"{playername}, thank you for playing!  You have escaped ignorance!  Keep practicing!")
    exit()
#function for quitting early
def quitgame():
    print("thank you for playing! (quitter!)")
    exit()
#function for win sequence
def win():
    print(f'''
    
    You have reached the castle.  
    
    a loud voice calls from above:
    
    "{playername},I am CHAD, your python instructor...  you lost the drinking game and now you are stuck here.  You have all of the tools you need. To get out, you must provide the key!
    
    Otherwise, you will rot here in ignorance.  You have three chances."

    You have learned some valuable lessons during your time in this alternate reality.  Can you provide the key to python success??
    
    ''')
    test()
#function for lose sequence
def lose():
    print('You have lost!  You are stuck in an infinite loop of ignorance!')
    exit()

#main test loop with counters
def test():
    left = 2
    counter = 0
    answer = ' '    
    while counter < 3 and (answer != 'PRACTICE' and answer != 'practice' ):
        answer= input('What is the key to success?  Shout it out!\n>>')
        counter +=1
     
        if answer == 'PRACTICE':
            print('''

            Chad's booming voice calls out:

            "YES!  YOU HAVE ANSWERED CORRECTLY AND ESCAPED A LIFE OF IGNORANCE!  GO FORTH, AND PRACTICE!"

            With that, you awaken in your own surroundings, an open python book in front of you.  
            
            Better get started!

            You WIN!

     
                ''')
    
            winquit()
        # coumter check for three tries
        elif counter == 3:
                print('Chad shouts "YOU DID NOT LEARN YOUR LESSON, AND MUST STAY HERE FOREVER!"') 
                lose()
        # prompt for uppercase
        elif answer == 'practice':
            print('no, you must SHOUT IT!')
            test()
        #counter for tries left
        else:
            print(f"Try again, you have {left} more tries ")
            left -=1

# start the player in the woods
currentRoom = 'dark woods'
itemlist = ''
showInstructions()
playername= input("Welcome to XXXXXX!  A game in which you are the guinea pig at the mercy of my very questionable python skills! \n \nPlease enter your name: \n").title()

print(f"You awaken with a start, in an unfamiliar land wearing dirty leather clothing.  You have a splitting headache.  Your last memory was sitting at your computer,  playing a drinking game with your python instructors Chad and Paul.  Every time you made a mistake in your python coding, you had to take a drink.  Double if you were caught hardcoding.  Obviously, you drank too much...")

time.sleep(3)

print(f'''
    ...your only hope now is to somehow escape from this strange dimension and get out of your infinite loop.
    

    good luck, {playername}
    ''')
# breaking this while loop means the game is over

time.sleep(5)



while True:
    showStatus()
    
    
    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')
    if move == 'quit' or move == 'exit':
        quitgame()
    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get programming manual" becomes ["get", "programming manual"]          
    # error correction in case user only enters one word, which causes errors
    if ' ' not in move:
        print('Please enter a two part command')
        continue
    move = move.lower().split(" ", 1)
    
    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
            
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
        
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' taken!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
    #to inspect an item
    if move[0] == 'look':
        #item must be in inventory
        if move[1] in inventory:
            print(items[move[1]]['description'])

        elif move[1] not in inventory:
            print(f'You dont have a {move[1]}')
        #below is hard code made before i figured out a better way.
        #elif move[1] == "paper":
            #print(items[move[1]]['description'])
        #elif move[1] == "sword":
            #print(items['sword']['description'])
        #elif move[1] == 'programming manual':
            #print(items['programming manual']['description'])
        time.sleep(3)
    if currentRoom == rooms['Castle of Knowledge']:
        win()
    
    elif move[0] not in commands:
        #try:
        print('sorry, your command was misunderstood.  Please use either \'get (item)\', \'go (direction)\', or \'look (item)\' ')
        #except: 
    #elif move[1] not in commands2:       #print('sorry')
        print('sorry, your command was misunderstood.  Please use either \'get (item)\', \'go (direction)\', or \'look (item)\' ')   
    elif move[1] =='':
        print('commands must be two-part')       #continue
win()        
```
  
</details>

- based off our RPG mini project
- includes many more rooms and an ASCII map
