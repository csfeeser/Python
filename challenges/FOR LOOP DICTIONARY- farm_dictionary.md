# "Looping with for" Challenge!

![Image description](https://i.kym-cdn.com/photos/images/newsfeed/001/822/189/47f.jpg)

```
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
```

### Part 1

• Write a for loop that returns all the animals from the NE Farm!

<details>
<summary>Gimme a hint!</summary>
<br>

    NE_animals= farms[0]["agriculture"]

<details>
<summary>Gimme another hint!</summary>
<br>    

    NE_animals= farms[0]["agriculture"]
         
    for x in NE_animals:
         print(x)

</details>
</details>

### Part 2

• Ask a user to choose a farm (NE Farm, W Farm, or SE Farm). Return the plants/animals that are raised on that farm.

<details>
<summary>Gimme a hint!</summary>
<br>

    for farm in farms:
        print("-", farm["name"])
    choice= input("Pick a farm!\n")

<details>
<summary>Gimme another hint!</summary>
<br>

    for farm in farms:
        print("-", farm["name"])
    choice= input("Pick a farm!\n")

    for farm in farms:
        if farm["name"].lower() == choice.lower():
            # you do the rest!

</details>
</details>

### Part 3

• Ask a user to choose a farm (NE Farm, W Farm, or SE Farm)... but only return ANIMALS from that particular farm.

<details>
<summary>Gimme a hint!</summary>
<br>
    
    yuck= ["carrots", "celery"]
    
<details>
<summary>Gimme another hint!</summary>
<br>

    yuck= ["carrots", "celery"]
    
    for farm in farms:
        print("-", farm["name"])
    choice= input("Pick a farm!\n")

    for farm in farms:
        if farm["name"].lower() == choice.lower():
            for ag_item in farm["agriculture"]:
                if ag_item not in yuck:
                     print(ag_item)

</details>
</details>
    
### SUPER BONUS

Test the flexibility of your code... does it still work if you swap the value of farms for this?

```
farms = [{"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]
```
