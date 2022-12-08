# MORNING WARM-UP

The script below is busted. Do your best to fix it, then test it vigorously! You are not required to IMPROVE the script, just make it work "as advertised!"

`student@bchd:~$` `vim bustedcode.py`

```python
#!/usr/bin/env python3
# A program that prompts a user for two operators and operation (plus or minus)
# the program then shows the result.
# The user may enter q to exit the program.

def calculator()
        print("\nWhat is the first operator?")
        calc1 = raw_input()
        calc1 = float(calc1)
        print("\nWhat is the second operator? Or, enter q to quit: ")
        calc2 = raw_input()
        calc2 = float(calc2)
        print("Enter an operation to perform on the two operators (+ or -): ")
        operation = raw_input()
        if operation == "+":
            add(calc1,calc2)
        ifel operation == '-':
            sub(calc1,calc2)
        else:
            print("\n Not a valid entry.")

main()

def add(num1,num2):
    print(\n + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
    
def sub():
    print("\n" + str(num1) + " - " + str(num2) + " = " + str(num1 - num2))
    
```

`student@bchd:~$` `python3 bustedcode.py`
