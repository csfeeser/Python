# CHALLENGE: SHEBANG, INPUT, PRINT, CONCATENATE, VARIABLES

<img src="https://i.redd.it/i0imk0ay05k21.jpg" alt="drawing" width="400"/>

**Objective:** Make the following output using the following list:

1. Include this list: 
    
    ```
    icecream= ["indentation", "spaces"] 
    ```

2. Include this list:

    ```
    tlgstudents= ["Aaron","Alex","Alonzo","Brandon","Chris","Francisco","James","Jonathan","Lillian","Manuel","Patrick","Robert","Ryan","Troy","Wes","Henry","Yalined"]
    ```
    
3. Append the integer **(not string!)** `4` to the list `icecream`.

<details>
<summary>I need a hint!</summary>
<br>
    
    icecream.append(4)
</details>

4. Include an input asking for a number between 0 and 5. Use this number to identify one of the students from the *tlgstudents* list!

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
