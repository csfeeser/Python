### Busted Numbers Game!

Below is a script for a number guessing game! However, it's busted! Please try and get it operational (no need to improve it, just make it work).

1. Only let the user have FIVE chances to guess the correct answer!

2. Add error handling so that if the user types in something that isn't a number, it doesn't error out the script!

```python
#!/usr/bin/env python3
"""Number guessing game! User has 5 chances to guess a number between 1 and 100!"""

def main():
    num= random.randint(1,100)
    
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
            rounds + 1

        if guess < num:
            print("Too low!")
            rounds + 1

        else:
            print("Correct!")
```
