# Code Repair! Tuesday Morning Challenge

<img src="https://miro.medium.com/max/1118/1*PzCZz2_-LIDiF0F1ZXBfiw.jpeg" width="300"/>

Time for something different- instead of writing code, we'll be repairing it. The code block below uses all the concepts we learned about yesterday- shebang, variables, methods, built-in functions, and concatenation!

1. Create a new file!

    `student@bchd:~$` `vim tuesdaychallenge.py`
    
    ```
    #!/usr/env python3

    number= 2

    name= input(What is your name?\n>)

    # This is what you should see when print runs-
    # Hi <name>! Welcome to Day 2 of Python Training!
    
    print("Hi " + name.capitalize + "! Welcome to Day " + "number" + " of Python Training!")
    ```

0. Save and quit back to your command line with `:wq`.

0. Change the permissions with the following command:

    `student@bchd:~$` `chmod u+x tuesdaychallenge.py`
    
0. Execute the script like so. **THERE WILL BE ERRORS** (that's the point!) If you don't execute it this way, you won't see every glorious error there is to fix! :)

    `student@bchd:~$` `./tuesdaychallenge.py`
    
0. As you make changes to fix the script, continue to execute the script to test it. For maximum fulfillment, try to only fix what is causing the error message before fixing anything else. The more errors you see, the more you'll learn how to fix them! Error messages are your FRIEND.

<details>
<summary>Need help? Click here to see where errors are located:</summary>
<br>
    

    #!/usr/env python3  ## INCORRECT SHEBANG

    day= 2

    name= input(What is your name?\n>) ## MISSING QUOTES

    print("Hi " + name.capitalize + "! Welcome to Day " + "number" + " of Python Training!")
                       ^                                   ^  ^
                       ^                                   ^  "quotes" makes this a string, not a variable
                       ^                                   also, can't + an integer to a string!
                       missing () at end of method

    
</details>
