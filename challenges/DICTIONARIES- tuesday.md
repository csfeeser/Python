# CHALLENGE: DICTIONARIES

1. Create a new script!

0. Include a shebang line.

0. Make your file executable with a ./

0. Save a user's input to the variable `char_name` from the following question:

        Which character do you want to know about? (Starlord, Mystique, Hulk)

0. Save a user's input to the variable `char_stat` from the following question:

        What statistic do you want to know about? (real name, powers, archenemy)

0. Use the char_name and char_stat values to pull the appropriate value from the dictionary below.

    ```
    marvelchars= {
    "Starlord":
      {"real name": "peter quill",
      "powers": "dance moves",
      "archenemy": "Thanos"},

    "Mystique":
      {"real name": "raven darkholme",
      "powers": "shape shifter",
      "archenemy": "Professor X"},

    "She-Hulk":
      {"real name": "bruce banner",
      "powers": "super strength",
      "archenemy": "adrenaline"}
                 }
    ```
    
0. Create a print function that combines that information into this output:

        <char_name>'s <char_stat> is: <value>

**POWER BONUS 1:** When returning the hero's name, have it capitalized appropriately (e.g. Wolverine, not wolverine)

<details>
<summary>Hints:</summary>
        
- Use the .**[title](https://docs.python.org/3/library/stdtypes.html#str.title)**() method to capitalize both parts of "harry potter" and "captain america"s names!  
      
</details>

**SUPER BONUS 2:** Make the user's input error proof!

<details>
<summary>Hints:</summary>

- Use the .**[lower](https://docs.python.org/3/library/stdtypes.html#str.lower)**() method so that any input from the user matches the case of `wolverine`,`harry potter`, or `captain america`!

</details>

<!--
**MEGA BONUS 3:** Allow the user to try again without exiting the script! Requires previous knowledge of **while loops**.

### Wow, done with all three? Try this one on for size:

```python
hero={'name':{'alias':'Batman','real name':'Bruce Wayne'},'background':{'origin':'Parents got murdered, got angry. Is super rich.','family':{'parents':'dead','siblings':None},'age':32,'number of deaths':19},'powers':['ninja training','money','batsuit'],'enemies':['joker','two face','scarecrow','poison ivy'],'allies':['cat woman','red robin','nightwing'],'rivals':['joker'],'weaknesses':['poverty','strict moral code']}
```

Using that dictionary, ask a user if they'd like to see all of Batman's enemies, allies, rivals, powers, or weaknesses. **Using a for loop,** display the contents of the chosen list.

<!-- 
```
hero= {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "highest", "strength": "money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}

answer= " "

while answer != "q":
  try:
    char_name= input("Which character do you want to know about? (Flash, Batman, Superman) ")

    char_stat= input("What statistic do you want to know about? (strength, speed, or intelligence) ")

    print(f"{char_name.capitalize()}'s {char_stat} is: {hero[char_name][char_stat].capitalize()}")
  except:
    print("You provided incorrect input.")

  answer= input("Press ENTER to choose another hero, or press Q to quit!")
```  
-->
