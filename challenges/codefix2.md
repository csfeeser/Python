# Code Repair! Tuesday Morning Challenge

<img src="https://miro.medium.com/max/1118/1*PzCZz2_-LIDiF0F1ZXBfiw.jpeg" width="300"/>

Time for something different- instead of writing code, we'll be repairing it. The code block below uses all the concepts we learned about yesterday- shebang, variables, methods, built-in functions, and concatenation!

1. Create a new file!

    `student@bchd:~$` `vim ~/mycode/tuesdaymorningchallenge.py`
    
    ```python
    #!/usr/env/python3
    
    main()
    
    def main()
        students = [
            "Amir", "Breana", "Katie", "Clayton", "Coty", "Daiyron",
            "Douglas", "Gabriel", "Jakira", "John", "Jonathan",
            "Justin", "Megan", "Tayo", "Summer", "Tomiwa"
    
        # len() function counts up how many names in the list
        headcount = len(students)
    
        str_number = input(f"Pick a number between 1 and {headcount}: ")
    
        # int() function converts a string into an integer
        int_number = int(str_number)
    
        student_choice = students[str_number]
    
        print("{student_choice} is AWESOME!")
    ```

0. Save and quit back to your command line with `:wq`.

0. Change the permissions with the following command:

    `student@bchd:~$` `chmod u+x ~/mycode/tuesdaymorningchallenge.py`
    
0. Execute the script like so. **THERE WILL BE ERRORS** (that's the point!) If you don't execute it this way, you won't see every glorious error there is to fix! :)

    `student@bchd:~$` `/home/student/mycode/tuesdaymorningchallenge.py`
    
0. As you make changes to fix the script, continue to execute the script to test it. For maximum fulfillment, try to only fix what is causing the error message before fixing anything else. The more errors you see, the more you'll learn how to fix them! Error messages are your FRIEND.

<details>
<summary>Need help? Click here to see where errors are located:</summary>
<br>
    
```python
#!/usr/env/python3
# ^^ incorrect shebang line!

main() # call functions AFTER you define them!

def main() # missing a colon
    students = [
        "Amir", "Breana", "Katie", "Clayton", "Coty", "Daiyron",
        "Douglas", "Gabriel", "Jakira", "John", "Jonathan",
        "Justin", "Megan", "Tayo", "Summer", "Tomiwa"
              # missing a closing bracket!
              
    headcount = len(students)

    str_number = input(f"Pick a number between 1 and {headcount}: ")

    int_number = int(str_number)

                                # you can't slice lists with strings!
    student_choice = students[str_number]
                                # ...what happens if you pick "16"? how can that be fixed?
                                
    # f strings need an f in front of the first "quotation mark"
    print("{student_choice} is AWESOME!")
```
    
</details>


### SOLUTION

<details>
<summary>Click here to see the fixed script!</summary>
<br>
    
```python
#!/usr/bin/env/python3

def main():
    students = [
        "Amir", "Breana", "Katie", "Clayton", "Coty", "Daiyron",
        "Douglas", "Gabriel", "Jakira", "John", "Jonathan",
        "Justin", "Megan", "Tayo", "Summer", "Tomiwa"
               ]

    headcount = len(students)

    str_number = input(f"Pick a number between 1 and {headcount}: ")

    int_number = int(str_number) - 1

    student_choice = students[int_number]

    print(f"{student_choice} is AWESOME!")

main()
```

</details>
