# "Looping with for" Challenge!

![Image description](https://i.kym-cdn.com/photos/images/newsfeed/001/822/189/47f.jpg)

```
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
```

### Test

• Write a for loop that returns all the animals from the NE Farm!

### Trial

• Ask a user to choose a farm (NE Farm, W Farm, or SE Farm). Return the plants/animals that are raised on that farm.

### Challenge

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
