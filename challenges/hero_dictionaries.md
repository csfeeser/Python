## DICTIONARY WARMUP

#### Part 1

Create a script that includes the following dictionary:

```
heroes= {"flash":
                   {"speed": "fastest", 
                    "intelligence": "lowest", 
                    "strength": "lowest"}, 
         "batman":
                   {"speed": "slowest", 
                    "intelligence": "highest", 
                    "strength": "money"}, 
         "superman":
                   {"speed": "fast", 
                    "intelligence": "average", 
                     "strength": "strongest"}}
```
    
Create the following outputs- the output in <ANGLE BRACKETS> must come from the dictionary!
        
```
Flash is <fastest>!
Superman is <strongest>!
Batman has the ultimate super power: <money>
```

<details>
<summary>Help me Chadly Wan Kenobi!</summary>

    print(f"Flash is {heroes['flash']['speed']}!")
    # OR
    print("Flash is " + heroes['flash']['speed'] + "!")
        
</details>
        
#### Part 2

1. Create a variable `char_name`. Use the `input()` function to assign it a value from the following prompt:

        Which character do you want to know about? (Flash, Batman, Superman)
        
0. Create a variable `char_stat`. Use the `input()` function to assign it a value from the following prompt:

        What statistic do you want to know about? (strength, speed, or intelligence)
        
0. After a user provides input, use the values of `char_name` and `char_stat` values to pull the appropriate value from the dictionary below. 

    ```
    heroes= {"flash":
                       {"speed": "fastest", 
                        "intelligence": "lowest", 
                        "strength": "lowest"}, 
             "batman":
                       {"speed": "slowest", 
                        "intelligence": "Highest", 
                        "strength": "Money"}, 
             "superman":
                       {"speed": "fast", 
                        "intelligence": "average", 
                         "strength": "strongest"}}
    ```
    
0. You should return an output line that looks like this:

        flash's speed is: fastest

**BONUS: When returning the hero's name, have it capitalized appropriately (e.g. Flash, not flash)**
        
        Flash's speed is: FASTEST
        
<details>
<summary>Help me Chadly Wan Kenobi!</summary>

    char_name= input("Which character do you want to know about? (Flash, Batman, Superman)\n>")
    char_stat= input("What statistic do you want to know about? (strength, speed, or intelligence)\n>")

    print(f"{char_name.capitalize()}'s {char_stat} is: {heroes[char_name.lower()][char_stat.lower()].upper()}")
        
</details>
        

