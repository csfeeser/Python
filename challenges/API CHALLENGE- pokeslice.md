# Practice With API Slicing

![Image description](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png)
![Image description](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png)
![Image description](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png)
![Image description](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/144.png)
![Image description](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/145.png)
![Image description](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/146.png)

Start by using the script provided below:

```python
#!/usr/bin/env python3

import requests

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    print(pokeapi)

main()
```

View the output from that URL here! https://pokeapi.co/api/v2/pokemon/bulbasaur

### Part 1- Slicing (NO for loop!)

- Find the `"sprites"` key. Print the URL to "front_default", which is a link to an image of your Pokemon!

<details>
<summary>SLICE SOLUTION</summary>
    <br>
pokeapi["sprites"]["front_default"]
</details>

### Part 2- Slicing WITH a for loop!

- Look at the `"moves"` key. It returns a list of dictionaries; each dictionary contains the name of one of the Pokemon's "moves."
- Print out the `"name"`s of ALL the selected Pokemon's `"moves"`. 

<details>
<summary>What should I be looping over?</summary>
    <br>
for x in pokeapi["moves']:
</details>

<details>
<summary>How do I slice those dictionaries returned by the for loop?</summary>
    <br>
x["move"]["name"]
</details>

### Part 3- Loop or NOT to Loop

- Look at the `"game_indices"` key. This returns a list of dictionaries; each dictionary contains the name of each Pokemon game this character appeared in! (*Pokemon Red*, *Pokemon Black*, *Pokemon Crystal*, etc.
- Count up the total number of games this Pokemon character appeared in. You can solve this with a loop or without a loop... your choice!
- Print the count of how many games the selected Pokemon has been in!

<details>
<summary>How could I count those up without a for loop?</summary>
    <br>
Use the len() function on pokeapi["game_indices"]
</details>

<details>
<summary>How could I count those up WITH for loop?</summary>
    <br>
Create a counter (games= 0, for instance). Then loop over pokeapi["game_indices"] and add 1 to `games` every time it loops.
</details>

### Bonuses!

- Go back to part 3. If you didn't use a loop, try to solve it WITH a loop! If you did use a loop, try to solve it WITHOUT a loop!
- That URL you returned in Part 1 that leads to a picture of your Pokemon? Use it to download the picture to `/home/student/static`! (use GOOGLE!)


## SOLUTION

```python
#!/usr/bin/env python3

import requests
import wget

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    # NIKK
    print(f"{pokeapi['name']} image- {pokeapi['sprites']['front_default']}")
    imgurl= pokeapi['sprites']['front_default']

    # BONUS
    wget.download(imgurl, "/home/student/static/")

    # J
    for x in pokeapi['moves']:
        print(' >', x['move']['name'])

    # ETHAN
    print(f"{pokeapi['name']} has appeared in {len(pokeapi['game_indices'])} games!")

    # J
    game_indices = 0

    for g in pokeapi['game_indices']:
        game_indices += 1

    print('This pokemon has appeared in', game_indices, 'video games')

main()
```
