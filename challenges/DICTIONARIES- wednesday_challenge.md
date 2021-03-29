# CHALLENGE: DICTIONARIES

1. Create a new script!

0. Include a shebang line.

0. Make your file executable with a ./

0. Save a user's input to the variable `char_name` from the following question:

        Which character do you want to know about? (Wolverine, Harry Potter, Agent Fitz)

0. Save a user's input to the variable `char_stat` from the following question:

        What statistic do you want to know about? (real name, powers, archenemy)

0. Use the char_name and char_stat values to pull the appropriate value from the dictionary below.

    ```
    heroes=  {
    "Wolverine":
        {"real name": "James Howlett",
        "powers": "regeneration",
        "archenemy": "Sabertooth",},
    "Harry Potter":
        {"real name": "Harry Potter",
        "powers": "he's a wizard",
        "archenemy": "Voldemort",},
    "Agent Fitz":
        {"real name": "Leopold Fitz",
        "powers": "intelligence",
        "archenemy": "Hydra",}
            }
    ```
    
0. Create a print function that combines that information into this output:

        <char_name>'s <char_stat> is: <value>

**BONUS 1:** When returning the hero's name, have it capitalized appropriately (e.g. Flash, not flash)

**SUPER BONUS 2:** Make the user's input error proof!

**MEGA SUPER BONUS 3:** Allow the user to try again without exiting the script!

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
