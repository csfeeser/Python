## SOLUTION: Input During Timer

***SCENARIO:*** You want two things to happen; a timer is counting down, and if the timer reaches zero, the script ends. HOWEVER, if the user can type in some special command, the death-timer is broken :)

The following code uses **THREADING**. Threading allows (essentially) your code to do *two things (or more) at once*- in this case, one thread runs the timer and the other thread accepts input from the user.

Read more about threading here! https://realpython.com/intro-to-python-threading/

```python
import threading
import os

def decision():
    print("You took too long! The zombie ate your brains!")
    os._exit(os.EX_OK)
    # os._exit will FORCE the program to end!

S = threading.Timer(3.0, decision)
  # What does the above line mean?
  # threading.Timer is a class object- how it works depends on the two arguments provided:
  # arg 1 (10.0) is the number of seconds until a function is called0
  # arg 2 (decision) is the function that will be called in 10.0 seconds

S.start()
  # this line STARTS the separate thread!
  # the thread "S" will run simultaneously as more actions
  # below are executed
#print("PROGRAM TERMINATION\n")  
#S.cancel()

print("You're trapped in a room with a zombie!!! You have 3 seconds to figure out what to do before the zombie eats your brains!")

while True:
    choice= input("What do you do?\n>")
    if choice.lower() == "run":
        print("You escaped! Whew!")
        S.cancel()
        break
          # S.cancel CANCELS the "S" thread that's running the countdown
          # if we manage to cancel the thread before it runs "decision()",
          # we'll avoid executing os._exit (i.e. GAME OVER)

print("YOU WIN! You should only see this message if you escaped the zombie!")
```
