# Code Repair Challenge!

Time for something different- instead of writing code, we'll be repairing it. The code block below uses all the concepts we learned about yesterday- lists, dictionaries, methods, functions, built-in functions, and concatenation!

1. Create a new file!

    `student@bchd:~$` `vim bustedchallenge.py`
    
    ```
    #!/usr/env python3

    def main():

        nums= [1,2,3,4,5]
        words= {"verb": "sprint",
                "adjective": "awesome",
                "noun": "Python"

        name= input(What is your name?\n>)

        # Hi <name>! Welcome to Day 2 of Python Training!
        print("Hi " + name.capitalize + "! Welcome to Day " + nums[1] + " of " + words[noun] + " Training!")
    ```

0. Change the permission settings.

    `student@bchd:~$` `chmod u+x bustedchallenge.py`
    
0. Run the script. It WILL fail!

    `student@bchd:~$` `./bustedchallenge.py`
    
0. As you make changes to fix the script, continue to execute the script to test it. For maximum fulfillment, try to only fix what is causing the error message before fixing anything else. The more errors you see, the more you'll learn how to fix them! Error messages are your FRIEND.
