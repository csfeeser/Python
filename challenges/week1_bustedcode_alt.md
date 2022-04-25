# Fixing a Week's Worth of Code!

![Image description](https://c.tenor.com/jhsh9h45xYAAAAAM/fix-bug-when-i-try-to-fix-a-bug.gif)

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
    # python errors try their best, but they don't always get the line
    # number right where the error occurred!
    name, num= name_grabber()
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
### SOLUTION

```python
#!/usr/bin/env python3
import sys
# you can't use a module's functions/classes/whatever
# unless you import it!!!
import time

# there's nothing wrong with this function, it's just some cool code!
def print1by1(text, delay=0.1):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

def name_grabber():
    name= input("What is your name?\n>")
    num= input("Pick a number between 1 and 3")
    if num in ["1","2","3"]:
                 return name, num

def main():
    num_dict= {"1":"great","2":"awesome","3":"superb"}
    name, num= name_grabber()
             # when opening files;
             # if you don't specify a permission
             # the default will be r, READ
    with open("horoscope.txt", "w") as fileobj:
        fileobj.write(f"{name}, I predict today will be {num_dict[num].upper()}!")

    # not an error per se, but it's undesirable that
    # this gets written out with no spaces
    # fix the for loop to give a nicer output!
    for x in ["YOUR", "FUTURE", "HAS", "BEEN", "WRITTEN", "TO", "HOROSCOPE.TXT..."]:
        # use for loop to return each string in this list
        # PLUS a whitespace to be printed out one character at a time
        print1by1(f"{x} ")

if __name__ == "__main__":
    # gotta call main to start off the whole thing
    main()
```
-->
