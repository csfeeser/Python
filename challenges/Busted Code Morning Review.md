# Code Repair Challenge!

For this challenge, instead of writing code we'll be repairing it. The code block below uses concepts we've already learned- lists, dictionaries, methods, functions, built-in functions, and concatenation!

1. Create a new file!

    `student@bchd:~$` `vim bustedchallenge.py`
    
    ```
    #!/usr/env python3

    def main():

        words= {1: "great",
                2: "fabulous",
                3: "super"}

        while true
            name= input(What is your name?\n>)
            num= input("Pick a number between 1 and 3: ")
            
            if name and num in words.keys():
                # Hi <name>! Welcome to Day 2 of Python Training!
                print("Hi " + name.capitalize + "! Have a " + words[num] + " day!")
                brake
            else:
              print("Come on, follow directions. Try again.")
              continue
              # the continue keyword skips over any remaining code and goes back to
              # the beginning of the while loop!
    ```
   
0. As you make changes to fix the script, continue to execute the script to test it. The more errors you see, the more you'll learn how to fix them! Error messages are your FRIEND.


## SOLUTION

```python
#!/usr/bin/env python3

def main():

    words= {1: "great",
            2: "fabulous",
            3: "super"}

    while True:
        name= input('What is your name?\n>')
        num= int(input("Pick a number between 1 and 3: "))

        # input saves the returned value as a STRING
        # num = "2"

        if name and num in words.keys():
        # if the var name has a value
        # if num is one of the keys in the dict words
            # Hi <name>! Welcome to Day 2 of Python Training!
            print("Hi " + name.capitalize() + "! Have a " + words[num] + " day!")
            break
        else:
          print("Come on, follow directions. Try again.")
          continue
          # the continue keyword skips over any remaining code and goes back to
          # the beginning of the while loop!

main()
```
