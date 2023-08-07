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
    "all": people_info = [
	    {
	        "Name": "Alex",
	        "Spirit Animal": "Tiger",
	        "Super Power": "Telekinesis",
	        "Skill Level": "Phenomenal"
	    },
	    {
	        "Name": "Benji",
	        "Spirit Animal": "Bear",
	        "Super Power": "Time Manipulation",
	        "Skill Level": "Spectacular"
	    },
	    {
	        "Name": "Cayla",
	        "Spirit Animal": "Owl",
	        "Super Power": "Flight",
	        "Skill Level": "Magnificent"
	    },
	    {
	        "Name": "Demetra",
	        "Spirit Animal": "Dragonfly",
	        "Super Power": "Invisibility",
	        "Skill Level": "Astounding"
	    },
	    {
	        "Name": "Derek",
	        "Spirit Animal": "Wolf",
	        "Super Power": "Teleportation",
	        "Skill Level": "Marvelous"
	    },
	    {
	        "Name": "Deshawn",
	        "Spirit Animal": "Eagle",
	        "Super Power": "Super Strength",
	        "Skill Level": "Incredible"
	    },
	    {
	        "Name": "James",
	        "Spirit Animal": "Lion",
	        "Super Power": "Mind Reading",
	        "Skill Level": "Wonderful"
	    },
	    {
	        "Name": "Maria",
	        "Spirit Animal": "Fox",
	        "Super Power": "Shape-Shifting",
	        "Skill Level": "Astonishing"
	    },
	    {
	        "Name": "Marylyn",
	        "Spirit Animal": "Dolphin",
	        "Super Power": "Telepathy",
	        "Skill Level": "Epic"
	    },
	    {
	        "Name": "Nor",
	        "Spirit Animal": "Butterfly",
	        "Super Power": "Elemental Control",
	        "Skill Level": "Fantastic"
	    },
	    {
	        "Name": "Sal",
	        "Spirit Animal": "Tiger",
	        "Super Power": "Telekinesis",
	        "Skill Level": "Phenomenal"
	    },
	    {
	        "Name": "Sammy",
	        "Spirit Animal": "Bear",
	        "Super Power": "Time Manipulation",
	        "Skill Level": "Spectacular"
	    }
	]

}
```


### SOLUTION

<details>
<summary>Click here!</summary>
	
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

</details>
