# MORNING WARM-UP

The script below is busted. Do your best to fix it, then test it vigorously! You are not required to IMPROVE the script, just make it work "as advertised!"

**My advice? Run the code, see what error returns. Try to fix that error, then run the code again... then repeat until successful!**

`student@bchd:~$` `vim bustedcode.py`

```
#!/usr/bin/env python3

import time
import sys

def delay_print(s):
    # there's nothing wrong with this function, it's just some cool code that
    # will print out strings one character at a time! :)
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.25)

delay_print("Good morning, Mr. Stark. Here are your network interfaces:\n)
print(netifaces.interfaces())

for x in netifaces.interfaces():
    with open("challenge.log") as foo:                 # opens writeable file for logging
        print('Logging addresses for interface x')     # prints name of interface being logged
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr'], file=bar) # Prints the MAC address to file
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr'], file=bar) # Prints the IP address to file
    except:
        print('Could not collect adapter information') # Print an error message
```

`student@bchd:~$` `python3 bustedcode.py`


### SOLUTION

```
#!/usr/bin/env python3

import time
import sys 
import netifaces

def delay_print(s):
    # there's nothing wrong with this function, it's just some cool code that
    # will print out strings one character at a time! :)
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

delay_print("Good morning, Mr. Stark. Here are your network interfaces:\n")
print(netifaces.interfaces())

for igloo in netifaces.interfaces():
    with open("challenge.log", "a") as foo:                 # opens writeable file for logging
        try:
            print('Logging addresses for interface ' + igloo)     # prints name of interface being logged
            print((netifaces.ifaddresses(igloo)[netifaces.AF_LINK])[0]['addr'], file=foo) # Prints the MAC address to file
            print((netifaces.ifaddresses(igloo)[netifaces.AF_INET])[0]['addr'], file=foo) # Prints the IP address to file
        except Exception as e:
            print('Could not collect adapter information:', e) # Print an error message
```            
