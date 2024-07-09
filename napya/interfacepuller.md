The following code was shown in class; it will create a text output of all interfaces on a Linux system and their IPv4/MAC addresses.

You MUST install the `netifaces` library for this to work!

```python
#!/usr/bin/env python3

import netifaces
# python3 -m pip install netifaces

def output():
    for i in netifaces.interfaces():
        print('\n****** details of interface - ' + i + ' ******')
        try: 
            print('MAC: ', end='') 
            print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
            print('IP: ', end='')  
            print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
        except:          
            print('Could not collect adapter information') 
            # ^^ this will print instead of causing an error if any of the above data can't be found

if __name__ == "__main__": # if this code is being executed DIRECTLY:
    output()
```
