# Reducing Code Length with Functions

Functions! They are awesome. And necessary. You'll never be an effective programmer if you can't make your code efficient, effective, readable, and repeatable by using functions. However, it's possible to get carried away a bit. Happens to all of us :)

Below is a working calculator script... however, it's a tad on the lengthy side. Your goal is to SHORTEN this script WITHOUT sacrificing any of its utility.

```python
#!/usr/bin/env python3

def add(x, y):
    answer = x + y
    print(answer)

def subtract(x, y):
    answer = x - y
    print(answer)

def divide(x, y):
    answer = x / y
    print(answer)

def multiply(x, y):
    answer = x * y
    print(answer)

def main():
    while True:
        try:
            x = float(input("Enter in a number: "))
            y= float(input("Enter ANOTHER  number: "))
            break
        except:
            print("Invalid input, try again.")

    operation = ""
    while(operation != "add" and operation != "subtract" and operation != "divide" and operation != "multiply"):
        operation = input("What operation would like to perform? OPTIONS: 'add', 'subtract','divide','multiply': ").lower()

    if(operation == "add"):
        add(x, y)
    elif(operation == "subtract"):
        subtract(x, y)
    elif(operation == "divide"):
        if y != 0:
            divide(x, y)
        else:
            print("You can't divide by zero!")
    elif(operation == "multiply"):
        multiply(x, y)
    else:
        print("use a valid OPTION")

if __name__ == "__main__":
    main()
```
