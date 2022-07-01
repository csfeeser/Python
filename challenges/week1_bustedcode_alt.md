# Fixing a Week's Worth of Code!

![Image description](https://c.tenor.com/2ObfdQUkkh8AAAAd/bug-fix-fixing-bugs-in-your-code.gif)

### Below is a piece of code that uses (almost) all the concepts that we covered in our first week-- let's fix it up!

`bugginout.py`

```python
#!/usr/bin/env python
import sys

# there's nothing wrong with this function, it's just some cool code!
def print1by1(text, delay=0.1):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

def name_grabber():
    # uh oh! this while loop should force the user to answer again
    # if the user DOESN'T enter a name and DOESN'T pick a number
    # between 1 and 3!
    while True:
         name= input("What is your name?\n>")
         num= input("Pick a number between 1 and 3")
         if name and num in ["1","2","3"]:
             return name, num

def main():
    num_dict= {"1":"great","2":"awesome","3":"superb"
    name, num= name_grabber() # HINT: python error tracing doesn't always get the line number correct!
         # hmm, something's missing in that open() function...
    with open("horoscope.txt") as fileobj:
        fileobj.write(f"{name}, I predict today will be {num_dict[num].upper()}!")

    # Not an error per se, but it's undesirable that
    # this gets written out with no spaces!
    # Fix the for loop to give a nicer output!
    for x in ["YOUR", "FUTURE", "HAS", "BEEN", "WRITTEN", "TO", "HOROSCOPE.TXT..."]:
        print1by1(x)
```

`student@bchd:~$` `chmod u+x bugginout.py`

`student@bchd:~$` `./bugginout.py`

### `horoscope.txt` should be in your current working directory*!

*the directory you were in when you executed the code!

<!--

## SOLUTION

```python
#!/usr/bin/env python3
import sys 
import time

# there's nothing wrong with this function, it's just some cool code!
def print1by1(text, delay=0.1):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

def name_grabber():
    # uh oh! this while loop should force the user to answer again
    # if the user DOESN'T enter a name and DOESN'T pick a number
    # between 1 and 3!
    while True:
         name= input("What is your name?\n>")
         num= input("Pick a number between 1 and 3")
         if name and num in ["1","2","3"]:
             return name, num 

def main():
    num_dict= {"1":"great","2":"awesome","3":"superb"}
    name, num= name_grabber() # HINT: python error tracing doesn't always get the line number correct!
         # hmm, something's missing in that open() function...
    with open("horoscope.txt", "w") as fileobj:
        fileobj.write(f"{name}, I predict today will be {num_dict[num].upper()}!")

    # Not an error per se, but it's undesirable that
    # this gets written out with no spaces!
    # Fix the for loop to give a nicer output!
    for x in ["YOUR", "FUTURE", "HAS", "BEEN", "WRITTEN", "TO", "HOROSCOPE.TXT..."]:
        print1by1(x + " ")

main()
```
