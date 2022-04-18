# EXERCISE: LISTS, INPUT, PRINT, CONCATENATE, VARIABLES

<img src="https://i.redd.it/wk843smkri441.jpg" alt="drawing" width="400"/>

**Objective:** Make the following output using the following list:

1. Include this list: 
    
    ```
    icecream= ["indentation", "spaces"] 
    ```

2. Include this list:

    ```
    tlgstudents= ["Akino", "Bai", "Carlos", "Dalton", "Dan", "Edith", "Ethan", "Isaiah", "J", "Jessica", "John", "Justin", "Khalil", "Nikk", "Ramesh", "Scotty", "Sergio", "Shawn"]
    ```
    
3. Append the integer **(INTEGER, not string!)** `4` to the list `icecream`.

<details>
<summary>I need a hint!</summary>
<br>
    
    icecream.append(4)
</details>

4. Include an input asking for a number between 0 and 17. Use this number to identify one of the students from the *tlgstudents* list!

<details>
<summary>I need a hint!</summary>
<br>
    
    choice= input("Pick a student number!")
    
**Remember that *input()* always returns a string... look at the *int()* built-in function!**
</details>

<details>
<summary>I need another hint!</summary>
<br>
    
    choice= int(input("Pick a student number!"))
</details>

<details>
<summary>MOAR HINTZ!</summary>
<br>
    
    choice= int(input("Pick a student number!"))
    student_name= tlgstudents[choice]
</details>

5. Using the appended list and the input, make this output (emphasis placed):

   ```
   <student_name> always uses <4> <spaces> to indent.
   ```

**SUPER BONUS**

Find a way to randomize what student is picked!

**MEGA BONUS**

If the user types in a name instead of a number, use the name instead!

<!--
## SOLUTION including bonuses:

```python
# the choice() function from the random module
# will choose a random element from a list
from random import choice

icecream= ["indentation", "spaces"]

tlgstudents= ["Akino", "Bai", "Carlos", "Dalton", "Dan", "Edith", "Ethan", "Isaiah", "J", "Jessica", "John", "Justin", "Khalil", "Nikk", "Ramesh", "Scotty", "Sergio", "Shawn"]

# this will add the integer 4 to the icecream list
icecream.append(4)

# using """three quotes""" creates a multi-line doc string
# in other words, a string that uses line breaks instead of /n
print("""Do one of the following:
        - Enter a number between 0 and 17
        - Type in a student's name
        - Type in the word 'random'""")

# save the user's input as the variable "choice"
choice= input(">")

# if the number entered by the user can be
# cleanly converted to an integer:
if choice.isdigit():
    # convert string to integer and slice the list
    # save the returned name as "name"
    name= tlgstudents[int(choice)]

# if the name chosen is actually in the list of students:
elif choice in tlgstudents:
    # assign that name as the variable "name"
    name= choice

else:
    # if none of the above is true, use the choice()
    # function to grab a random name and save it as "name"
    name= random.choice(tlgstudents)

# Use an f-string to neatly combine these elements into a sentence.
print(f"{name} always uses {icecream[2]} {icecream[1]} to indent.")
```
