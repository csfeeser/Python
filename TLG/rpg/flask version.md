### To recreate this project, do the following steps:

# STEP 1:

`mkdir -p ~/mycode/flaskdemo/templates`

Copy the following into `rpg.py`:

`vim ~/mycode/flaskdemo/rpg.py`

```python
#!/usr/bin/python3
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

rooms = {
            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key',
                  'desc'  : 'You are in a dusty hall. A kitchen that smells of death is to the south. An equally dusty dining room lies to the east.'
                },
            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                  'desc'  : 'You barely have time to take in the bone-strewn kitchen before amonster rises from the shadows and LUNGES AT YOU!'
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion',
                  'desc' : 'This dining room is caked with dust. All of the food has long since been eaten by rats.'
               },
            'Garden' : {
                  'north' : 'Dining Room',
                  'desc'  : 'This garden has long since gone to ruin. A rusty gate with a barely legible sign reads "I OPEN ONLY FOR THE HOLDER OF BOTH KEY AND POTION."'
               },
         }

# these are GLOBAL VARIABLES; they will be recognized inside every function
inventory= []
currentRoom= "Hall"
message= ""
gameover= False

# the entire game is played on this route
@app.route("/")
def start():
    # pull the dictionary for the current room
    x= rooms[currentRoom]
    # render the jinja2 html file, pass in all required variables
    return render_template("status.html", inv=inventory, currentRoom=currentRoom, currentroomdict=x, msg=message, gameover=gameover)

# when a player makes a move, it is POSTED to /action
@app.route("/action", methods=["POST"])
def action():
    # the global keyword allows us to edit the "message" global variable
    global message
    # check if anything was in the form submitted
    if request.form.get("nm"):
            # if so, pull the value and normalize it
            move = request.form.get("nm")
            move = move.lower().split(" ", 1)
            # call the goget() function to see what happens with that move
            message= goget(move)
            # use endcheck() function to see if a GAMEOVER has occurred
            x= endcheck()
            if x:
                message= x
    else:
        message= ""
    # the value of message (what gets displayed at the top of html) gets defined one way or another
    return redirect("/")

def endcheck():
    global gameover
    # victory condition
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        msg= 'You escaped the house with the ultra rare key and magic potion... YOU WIN!'
        gameover= True
        return msg
    # loss condition
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        msg= 'A monster has got you... GAME OVER!'
        gameover= True
        return msg
    else:
        return None

def goget(move):
    # check for go or get, and take appropriate action
    global currentRoom
    global inventory
    if move[0] == 'go':
        # if go is first word, and a valid direction is chosen
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
            return ""
        else:
            # if a nonvalid direction is chosen
            return "You can't go that way!"

    if move[0] == 'get' :
        # if get is first word, there's an item in the room, and the item is what you wanted to pick up:
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory.append(move[1])
            del rooms[currentRoom]['item']
            return f"{move[1]} got!"
        else:
            # if any of those conditions weren't met
            return "Can't get {move[1]}!"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
```   

# STEP 2:

Copy the following into `status.html`:

`vim ~/mycode/flaskdemo/templates/status.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>FLASK API ADVENTURE!</title>
<body>
{% if not gameover %}
        <p><strong>{{ msg }}</strong></p>

        <p>You are in the {{ currentRoom }}.<br />

        Inventory:</p>
        <ul>
        {% for item in inv %}
                 <li>{{item}}</li>
        {% endfor %}
        </ul>
        {% if "item" in currentroomdict and currentroomdict["item"][0] in ["a","e","i","o","u"] %}
                 <p>You see an {{ currentroomdict["item"] }}<br />
            {% elif "item" in currentroomdict and currentroomdict["item"][0] not in ["a","e","i","o","u"] %}
                  <p>You see a {{ currentroomdict["item"] }}<br />
        {% endif %}
        {{ currentroomdict.desc }}</p>
        <form action = "/action" method = "POST">
            <p><input type = "text" name = "nm"></p>
            <p><input type = "submit" value = "submit"></p>
        </form>
{% endif %}
{% if gameover %}
    {{ currentroomdict.desc }}</p>
    <p><strong>{{ msg }}</strong></p>
{% endif %}
</body>
</html>
```
