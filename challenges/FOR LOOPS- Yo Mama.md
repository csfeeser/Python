# Looping Through Dictionaries With Yo Mama

Looping through dictionaries isn't easy! We'll be tackling some challenging APIs today... Chad elected to make a slightly simplified version of the NASA Asteroids API to practice with. He just replaced the asteroids with yo mamas.

**NOTE: no actual mommas are being referenced in this lab. If your momma shares a name with any of these mommas, it is purely coincidental.**

0. Create a new file in a directory of your choice.

    `student@bchd:~` `vim mommas.json`
    
0. Paste in the following:

    ```
    {"east_coast_mommas":[{"name": "Slobby","estimated_diameter": {"kilometers": {"diameter_min": 0.3,"diameter_max": 0.5},"miles": {"diameter_min": 0.02,"diameter_max": 0.03}},"is_potentially_hazardous": false},{"name": "Bingo","estimated_diameter": {"kilometers": {"diameter_min": 0.43,"diameter_max": 0.53},"miles": {"diameter_min": 0.042,"diameter_max": 0.033}},"is_potentially_hazardous": true}],"west_coast_mommas":[{"name": "Scratchy","estimated_diameter": {"kilometers": {"diameter_min": 0.3,"diameter_max": 0.5},"miles": {"diameter_min": 0.02,"diameter_max": 0.03}},"is_potentially_hazardous": false},{"name": "Bubba","estimated_diameter": {"kilometers": {"diameter_min": 0.43,"diameter_max": 0.53},"miles": {"diameter_min": 0.042,"diameter_max": 0.033}},"is_potentially_hazardous": true}],"central_mommas":[{"name": "Sweaty","estimated_diameter": {"kilometers": {"diameter_min": 0.3,"diameter_max": 0.5},"miles": {"diameter_min": 0.02,"diameter_max": 0.03}},"is_potentially_hazardous": false},{"name": "Croaky","estimated_diameter": {"kilometers": {"diameter_min": 0.43,"diameter_max": 0.53},"miles": {"diameter_min": 0.042,"diameter_max": 0.033}},"is_potentially_hazardous": true}]}
    ```
    
0. Save and quit.

0. Make another file IN THE SAME DIRECTORY.


    `student@bchd:~/mycode/` `vim mamachallenge.py`
    
0. Paste in the following:

    ```
    import json

    file= open("mommas.json", "r").read()

    mommas= json.loads(file)

    print(mommas)
    ```

### CHALLENGE 1:

- Write a for loop that goes through the "east_coast_mamas" and returns their names.

### CHALLENGE 2:

- Write a for loop that goes through the ALL mamas and returns their names.

### CHALLENGE 3:

- Write a script that returns which mommas are the largest.
- Write a script that return a random momma's name... IN A YO MOMMA JOKE.
