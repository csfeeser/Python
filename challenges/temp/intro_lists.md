# EXERCISE: LISTS, INPUT, PRINT, CONCATENATE, VARIABLES

<img src="https://i.redd.it/wk843smkri441.jpg" alt="drawing" width="400"/>

**Objective:** Add the following components to your code in this order:

**PART 1.** Put this list in your code:   

```python
wordbank= ["indentation", "spaces"] 
```

**PART 2.** Put this list in your code:   

```python
tlgstudents= ["Aaron", "Casey", "Donny", "Emmanuel", "Eric", "Jaelen", "James", "Jay", "John", "Ken", "Maurice", "Mike", "Ryan", "Shamain", "Tuang", "Tyler", "Zhenqian", "Travis"]
```
  
**PART 3.** Include an input asking for a number between 0 and 19. Save this as the variable `num`.

<details>
<summary>I need a hint!</summary>
<br>
    
    num= input("Pick a student number!")
</details>

**PART 4.** Remember that *input()* always returns a string... convert `num` into an integer!

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

**ROCKET SCIENTIST BONUS**

Find a way to randomize what student is picked!

**BRAIN SURGEON BONUS**

If the user types in a name instead of a number, use the name instead!
