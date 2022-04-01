# Morning Challenge:

The code below is broken! It's up to you to fix it. Scroll all the way to the bottom of the document to see how you can easily copy this code into your machine.

```
#!/usr/bin/env python3

import PySimpleGUI as sg
from sympy import *

# ########GLOBAL VARIABLES##########
welcomeMessage = "Welcome to my python-based calculator!"
operators = ["^", "√", "÷", "*", "+", "-"]
implicitMultiply = ["LOG", "LN", "SIN", "COS", "TAN", "("]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
history = []

column1 = [
    [sg.Button(button_text="LOG", size=(5, 1))],
    [sg.Button(button_text="LN", size=(5, 1))],
    [sg.Button(button_text=pretty(pi), size=(5, 1))],
    [sg.Button(button_text="^", size=(5, 1))],
    [sg.Button(button_text="DEL", size=(5, 1))],
    [sg.Button(button_text="OFF", size=(5, 1))]
]

column2 = [
    [sg.Button(button_text="SIN", size=(5, 1))],
    [sg.Button(button_text="√", size=(5, 1))],
    [sg.Button(button_text="7", size=(5, 1), button_color=('#12100E', 'white'))],
    [sg.Button(button_text="4", size=(5, 1), button_color=('#12100E', 'white'))],
    [sg.Button(button_text="1", size=(5, 1), button_color=('#12100E', 'white'))],
    [sg.Button(button_text="0", size=(5, 1), button_color=('#12100E', 'white'))]
]

column3 = [
    [sg.Button(button_text="COS", size=(5, 1))],
    [sg.Button(button_text="(", size=(5, 1))],
    [sg.Button(button_text="8", size=(5, 1), button_color=('#12100E', 'white'))],
    [sg.Button(button_text="5", size=(5, 1), button_color=('#12100E', 'white'))],
    [sg.Button(button_text="2", size=(5, 1), button_color=('#12100E', 'white'))],
    [sg.Button(button_text=".", size=(5, 1), button_color=('#12100E', 'white'))]
]

column4 = [
    [sg.Button(button_text="TAN", size=(5, 1))],
    [sg.Button(button_text=")", size=(5, 1))],
    [sg.Button(button_text="9", size=(5, 1), button_color=('#12100E', 'white'))],
    [sg.Button(button_text="6", size=(5, 1), button_color=('#12100E', 'white'))],
    [sg.Button(button_text="3", size=(5, 1), button_color=('#12100E', 'white'))],
    [sg.Button(button_text="(-)", size=(5, 1), button_color=('#12100E', 'white'))]
]

column5 = [
    [sg.Button(button_text="CLEAR", size=(5, 1))],
    [sg.Button(button_text="÷", size=(5, 1), button_color=('white', '#3A3E5C'))],
    [sg.Button(button_text="*", size=(5, 1), button_color=('white', '#3A3E5C'))],
    [sg.Button(button_text="+", size=(5, 1), button_color=('white', '#3A3E5C'))],
    [sg.Button(button_text="-", size=(5, 1), button_color=('white', '#3A3E5C'))],
    [sg.Button(button_text="=", size=(5, 1), button_color=('white', '#3A3E5C'))]
]

layout = [
    [sg.Output(size=(47, 5), key='-DISPLAY-', echo_stdout_stderr=True)],
    [sg.Column(column1),
     sg.VSeperator(pad=(1, 1)),
     sg.Column(column2),
     sg.VSeperator(pad=(1, 1)),
     sg.Column(column3),
     sg.VSeperator(pad=(1, 1)),
     sg.Column(column4),
     sg.VSeperator(pad=(1, 1)),
     sg.Column(column5)]
]


# ########MAIN FUNCTION##########
def main():
    global history

    # Create the window
    window = sg.Window('Scientific Calculator', layout, no_titlebar=True, grab_anywhere=True)
    print(welcomeMessage)
    equation = []

    # Create an event loop
    while True:
        event, values = window.read()

        if event == "OFF" or event == sg.WIN_CLOSED:
            break
        elif event == "CLEAR":
            window['-DISPLAY-'].update('')
            equation = []
        elif event == "DEL":
            output = window['-DISPLAY-'].Get()
            window['-DISPLAY-'].update('')
            print(output[0:-2], end="")
            del equation[-1]
        elif event == "=":
            if parenthesesChecker(equation):
                answer = calculate(equation)
                print(f"= {answer}")
                history.append(answer)
                equation = []
            else:
                print("ERROR: missing parenthesis!")
        else:
            if event == "LOG" or event == "LN" or event == "SIN" or event == "COS" or event == "TAN" or event == "√":
                print(event.lower() + "(", end="")
            else:
                if event in operators and event != "√" and len(equation) == 0:
                    if len(history) == 0:
                        print("ERROR: no previous history. Cannot perform operation on empty value.")
                    else:
                        equation.append(history[-1])
                        print("ANS", end="")
                print(event, end="")
            if len(equation) != 0 and equation[-1][-1] in numbers and event in numbers:
                equation[-1] += event
            else:
                equation.append(event)

    window.close()


# ########ACCESSORY FUNCTION##########
def parenthesesChecker(equation):
    stack = []

    for element in equation:
        if element in implicitMultiply or element == "√":
            stack.append(1)
        if element == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return True


def calculate(equation):
    subEq = []
    current = []
    subPar = 0
    tracking = False

    if len(equation) == 0:
        return 0

    track = 0
    for el in equation:
        # print(current)
        # if el not in operators:
        #     if track != len(equation) - 1 and equation[track + 1] in implicitMultiply:
        #         current.append("*")
        if tracking and el == ")" and subPar == 0:
            tracking = False
            if len(subEq) != 0:
                # print(current)
                current.append(funcCalc(equation[track - 2], calculate(subEq)))
                subEq = []
        elif tracking:
            if el in implicitMultiply:
                subPar += 1
            if el == ")":
                subPar -= 1
            subEq.append(el)
        elif el in implicitMultiply:
            tracking = True
        else:
            current.append(el)
        track += 1
        #print(current)
    # print(current)
    endNotReached = True
    while endNotReached:
        for item in range(len(current)):
            if current[item] == "^":
                current[item - 1] = performOperation(float(current[item - 1]), float(current[item + 1]), current[item])
                del current[item + 1]
                del current[item]
                break
            if current[item] == "√":
                current[item] = performOperation(float(current[item + 1]), 0, current[item])
                del current[item + 2]
                del current[item + 1]
                break
            if item == len(current) - 1:
                endNotReached = False
                break

    endNotReached = True
    while endNotReached:
        for item in range(len(current)):
            if current[item] == "*" or current[item] == "÷":
                current[item - 1] = performOperation(float(current[item - 1]), float(current[item + 1]), current[item])
                del current[item + 1]
                del current[item]
                break
            if item == len(current) - 1:
                endNotReached = False
                break

    endNotReached = True
    while endNotReached:
        for item in range(len(current)):
            if current[item] == "+" or current[item] == "-":
                current[item - 1] = performOperation(float(current[item - 1]), float(current[item + 1]), current[item])
                del current[item + 1]
                del current[item]
                break
            if item == len(current) - 1:
                endNotReached = False
                break

    if len(current) != 1:
        print(f"Current answer array length: {len(current)}")
        return "INTERNAL ERROR: Improper calculation."
    else:
        return float(current[0])


def funcCalc(func, value):
    if func == "(":
        return value
    elif func == "LOG":
        return log(value)
    elif func == "LN":
        return ln(value)
    elif func == "SIN":
        return sin(value)
    elif func == "COS":
        return cos(value)
    elif func == "TAN":
        return tan(value)
    else:
        print(f"ERROR: unrecognized function: {func}. Returning 0.")
        return 0


def performOperation(num1, num2, op):
    if op == "^":
        return exp(num1, num2)
    elif op == "√":
        return exp(num1, 1 / 2)
    elif op == "+":
        return add(num1, num2)
    elif op == "-":
        return add(num1, -num2)
    elif op == "*":
        return multiply(num1, num2)
    else:
        return multiply(num1, 1 / num2)


def exp(base, power):
    return base ** power


def add(first, second):
    return first + second


def multiply(first, second):
    return first * second


# Call the main function
if __name__ == "__main__":
    main()
```

<details>
<summary>Click here for the download link</summary>
<br>
APRIL FOOLS!!! Here's the link to the real challenge! https://github.com/csfeeser/Python/blob/master/challenges/Fizzbuzz%20Read%20in%20File.md
</details>
