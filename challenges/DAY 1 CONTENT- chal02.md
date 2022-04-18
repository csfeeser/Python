# CHALLENGE: SHEBANG, INPUT, PRINT, CONCATENATE, VARIABLES

<img src="https://i.redd.it/wk843smkri441.jpg" alt="drawing" width="400"/>

**Objective:** Make the following output using the following list:

1. Include this list: 
    
    ```
    icecream= ["indentation", "spaces"] 
    ```

2. Include this list:

    ```
    ["Akino", "Bai", "Carlos", "Dalton", "Dan", "Edith", "Ethan", "Isaiah", "J", "Jessica", "John", "Justin", "Khalil", "Nikk", "Ramesh", "Scotty", "Sergio", "Shawn"]
    ```
    
3. Append the integer **(INTEGER, not string!)** `4` to the list `icecream`.

<details>
<summary>I need a hint!</summary>
<br>
    
    icecream.append(4)
</details>

4. Include an input asking for a number between 0 and 14. Use this number to identify one of the students from the *tlgstudents* list!

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

## SOLUTION including bonuses:

```python
#!/usr/bin/env python3

import random

# make our lists
icecream = ["indentation", "spaces"]
tlgstudents= ["Bryan", "Colin", "Erik", "Gregory", "John", "Kishor", "Leia", "Maria", "Monte", "Jarrad", "Pemba", "Don", "Tim", "Travis", "Trung"]

# add 4 to the icecream list
icecream.append(4)

# prompt for a number- REMEMBER, input always returns the answer as a string!
studentid= input("Enter a number from 0 - 14: ")

# MEGA BONUS SOLUTION: check whether the input was a name or a number
if studentid.isdigit():
    # if the input can be converted to an integer, do so and print the final output
    print(f"{tlgstudents[int(studentid)]} always uses {icecream[2]} {icecream[1]} to indent.")
else:
    # if it can't be converted to an integer, it must be a name.
    print(f"{studentid} always uses {icecream[2]} {icecream[1]} to indent.")


# SUPER BONUS SOLUTION:
# the random.choice() function will randomly grab an element from a list
# randomstudent is now a random string from the tlgstudents list
randomstudent= random.choice(tlgstudents)

print(f"RANDOM STUDENT {randomstudent} always uses {icecream[2]} {icecream[1]} to indent.")
```
