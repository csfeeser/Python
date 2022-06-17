## SOLUTION: Playing sound in the background

***SCENARIO:*** You want two things to happen; your code running as normal WHILE sound plays in the background throughout!

The following code uses **THREADING**. Threading allows (essentially) your code to do *two things (or more) at once*- in this case, one thread runs the timer and the other thread accepts input from the user.

Read more about threading here! https://realpython.com/intro-to-python-threading/

Install the `playsound` module to use this code!

`python3 -m pip install playsound`

## IMPORTANT NOTE: Your Alta3 BCHD machine does not support sound or graphics. To use this, you'll need to run it on your personal machine.

```python
import threading
from playsound import playsound

def music():
    playsound('/path/to/a/sound/file/you/want/to/play.mp3')

sound_thread = threading.Thread(target=music, args=(1,))
sound_thread.start()

input("Sound should now be playing and look! You're typing in an input while doing so! Press ENTER!")
print("Your code will continue to run while music plays, and music will stop when the code stops.")
```
