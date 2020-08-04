## ENRICHMENT: Functions
### Let's get some more practice in using functions!



#### PART 1

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

1. Write a function that takes a string as an argument (ex. defmyfunction(string)). Have the function check if the string is a palindrome (a word that is the same backwards and forwards).

**HINT:** use the reverse() method!


 
            
