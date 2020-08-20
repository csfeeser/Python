# List Comprehensions

### Objective

This lab will introduce students to the basics of list comprehensions.

### Procedure

0. First let's start with creating a basic list of all the numbers that each die could have, and add it to their list.

    `student@pyb-000-bchd:~$` `vim dice-roller.py`

        red = []
        blue = []

        for i in range(1,7):
            red.append(f'red {i}')
            blue.append(f'blue {i}')

        print(red)
        print(blue)

0. Run your script and make sure you are getting these lists built for you as follows:

    `student@pyb-000-bchd:~$` `python3 dice-roller.py`

        ['red 1', 'red 2', 'red 3', 'red 4', 'red 5', 'red 6']
        ['blue 1', 'blue 2', 'blue 3', 'blue 4', 'blue 5', 'blue 6']

0. Now, get back into your script, and let's put together a list of all the possible combinations that these dice could have. We will have this information coming back to us as a list of tuples. Add this **UNDER** the existing code.

    `student@pyb-000-bchd:~$` `vim dice-roller.py`

        combo = []
        for die in red:
            for dice in blue:
                combo.append((die, dice))

        print(combo)

0. Okay, now run the script again.

     `student@pyb-000-bchd:~$` `python3 dice-roller.py`

        ['red 1', 'red 2', 'red 3', 'red 4', 'red 5', 'red 6']
        ['blue 1', 'blue 2', 'blue 3', 'blue 4', 'blue 5', 'blue 6']
        [('red 1', 'blue 1'), ('red 1', 'blue 2'), ('red 1', 'blue 3'), ('red 1', 'blue 4'),
         ('red 1', 'blue 5'), ('red 1', 'blue 6'), ('red 2', 'blue 1'), ('red 2', 'blue 2'),
         ('red 2', 'blue 3'), ('red 2', 'blue 4'), ('red 2', 'blue 5'), ('red 2', 'blue 6'),
         ('red 3', 'blue 1'), ('red 3', 'blue 2'), ('red 3', 'blue 3'), ('red 3', 'blue 4'),
         ('red 3', 'blue 5'), ('red 3', 'blue 6'), ('red 4', 'blue 1'), ('red 4', 'blue
         2'), ('red 4', 'blue 3'), ('red 4', 'blue 4'), ('red 4', 'blue 5'), ('red 4',
         blue 6'), ('red 5', 'blue 1'), ('red 5', 'blue 2'), ('red 5', 'blue 3'), ('red
         5', 'blue 4'), ('red 5', 'blue 5'), ('red 5', 'blue 6'), ('red 6', 'blue 1'),
         ('red 6', 'blue 2'), ('red 6', 'blue 3'), ('red 6', 'blue 4'), ('red 6', 'blue
         5'), ('red 6', 'blue 6')]

0. The output is exactly what we want, however, the code is a bit sloppy and cumbersome. Let's make a new file, and try to do this again with list comprehensions. First of all, let's just try making the red list.

     `student@pyb-000-bchd:~$` `vim dice-comprehension.py`

         red = [f'red {i}' for i in range(1,7)]
         print(red)

     Notice how we are still keeping our for loop `for i in range(1,7)`, but now, instead of appending to the list we created, we simply are setting the list item as the object that goes before the **for** loop, `f'red {i}'`.

0. Try it out!

     `student@pyb-000-bchd:~$` `python3 dice-comprehension.py`

         ['red 1', 'red 2', 'red 3', 'red 4', 'red 5', 'red 6']

0. **Mini Challenge**: Create a list comprehension to create the blue list, based off of the format of the red list above. Once you have done that, make sure your output is:


     `student@pyb-000-bchd:~$` `python3 dice-comprehension.py`

         ['red 1', 'red 2', 'red 3', 'red 4', 'red 5', 'red 6']
         ['blue 1', 'blue 2', 'blue 3', 'blue 4', 'blue 5', 'blue 6']

0. Next, let's create a list comprehension to clear up our combo list. Add this to the bottom of your script. **Note that the line break is not necessary, and may result in your code not functioning properly if done improperly.** The line break here is so that we can more easily see the relationship of the two **for** loops that we already have used.

     `student@pyb-000-bchd:~$` `vim dice-comprehension.py`

        combo = [(r_die, b_die) for r_die in red
                                for b_die in blue]
        print(combo)

0. Try it out again.

     `student@pyb-000-bchd:~$` `python3 dice-comprehension.py`

     ['red 1', 'red 2', 'red 3', 'red 4', 'red 5', 'red 6']
     ['blue 1', 'blue 2', 'blue 3', 'blue 4', 'blue 5', 'blue 6']
     [('red 1', 'blue 1'), ('red 1', 'blue 2'), ('red 1', 'blue 3'), ('red 1', 'blue 4'),
      ('red 1', 'blue 5'), ('red 1', 'blue 6'), ('red 2', 'blue 1'), ('red 2', 'blue 2'),
      ('red 2', 'blue 3'), ('red 2', 'blue 4'), ('red 2', 'blue 5'), ('red 2', 'blue 6'),
      ('red 3', 'blue 1'), ('red 3', 'blue 2'), ('red 3', 'blue 3'), ('red 3', 'blue 4'),
      ('red 3', 'blue 5'), ('red 3', 'blue 6'), ('red 4', 'blue 1'), ('red 4', 'blue
      2'), ('red 4', 'blue 3'), ('red 4', 'blue 4'), ('red 4', 'blue 5'), ('red 4',
      blue 6'), ('red 5', 'blue 1'), ('red 5', 'blue 2'), ('red 5', 'blue 3'), ('red
      5', 'blue 4'), ('red 5', 'blue 5'), ('red 5', 'blue 6'), ('red 6', 'blue 1'),
      ('red 6', 'blue 2'), ('red 6', 'blue 3'), ('red 6', 'blue 4'), ('red 6', 'blue
      5'), ('red 6', 'blue 6')]

0. Excellent! Take some time to practice doing your own list comprehensions now!
