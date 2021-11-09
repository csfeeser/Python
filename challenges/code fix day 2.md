# Code Repair! Tuesday Morning Challenge

Time for something different- instead of writing code, we'll be repairing it. The code block below uses all the concepts we learned about yesterday- lists, dictionaries, methods, functions, built-in functions, and concatenation!

1. Create a new file!

    `student@bchd:~$` `vim tuesdaychallenge.py`
    
    ```
    #!/usr/env python3

    def main():

        mylist= [1,2,3,4,5, "Python"]

        name= input(What is your name?\n>)

        # Hi <name>! Welcome to Day 2 of Python Training!
        print("Hi " + name.capitalize + "! Welcome to Day " + mylist[1] + " of " + mylist[6] " Training!")
    ```

0. Change the permission settings.

    `student@bchd:~$` `chmod u+x tuesdaychallenge.py`
    
0. Run the script. It WILL fail!

    `student@bchd:~$` `./tuesdaychallenge.py`
    
0. As you make changes to fix the script, continue to execute the script to test it. For maximum fulfillment, try to only fix what is causing the error message before fixing anything else. The more errors you see, the more you'll learn how to fix them! Error messages are your FRIEND.
