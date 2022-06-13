## Welcome to Week 2!

Over the course of the past week, we've learned the following:

- running Python in a Linux environment
- built-in functions
- custom functions
- methods
- lists, dictionaries, strings, integers, floats, booleans
- reading/writing to files
- importing modules
- standard vs. third party modules
- if/elif/else logic
- while loops
- for loops

...and more!  

To get the blood moving this morning, take the code below and implement additional features where indicated by `#comments`!

`student@bchd:~$` `vim week2warmup.py`

```python
#!/usr/bin/env python3
"""Week 2 Morning Warmup"""

words= ["astonishing", "disgusting", "damaging", "dreadful", "amazing", "awesome", "astounding", "distressing"]

# OBJECTIVE 1: break the while loop when the user ACTUALLY types something in
while True:
  name= input("What is your name?\n>")




# NOTE: there are four a-words, so there should be four lines of output in the "monday.txt" file!

# OBJ. 2: put the correct permission argument in the open() function below
with open("monday.txt") as fileobj:

     # OBJ. 3- while indented under the with/as, loop over the "words" list above
     # OBJ. 4- add if logic to only allow words that start with the letter "a"
     # OBJ. 5- insert "name" and each "a-word" into the .write() line below.
     fileobj.write("Hello, " + "! I hope you have an " + " day today!")
```
