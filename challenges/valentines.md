# Fixing Code!

![Image description](https://i.etsystatic.com/32087542/r/il/2e7185/3649549023/il_340x270.3649549023_muqz.jpg)

### Below is a piece of code that uses (almost) all the concepts that we covered in our training so far-- let's fix it up!

`student@bchd:~$` `vim bugginout.py`

```python
#1/usr/bin/python3
"""Just a lil' warmup!""

name= input(What is your name?\n>)
num= input("Pick a number between 1 and 3\n>")
num= num - 1

adj_list= ["stupendous","splendiferous","magnificent"]
adj= adj_list[num]

# these prints are for debugging purposes, you may delete them when you're ready
print(name)
print(adj)

# FINAL PART OF CHALLENGE:
# USE THE name AND adj VARIABLES TO PRINT THE FOLLOWING:
# "Hello <name>! Have a <adj> Valentine's Day!
```

`student@bchd:~$` `chmod u+x bugginout.py`

`student@bchd:~$` `./bugginout.py`
