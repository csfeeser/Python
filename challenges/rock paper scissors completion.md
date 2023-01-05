<img src="https://i.kym-cdn.com/photos/images/facebook/001/680/636/590.jpg" alt="drawing" width="500"/>

---
# Rock Paper Scissors!

### Below is the beginning of a script for a "Rock Paper Scissors" game! However, it's incomplete... please try and get it operational!

When working properly, the user should be able to type in rock, paper, or scissors and be told if they won or lost!

**BONUS**- make the script "user-proof"; meaning if the user types in something wrong it won't cause an error, it will just end the game!

**ROCKET SCIENTIST BONUS**- Play multiple times... the winner is the one who scores 2 out of 3 games!

```python
# computer needs to make a choice
# choices need to be evaluated
# print out the result (who won)

def main():
    """body of the game"""
    
    choice= input("Rock, Paper, or Scissors?\n>")
    botchoice= random.choice(["rock", "paper", "scissors"])

    choice= choice.lower() # validates input by forcing input to be lower case

    # uncomment these print functions to debug
    #print(choice)
    #print(botchoice)

    if choice not in ["rock", "paper", "scissors"]:
        print("You entered an invalid choice, you lose(r)!")

    elif choice == "scissors" and botchoice == "paper":
        print("You win!")
    # user picked scissors... did they win or lose?

    ### ADD MORE HERE

main()
```
