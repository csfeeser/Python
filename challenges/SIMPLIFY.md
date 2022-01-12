# Simplifying Code


<img src="https://images.squarespace-cdn.com/content/v1/56e0aa00a3360c10606c90b8/1467855766712-J37RID0B92VM6OQL2LE0/keeping-it-simple-project-plan-from-point-a-to-point-b.jpg" alt="drawing" width="500"/>

### If it works, it works! But as we get more and more proficient with Python, writing code that is SHORT and EFFICIENT is easier to read, easier to write, easier to reuse!

Below is code that WORKS, but it needs trimmed down!

1. Create a directory for this challenge and move into it.

    `student@bchd:~` `mkdir -p ~/mycode/challenge && cd ~/mycode/challenge`
    
0. Download the `pokedex.txt` data that we've used before :)

    `student@bchd:~/mycode/challenge$` `wget https://raw.githubusercontent.com/csfeeser/Python/master/data%20sets/pokedex.txt`
    
0. Ensure that `pandas` is installed.

    `student@bchd:~/mycode/challenge$` `python3 -m pip install pandas`
    
0. Create the file below. You may make ANY CHANGES YOU LIKE, **as long as the output remains the same**. Try to make this script as short as possible :)

    `student@bchd:~/mycode/challenge$` `vim challenge.py`
    
```python
#!/usr/bin/env python3

import pandas as pd

def menu():
    """this will print out a menu of choices so the user knows what is available."""
    while True:
          demolist = ["Apple","Banana","Cherries","Dragonfruit"]
          print("Choose a fruit: ")
          print("1.", demolist[0])
          print("2.", demolist[1])
          print("3.", demolist[2])
          print("4.", demolist[3])
          break

    while True:
        choice= input(">")

        if choice == "1":
            print("You picked apple!")
            break
        elif choice == "2":
            print("You picked banana!")
            break
        elif choice == "3":
            print("You picked cherries!")
            break
        elif choice == "4":
            print("You picked dragonfruit!")
            break
        else:
            print("That was not an option.")
            break

def sports():
    """what is a more efficient way to return this info instead of using a bunch
    of if/elif/else lines?"""

    while True:

        quitwords= ["Q", "q", "Quit", "quit", "Stop", "stop", "End", "end"]

        print("\nPick a sport to see what equipment you need!")
        print(["football", "soccer", "tennis", "baseball"])

        sport= input("\n>")

        if sport in quitwords:
            break

        if sport == "football":
            print("football, pads, helmet")
            break

        elif sport == "soccer":
            print("soccer ball, shin guards")
            break

        elif sport == "tennis":
            print("two tennis rackets, tennis ball")
            break

        elif sport == "baseball":
            print("baseball, bat, glove")
            break

        else:
            print("That is not one of the correct sports!")


def creation():
    poke_df = pd.read_csv("pokedex.txt", index_col=1)
    
    print("\n10 best attackers:")
    new_df = poke_df.sort_values(["Attack"], ascending=False)    
    print(new_df.head(10))

    print("\n10 best defenders:")
    new_df = poke_df.sort_values(["Defense"], ascending=False)              
    print(new_df.head(10))

    print("\n10 highest HP:")
    new_df = poke_df.sort_values(["HP"], ascending=False)              
    print(new_df.head(10))


def challenge():
    # HARDER THAN IT LOOKS:
    # I have a bunch of numbers that I need to increase by 1!

    nums= [5,10,15,20,25]

    # this will cause an error! how should we do this, then?
    nums[0] = nums[0] + 1
    nums[1] = nums[1] + 1
    nums[2] = nums[2] + 1
    nums[3] = nums[3] + 1
    nums[4] = nums[4] + 1
 
# menu()
# sports()
# creation()
# challenge()
```

### EXAMPLE SOLUTION

There are MANY ways you could write this code in a more concise manner. The following is just ONE example.

```python
#!/usr/bin/env python3

import pandas as pd

def menu():
    """this will print out a menu of choices so the user knows what is available."""
    while True:
        try:
            demolist = list(enumerate(["Apple","Banana","Cherries","Dragonfruit"]))
            print("Choose a fruit: ")
            for num, fruit in demolist:
                print(f"{num + 1}. {fruit}")
            choice= int(input(">"))
            print(f"You picked {demolist[choice-1][1]}!")
            break
        except:
            print("That is not a valid answer.")

def sports():
    """what is a more efficient way to return this info instead of using a bunch
    of if/elif/else lines?"""

    while True:
        sportsdict= {"football": "football, pads, helmet",
                     "soccer": "soccer ball, shin guards",
                     "tennis": "two tennis rackets, tennis ball",
                     "baseball": "baseball, bat, glove",
                     "quitwords": ["q","quit","stop","end"]
                    }

        print("\nPick a sport to see what equipment you need!")
        print([sport for sport in sportsdict.keys()])

        sport= input("\n>").lower()

        if sport in sportsdict["quitwords"]:
            break
        
        elif sport in sportsdict.keys():
            print(sportsdict[sport])
            break

        else:
            print("That is not a valid selection.")


def creation(stat):
    poke_df = pd.read_csv("pokedex.txt", index_col=1)
    
    new_df = poke_df.sort_values([stat], ascending=False)    
    print(new_df.head(10))

def challenge():
    # I have a bunch of numbers that I need to increase by 1!

    nums= [5,10,15,20,25]

    # a somewhat "janky" approach
    for x in range(len(nums)):
        nums[x-1] += 1

    print(nums)

    # a list comprehension (preferred approach)
    nums2= [num + 1 for num in nums]

    print(nums2)
 
menu()

sports()

for x in ["Attack","Defense","HP"]:
    input(f"\nPress ENTER to see the top 10 Pokemon with highest {x}:")
    creation(x)

challenge()
```
