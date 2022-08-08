# CHALLENGE: Complex Data Slicing, For Loops, and Superhero Programmers!

<img src="https://simpleprogrammer.com/wp-content/uploads/2019/04/programmer-hero.png" alt="drawing" width="300"/>

### Attempt these challenges in increasing difficulty!

**Part 1.** Find your name in the `classinfo` dictionary below. Write code that prints your first name from the `classinfo` data shown here.

**Part 2.** Find your name in the `classinfo` dictionary below.  Write a script that outputs **ONE** of the following using the `classinfo` dictionary below. (fill in the blank!):

	My name is ______ and my spirit animal is _______.

	My name is ______ and my skills are _______.

	My name is ______ and my super power is _______.


**Part 3.** Write a script that loops through the entire `classinfo` dictionary. Have it output the following for every person in class:

#### EXAMPLE:
	

    Mario, a <wondrous> <alpaca> of a programmer, possesses a <structure weakening> factor for moonlighting as a superhero!
    
    Luigi, an <admirable> <donkey> of a programmer, possesses a <super strength> factor for moonlighting as a superhero!

[...and so on!]

[Chad's janky code to make this dictionary for each of his classes](https://github.com/csfeeser/Python/blob/master/solutions/classinfomaker.py)

```python
classinfo = {
    "all": [
        {
            "name": "Leo",
            "skill level": "wondrous",
            "spirit animal": "Alpaca",
            "super power": "Structure Weakening",
        },
        {
            "name": "Andi",
            "skill level": "admirable",
            "spirit animal": "Shark",
            "super power": "Super Strength",
        },
        {
            "name": "Bianca",
            "skill level": "amazing",
            "spirit animal": "Goat",
            "super power": "Weather Control",
        },
        {
            "name": "Charlie",
            "skill level": "astonishing",
            "spirit animal": "Banana",
            "super power": "Flight",
        },
        {
            "name": "Cynthia",
            "skill level": "awesome",
            "spirit animal": "Horse",
            "super power": "X-ray Vision",
        },
        {
            "name": "Davi",
            "skill level": "brilliant",
            "spirit animal": "Eagle",
            "super power": "Helicopter Propulsion",
        },
        {
            "name": "Eric",
            "skill level": "cool",
            "spirit animal": "Rabbit",
            "super power": "Invisibility",
        },
        {
            "name": "Jacob",
            "skill level": "enjoyable",
            "spirit animal": "Water buffalo",
            "super power": "Immobility",
        },
        {
            "name": "Jim",
            "skill level": "excellent",
            "spirit animal": "Chicken",
            "super power": "Immutability",
        },
        {
            "name": "Paul",
            "skill level": "fabulous",
            "spirit animal": "Duck",
            "super power": "Invulnerability",
        },
        {
            "name": "Joseph",
            "skill level": "fantastic",
            "spirit animal": "Goose",
            "super power": "Jet Propulsion",
        },
        {
            "name": "Josia",
            "skill level": "fine",
            "spirit animal": "Pigeon",
            "super power": "Matter Ingestion",
        },
        {
            "name": "Kendra",
            "skill level": "incredible",
            "spirit animal": "Turkey",
            "super power": "Mobile Invulnerability",
        },
        {
            "name": "Tito",
            "skill level": "magnificent",
            "spirit animal": "Aardvark",
            "super power": "Muscle Manipulation",
        },
        {
            "name": "Ryan",
            "skill level": "marvelous",
            "spirit animal": "Aardwolf",
            "super power": "Nail Manipulation",
        },
        {
            "name": "Sabin",
            "skill level": "outstanding",
            "spirit animal": "Elephant",
            "super power": "Needle Projection",
        },
        {
            "name": "Lawrence",
            "skill level": "phenomenal",
            "spirit animal": "Leopard",
            "super power": "Organic Constructs",
        },
        {
            "name": "Sharry",
            "skill level": "pleasant",
            "spirit animal": "Albatross",
            "super power": "Prehensile Hair",
        },
        {
            "name": "Sheraz",
            "skill level": "pleasing",
            "spirit animal": "Alligator",
            "super power": "Prehensile Tail",
        },
        {
            "name": "Sunny",
            "skill level": "remarkable",
            "spirit animal": "Alpaca",
            "super power": "Prehensile Tongue",
        },
    ]
}
```


### SOLUTION

```python
# parts 1 and 2
name= classinfo["all"][2]["name"]
power= classinfo["all"][2]["super power"]

print(name, "has the power of", power)

# part 3
for x in classinfo["all"]:
    name= x["name"]
    skill= x["skill level"]
    power= x["super power"]
    animal= x["spirit animal"]

    # Mario, a <wondrous> <alpaca> of a programmer, possesses a <structure weakening> factor for moonlighting as a superhero!
    print(f"{name}, a {skill} {animal} of a programmer, possesses a {power} factor for moonlighting as a superhero!")
```
