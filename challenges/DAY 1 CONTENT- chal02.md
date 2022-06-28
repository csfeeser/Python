# EXERCISE: LISTS, INPUT, PRINT, CONCATENATE, VARIABLES

<img src="https://i.redd.it/wk843smkri441.jpg" alt="drawing" width="400"/>

**Objective:** Add the following components to your code in this order:

**PART 1.** Put this list in your code:   

```python
wordbank= ["indentation", "spaces"] 
```

**PART 2.** Put this list in your code:   

```python
tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]
```
    
**PART 3.** Add a line of code that appends the integer `4` to the list `wordbank`.

<details>
<summary>I need a hint!</summary>
<br>
    
    wordbank.append(4)
</details>

**PART 4.** Include an input asking for a number between 0 and 19. Save this as the variable `num`.

<details>
<summary>I need a hint!</summary>
<br>
    
    num= input("Pick a student number!")
</details>

**PART 5.** Remember that *input()* always returns a string... convert `num` into an integer!

<details>
<summary>I need another hint!</summary>
<br>
    
    num= int(input("Pick a student number!"))
</details>

**PART 5.** Use the integer `num` to slice one of the elements from the list `tlgstudents`. Save the name you return as the variable `student_name`.

<details>
<summary>MOAR HINTZ!</summary>
<br>
    
    choice= int(input("Pick a student number!"))
    student_name= tlgstudents[choice]
</details>

**PART 6.** Using elements from the `tlgstudents` list and the `student_name` string, print this output.

```
<student_name> always uses <4> <spaces> to indent.
```
> "4" and "spaces" should come from tlgstudents!

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

wordbank= ["indentation", "spaces"]

tlgstudents= ["Cat", "Chris", "Dao", "David", "Henwin", "Herman", "Jose", "Justin", "Kris", "Mannie", "Marcos", "Marshall", "Michael", "Mike", "Nikko", "Phil", "Ryan", "Sachin", "Samekh", "Will"]

# this will add the integer 4 to the wordbank list
wordbank.append(4)

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
print(f"{name} always uses {wordbank[2]} {wordbank[1]} to indent.")
```
-->
