# Morning Warmup! Fixing Broken Code!

![ok](https://github.com/user-attachments/assets/a781e1f4-420c-43ea-9651-6541582d3d37)

> OH NO! A broken python! 😨

The script below is busted. Do your best to fix it, then test it vigorously! You are not required to IMPROVE the script, just make it work "as advertised!"

Here is a new function you MIGHT need (depending on how you fix this up)- [int()](https://www.w3schools.com/python/ref_func_int.asp)
Also just a reminder, the `input()` function returns **STRINGS**, no matter what the user inputs!

`student@bchd:~$` `vim bustedcode.py`

```python
#!/usr/bin/env python3

def calculator()
   num1= input(Enter your first number: )
   num2= input(Enter your second number: )
   print("{num1} + {num2} = {num1 + num2}")
```

`student@bchd:~$` `python3 bustedcode.py`

When you are finished, type `live gtg` at your command line!

`student@bchd:~$` `live gtg`

<details>
  <summary>Click here for the solution!</summary>

```python
#!/usr/bin/env python3

def calculator():  # Added colon to function definition
    num1 = int(input("Enter your first number: "))   # Added missing quotation marks and converted input to int
    num2 = int(input("Enter your second number: "))  # Added missing quotation marks and converted input to int
    print(f"{num1} + {num2} = {num1 + num2}")        # Fixed f-string formatting for proper variable substitution

calculator()  # Added function call to execute the calculator
```

</details>
