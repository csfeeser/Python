# WHILE LOOPS, IF/ELIF/ELSE

Below is a script for a number guessing game! However, it could certainly be improved. Try and add the following two features:

1. Only let the user have FIVE chances to guess the correct answer!

2. Add error handling so that if the user types in something that isn't a number, it doesn't error out the script!

```python
#!/usr/bin/env python3
"""Number guessing game!"""

import random

def main():
    num= random.randint(1,100)

    while True:
        guess= int(input("Guess a number between 1 and 100"))

        if guess > num:
            print("Too high!")

        elif guess < num:
            print("Too low!")

        else:
            print("Correct!")
            break

main()
```
