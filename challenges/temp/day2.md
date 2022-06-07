## Day 2 Warmup!

<img src="https://pbs.twimg.com/media/Ei1-My3UMAAwJ4a.jpg" alt="drawing" width="300"/>

Open a new file named `day2warmup.py`

`student@bchd:~$` `vim day2warmup.py`

Put the following into your file:

```python
#!/usr/bin/python

#heroes= ["Spiderman", "Batman", "Black Panther", "Wonder Woman", "Storm"]

# PART 1
# Print out your favorite character from this list! The output would look something like:
# My favorite character is Black Panther!


# PART 2
# Ask the user to pick a number between 1 and 100.
# Convert the input into an integer.


nums= [1, -5, 56, 987, 0]

# PART 3
# check out https://docs.python.org/3/library/functions.html or go to Google
# use a built-in function to find which integer in nums is the biggest.
# then, print out that number!


# PART 4
# put ALL of this code inside a function!
# look at lab 11, step 4 for an example!
```

Save and quit (`:wq`)

Add execute permission.

`student@bchd:~$` `chmod u+x day2warmup.py`

Now run the script!

`student@bchd:~$` `./day2warmup.py`

OOPS, AN ERROR
```
-bash: ./day2warmup.py: /usr/bin/python: bad interpreter: No such file or directory
```

Something is wrong with the shebang line! You'll need to fix it before you can test run your code :)
