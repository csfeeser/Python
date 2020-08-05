## ENRICHMENT: Functions
### Let's get some more practice in using functions!



#### PART 1

**DID YOU KNOW** you can indent whole blocks of lines in vim! It's true!

- When inside vim, press <kbd>escape</kbd> to get into command mode.
- Move your cursor to the top line of the block you wish to indent.
- Press <kbd>shift</kbd> + <kbd>v</kbd> to enter `-- VISUAL LINE --` mode (you'll see it in the bottom left)
- Press the <kbd>down</kbd> button and highlight all those lines you want to indent.
- With your block highlighted, press <kbd>shift</kbd> + <kbd>></kbd> to bump all those lines to the right!
- You can now slap a function definition at the top and a function call at the bottom! Done!

1. Take this code and convert it into a function!

       x= float(input("How would you rank your day today on a scale of 1-10?"))
       if x == 10:
           print("Attaboy! Stay positive!")
       elif x >= 8:
           print("Sounds lovely! Keep on truckin'!")
       elif x >= 6:
           print("Chin up, buttercup!")                    
       elif x >= 4:            
           print("I recommend some hot chocolate and a hug, maybe...")               
       elif x >= 2:
           print("Dude, are you ok?")                   
       else:
           print("Geez!!! You might as well just go back to bed!")
            
#### PART 2

1. Below is a static function- it will only execute the code that's inside it exactly as written. Rewrite the function so that it accepts arguments to take the place of x and y instead. **You may not use input() inside the function!**

       def python_props():
           x= "fun"
           y= "useful"
           print(f"Python is {x} and {y}!")

       python_props()

#### PART 3

1. Write a function that takes a string and applies the Spongebob Sarcasm Font to it (randomly capitalize letters). The string must be taken as an argument (ex. defmyfunction(string)). **You may not use input() inside the function!**

**You may Google for the solution if you don't feel like figuring out how to randomly capitalize... there is no method that does this.**

![Image description](https://github.com/csfeeser/TLG-Python/blob/master/enrichment/Spongebob-memes.jpg?raw=true)


 
            
