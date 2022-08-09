### Busted Numbers Game!

<img src="https://www.codesnail.com/wp-content/uploads/2020/08/guess-the-number-game-in-python.png" alt="drawing" width="500"/>


Below is a script for a number guessing game! However, it's busted! Please try and get it operational (no need to improve it, just make it work).

When working properly, the user should have **5 chances** to guess a number that is between 1 and 100. The program will tell the user if they guess too high or too low, and if they guess correctly the script should end!

```python
#!/usr/bin/env python3
"""Number guessing game! User has 5 chances to guess a number between 1 and 100!"""

def main():
    num= random.randint(1,100)
    
    rounds= 0
    
    while rounds < 5 and guess != num:
        guess= input("Guess a number between 1 and 100\n>")
        
        # COOL CODE ALERT: what is the purpose of the next four lines?
        if guess.isdigit():
            guess= int(guess)
        else:
            continue

        if guess > num:
            print("Too high!")
            rounds + 1

        if guess < num:
            print("Too low!")
            rounds + 1

        else:
            print("Correct!")
```


### SOLUTION

```python
#!/usr/bin/env python3
"""Number guessing game! User has 5 chances to guess a number between 1 and 100!"""
import random

def main():
    num= random.randint(1,100)
    
    guess= ""
    rounds= 0
    
    while rounds < 5 and guess != num:
        guess= input("Guess a number between 1 and 100\n>")
        
        # COOL CODE ALERT: what is the purpose of the next fourlines?
        if guess.isdigit():
            guess= int(guess)
        else:
            continue

        if guess > num:
            print("Too high!")
            rounds += 1

        elif guess < num:
            print("Too low!")
            rounds += 1

        else:
            print("Correct!")

main()
```
