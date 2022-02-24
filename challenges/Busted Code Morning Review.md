# Code Repair Challenge!

Time for something different- instead of writing code, we'll be repairing it. The code block below uses all the concepts we learned about yesterday- lists, dictionaries, methods, functions, built-in functions, and concatenation!

1. Create a new file!

    `student@bchd:~$` `vim bustedchallenge.py`
    
    ```
    #!/usr/env python3

    def main():

        words= {1: "great",
                2: "awesome",
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

0. Change the permission settings.

    `student@bchd:~$` `chmod u+x bustedchallenge.py`
    
0. Run the script. It WILL fail!

    `student@bchd:~$` `./bustedchallenge.py`
    
0. As you make changes to fix the script, continue to execute the script to test it. For maximum fulfillment, try to only fix what is causing the error message before fixing anything else. The more errors you see, the more you'll learn how to fix them! Error messages are your FRIEND.
