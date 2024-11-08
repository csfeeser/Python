### Warmup Activity: Haunted House Adventure with Flask and Jinja2!

![Image description](https://github.com/csfeeser/images/blob/master/pythondragon.png?raw=true)

**Objective**:  
Complete the Jinja2 template to display the player's current room, room description, most recent message about what happened, and their inventory.

### Steps to Set Up

1. **Create the project directory and template folder**:

    ```bash
    mkdir -p ~/mycode/day4warmup/templates
    ```

0. **Create `rpg.py`**:

    ```bash
    vim ~/mycode/day4warmup/rpg.py
    ```

    **Copy the following code into `rpg.py`:**

    ```python
    #!/usr/bin/python3
    from flask import Flask, redirect, render_template, request

    app = Flask(__name__)

    rooms = {
                'Hall': {
                      'south': 'Kitchen',
                      'east': 'Dining Room',
                      'item': 'key',
                      'desc': 'You are in a dusty hall. A kitchen that smells of death is to the south. An equally dusty dining room lies to the east.'
                    },
                'Kitchen': {
                      'north': 'Hall',
                      'item': 'monster',
                      'desc': 'You barely have time to take in the bone-strewn kitchen before a monster rises from the shadows and LUNGES AT YOU!'
                    },
                'Dining Room': {
                      'west': 'Hall',
                      'south': 'Garden',
                      'item': 'potion',
                      'desc': 'This dining room is caked with dust. All of the food has long since been eaten by rats.'
                   },
                'Garden': {
                      'north': 'Dining Room',
                      'desc': 'This garden has long since gone to ruin. A rusty gate with a barely legible sign reads "I OPEN ONLY FOR THE HOLDER OF BOTH KEY AND POTION."'
                   },
             }

    inventory = []
    currentRoom = "Hall"
    message = ""
    gameover = False

    @app.route("/")
    def start():
        x = rooms[currentRoom]
        return render_template("status.html", inv=inventory, currentRoom=currentRoom, currentroomdict=x, msg=message, gameover=gameover)

    @app.route("/action", methods=["POST"])
    def action():
        global message
        if request.form.get("nm"):
            move = request.form.get("nm").lower().split(" ", 1)
            message = goget(move)
            if endcheck():
                message = endcheck()
        else:
            message = ""
        return redirect("/")

    def endcheck():
        global gameover
        if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
            gameover = True
            return 'You escaped the house with the ultra rare key and magic potion... YOU WIN!'
        elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
            gameover = True
            return 'A monster has got you... GAME OVER!'
        else:
            return None

    def goget(move):
        global currentRoom
        global inventory
        if move[0] == 'go':
            if move[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][move[1]]
                return ""
            else:
                return "You can't go that way!"
        elif move[0] == 'get':
            if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
                inventory.append(move[1])
                del rooms[currentRoom]['item']
                return f"{move[1]} got!"
            else:
                return f"Can't get {move[1]}!"
        return ""

    if __name__ == "__main__":
       app.run(host="0.0.0.0", port=2224)
    ```

0. **Create the starter `status.html` file**:

    ```bash
    vim ~/mycode/day4warmup/templates/status.html
    ```

    **Copy the following starter code into `status.html`:**

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>FLASK API ADVENTURE!</title>
    </head>
    <body>

        <!-- Display the most recent message of what happened in game (msg) -->
        <!-- Display the name of the current room (currentRoom) -->
    
        {% if not gameover %}

            <!-- Inventory list with a for-loop to show each item -->
            
            {% if "item" in currentroomdict %}
                <p>You see: {{ currentroomdict["item"] }}</p>
            {% endif %}

        <!-- Display the room's description (desc) -->
       
            <form action="/action" method="POST">
                <p><input type="text" name="nm"></p>
                <p><input type="submit" value="submit"></p>
            </form>
        {% endif %}

    </body>
    </html>
    ```

### Provided Variables for Jinja2 Template

**DON'T COPY/PASTE the following, just read this line:**

```python
return render_template("status.html", inv=inventory, currentRoom=currentRoom, currentroomdict=x, msg=message, gameover=gameover)
```

Those are the variables that are being passed into the Jinja2 HTML template. Remember the variable on the LEFT (`inv`, not `inventory`) is the variable you can use in the template! Here is a table breaking down what each of those variables are:

| Variable         | Type     | Description                                                                                     |
|------------------|----------|-------------------------------------------------------------------------------------------------|
| `currentRoom`    | `string` | Name of the player's current room, e.g., "Hall".                                                |
| `currentroomdict`| `dict`   | Dictionary with details of the current room, including description and items.                   |
| `msg`            | `string` | Most recent message about the player's action (like a success or failure message).              |
| `inv`            | `list`   | List of items in the player's inventory, e.g., `["key", "potion"]`.                            |
| `gameover`       | `boolean`| Boolean indicating if the game has ended (`True`) or is ongoing (`False`).                      |

## YOUR OBJECTIVE:

- Edit the above jinja2 template where there are `<!-- HTML comments -->` to indicate where a change needs to occur. Use the variables from the table.
- Below is an example of what your HTML may look like in `aux1` after all Jinja2 expressions have been added to it. Words squared off in red represents data being passed into the file.

![image](https://github.com/user-attachments/assets/c96c9568-aa90-4c0d-b12a-26b9cf75f531)

- This is the VICTORY screen!

![image](https://github.com/user-attachments/assets/24cc210e-adac-4a63-8c77-c50764d94063)

- This is the FAILURE screen!

![image](https://github.com/user-attachments/assets/f9e84cf7-d445-4d7a-a9a4-3f275fe3f63a)

<details>
<summary>Solution</summary>

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>FLASK API ADVENTURE!</title>
</head>
<body>

    <!-- Display the most recent message -->
    <p><strong>{{ msg }}</strong></p>

    <!-- Display the name of the current room -->
    <p>You are in the {{ currentRoom }}.</p>
    
    {% if not gameover %}

        <!-- Inventory list -->
        <p>Inventory:</p>
        <ul>
            {% for item in inv %}
                <li>{{ item }}</li>
            {% endfor %}
        </ul>
        
        {% if "item" in currentroomdict %}
            <p>You see: {{ currentroomdict["item"] }}</p>
        {% endif %}

    <!-- Display the room's description -->
    <p>{{ currentroomdict.desc }}</p>
        
        <form action="/action" method="POST">
            <p><input type="text" name="nm"></p>
            <p><input type="submit" value="submit"></p>
        </form>
    {% endif %}

</body>
</html>
```

</details>

### Run Your Flask App
```bash
python3 ~/mycode/day4warmup/rpg.py
```

Then visit `aux1` to view the game!
