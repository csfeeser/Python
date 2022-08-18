## Error Handling Review

Something that your final project should/must include are error handling tools... gotta prevent those user errors! Below is a perfectly functioning piece of code, so long as the users run it EXACTLY as instructed (which will never happen). 

#### OBJECTIVE:

- Find the comments that start with WHAT IF and do your best to add code that prevents that issue from arising.
- Make error handling/prevention for each specific issue. Don't just throw the whole thing in a try/except and call it a day :)

```python
#!/usr/bin/env python3
"""Error handling refresher!"""

def sub(x,y):
    return x-y

def mult(x,y):
    return x*y

def add(x,y):
    return x+y

def div(x,y):
    return x / y

# DID YOU KNOW you can store functions in a dictionary?
# just don't include the () at the end and they are
# an OBJECT, not a function call!
funcdict= {"+": add,
            "-": sub,
            "/": div,
            "*": mult}

def main():
    # WHAT IF a user types in something that's not a number?
    num1= input("Enter a number\n>")
    num2= input("Enter a second number\n>")

    # WHAT IF a user picks an operator that isn't + - / or *?
    ope= input("Choose an operator: + - / *\n>")

    func= funcdict[ope]

    # WHAT IF a user tries to divide by zero?
    answer= func(num1, num2)

    print(f"{num1} {ope} {num2} = {answer}")

main()
```
