# Netmiko Lab Code... SIMPLIFIED!

Our Netmiko lab code was built to handle errors, loop across multiple devices, and take input from a csv file! However, that can make it more challenging to see and understand the role that Netmiko has to play in the script. Below is a VERY stripped down version of our original code that should help make the use of Netmiko more clear!

```python
#!/usr/bin/env python3

import os
import netmiko

def main():

        # statically set all variables for netmiko connection and configuration
        dev_type= "arista_eos"
        dev_ip= "sw-1"
        dev_un= "admin"
        dev_pw= "alta3"
        config_loc= "/home/student/mycode/usopen/sw-1-clean.conf"

        # use netmiko ConnectHandler class to create a connection with our switch
        open_connection = netmiko.ConnectHandler(device_type=dev_type, ip=dev_ip, username=dev_un, password=dev_pw)
        
        # use the ConnectHandler "send_command" method to execute a command in our switch, print result
        print("\n***** BEGIN SHOW IP INT BRIEF *****")
        print(open_connection.send_command("show ip int brief"))

        # use the os module's "system" function to execute a ping command on BCHD (not the switch)
        print("\n***** BEGIN ICMP CHECKING *****")
        response= os.system("ping -c 1 " + dev_ip)
        if response == 0:
            print(response)
        else:
            print("PING FAILED")

        # open the config file with the changes we want to push to the switch
        with open(config_loc, 'r') as config_file:
            # .read() out the file, and splitlines() to turn the text file into a list
            config_lines = config_file.read().splitlines()

        # enable mode = sudo mode for network devices!
        open_connection.enable()

        # apply the configuration to the switch with "send_config_set"- print the output to see how it goes!
        print("\n***** APPLYING SWITCH CONFIGURATION *****")
        print(open_connection.send_config_set(config_lines))

        # SAVE the changes you made to the switch with a "write memory" command
        open_connection.send_command_expect('write memory')

        # always close any connections that you open!
        open_connection.disconnect()

main()
```
