### Morning Challenge!

<img src="https://pics.me.me/guys-i-need-a-network-specialist-with-some-python-experience%E2%80%A6-69711252.png" width="300"/>

Create a python script that contains the following function:

```python
def multilineinput():
    print("Please paste your multi-line input.\n"
          "To end, press ctrl+d on Linux/Mac, ctrl+z on Windows")
    lines = []
    try:
        while True:
            lines.append(input())
    except EOFError:
        pass
    return lines
```

When executed, this code will allow you to paste in multiple lines at once, which you can also do multiple times! When you've finished pasting, press `ctrl d` to continue. The code will return each line pasted as an element in a list.

#### OBJECTIVE:

Use the function above in addition to your own code that you will write. Your code should do the following:
- allow users to paste in a list of servers
- return the list from the function
- use a for loop over the list of servers and execute an `nslookup` command (or other command of your choice) against each. *Hint: try the os.system() function from lab 22!*
