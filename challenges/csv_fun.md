## LAST TASK OF THE DAY:

`student@bchd~:` `mkdir -p ~/pokedex && cd ~/pokedex && wget https://raw.githubusercontent.com/csfeeser/Python/master/data%20sets/pokedex.txt`

Take this code and make it your own!

```
import csv

pokenum= input(">")

with open("pokedex.txt","r") as pokedata:
    for x in csv.DictReader(pokedata):
        pokedict= dict(x)
        if pokedict["#"] == pokenum:
            print(f"{pokedict['Name']} is of the {pokedict['Type 1']} type!")
```

Suggestions:

- Return more data! (attack, defense, HP, etc.)
- Return multiple pokemon!
- Return only pokemon from a specific generation!
- Return only pokemon from a specific type!
- Return only LEGENDARY pokemon!

WHEN YOU HAVE SOMETHING TO SHOW CHAD:

- Send it in the chat or push it to GitHub and share the link!

Once you've accomplished this, you can call it a day...

- HOWEVER, if Chad hasn't gotten your if-logic script yet hang around and we'll work on it some more!
