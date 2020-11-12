## "Looping with for" Challenge!

![Image description](https://github.com/csfeeser/TLG-Python/blob/master/skill%20level.png?raw=true)

#### Challenge Level will be determined by the DOOM2 Difficulty Scale

```
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
```

### Hey, Not Too Rough

• Write a for loop that returns all the animals from the NE Farm!

### Hurt Me Plenty

• Ask a user to choose a farm (NE Farm, W Farm, or SE Farm). Return the plants/animals that are raised on that farm.

### NIGHTMARE

• Ask a user to choose a farm (NE Farm, W Farm, or SE Farm)... but only return ANIMALS from that particular farm.


```python
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

print("""
~~**[[Pick a farm!]]**~~
========================
0. NE Farm
1. W Farm
2. SE Farm
""")

choice= int(input())

FORBIDDEN= ["celery","carrots"]
YUMMY= ["pigs", "chickens", "llamas","sheep", "cows"]

for x in farms[choice]["agriculture"]:
  # if x in FORBIDDEN:
   if x in YUMMY:
       print(f"{x}... yum!")
       #print(f"Yuck! I don't want {x}!")
   else:
       #print(f"{x}... yum!")
       print(f"Yuck! I don't want {x}!")
```
