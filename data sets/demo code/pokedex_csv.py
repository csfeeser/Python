import csv
  
with open("pokedex_gen1.txt") as pokedata:
    for x in csv.DictReader(pokedata):
        print(f'{x["Name"]} has an attack score of {x["Attack"]}.')
