### IMPORTING MODULES

It's very important to know how to import modules so you have access to as many tools as possible! Review the videos in labs 23 and 24 if you need more instruction outside of class.

Module practice:

Use `random.randint(x,y)` to return a number between x and y.
Use `random.choice(z)` to return a random value from z (usually a list).

Some ideas to practice with these:
 - print a number that is between 1 and 6
 - print two numbers between 1 and 6
 - print two numbers and figure out which one is bigger, then say that person is the winner!

<details>
<summary>Show me!</summary>

```python
import random

player1= random.randint(1,6)
player2= random.randint(1,6)

if player1 > player2:
    print("Player 1 wins!")
elif player1 == player2:
    print("Draw!")
else:
    print("Player 2 wins!")
```

</details>

### FOR LOOPS

BAD NEWS: for loops are one of the hardest concepts to master.
GOOD NEWS: they allow you to do amazing things with your code AND are used in pretty much every computer discipline... so once you learn it will serve you well!

The most common object to loop over is a list. Experiment looping over these lists

```python

# can you loop over this list and print "<hero name> is great!"
heroes= ["Batman","Spiderman","Catwoman","Alfred Pennyworth"]

# can you loop over this list of dictionaries are print: "<hero name>'s power is <power>"
hero_dict= [{"name": "Batman", "powers": "being the world's greatest detective"},
            {"name": "Spiderman", "powers": "web shooting"},
            {"name": "Catwoman", "powers": "burglary"},
            {"name": "Alfred Pennyworth", "powers": "being super butler"}
           ]
```

### READING/WRITING TO FILES

Data should ALWAYS come from outside your Python code, so you will always need to be able to read in the content of a file!


