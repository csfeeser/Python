# Practice With API Slicing

![Image description](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png)
![Image description](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png)
![Image description](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png)
![Image description](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/144.png)
![Image description](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/145.png)
![Image description](https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/146.png)

Start by using the script provided below:

```
#!/usr/bin/env python3

# imports always go at the top of your code
import requests

def main():
    pokeapi = requests.get("https://pokeapi.co/api/v2/pokemon/ditto").json()

    print(pokeapi)

main()
```

The Pokemon API can be found here! https://pokeapi.co/

### THE CHALLENGE

Use your script to print out the following:

1. Change the Pokemon in the URL to a Pokemon of your choice! **BONUS**- add input to collect what Pokemon to look up!

0. Print the URL to "front_default", which is a link to an image of your Pokemon! **BONUS**- download the image (one tool you could use is the wget module... or write to file with "wb"!)!

0. Return a count of how many "game_indices" the selected Pokemon has been in!

0. Print out the "name"s of ALL the selected Pokemon's "moves".
