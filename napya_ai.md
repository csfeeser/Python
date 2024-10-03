# Warmup: Using AI to Improve Python Network Automation!

<img src="https://media.licdn.com/dms/image/v2/D5622AQHhZVfRm7qPDQ/feedshare-shrink_800/feedshare-shrink_800/0/1721224930274?e=2147483647&v=beta&t=dqkCOSZP1-KflvJT3lDreRZ04xy4jMHorj5qvhYsCIY" width="300"/>

Good morning! Today, we’ll use the `llm` tool to generate code, then integrate and improve an existing network automation script using `netmiko`. The goal is to see how the AI can assist us with enhancing our Python script. Let’s dive in!

### **1. Start by generating a simple Python script with `llm`.**

Let’s begin by generating a silly Python script using the `llm` tool.

`student@bchd:~$` `llm "Generate a simple Python script that prints 10 random dog names"`

This will get you warmed up using `llm` and introduce some creativity. Run the script to see what you get!

### **2. Now, open `vim` and paste the `netmiko` script.**

Next, you’ll take a more practical approach by working with network devices. Open `vim` and paste the following script to get started:

`student@bchd:~$` `vim netmiko_script.py`

```python
from netmiko import ConnectHandler 

arista1 = { 
    'device_type': 'arista_eos', 
    'host':   'sw-1', 
    'username': 'admin', 
    'password': 'alta3', 
    } 

arista2 = { 
    'device_type': 'arista_eos', 
    'host':   'sw-2', 
    'username': 'admin', 
    'password': 'alta3', 
    } 

all_devices = [arista1, arista2]

for a_device in all_devices:
    net_connect = ConnectHandler(**a_device)
    output = net_connect.send_command("show arp")
    
    print(f"\n\n--------- Device {a_device['device_type']} ---------") 
    print(output) 
    print("--------- End ---------")
```

Save and exit by pressing `Esc`, then `:wq`.

### **3. Use the `llm` tool to add comments to the script.**

Our script currently has no comments! Let’s use the `llm` tool to add comments to each line, explaining what the code does.

`student@bchd:~$` `cat netmiko_script.py | llm -s "add comments explaining what each line of code does"`

This should give you a nicely commented version of the script.

### **4. Use `llm` to further improve the script.**

Here are 10 suggestions for features or tasks you can ask the AI to help with:

1. **Save ARP output to a file**: Ask the AI to modify the script so that the output from each device is saved to a text file.
2. **Use environment variables for credentials**: Ask the AI to refactor the script to store sensitive information like usernames and passwords in environment variables.
3. **Log successful connections**: Have the AI add logging to indicate when a connection to a device is successful.
4. **Handle exceptions for connection errors**: Ask the AI to add error handling to manage failed connections gracefully.
5. **Send multiple commands**: Modify the script to send multiple commands (e.g., "show version" and "show interfaces") to each device.
6. **Add device-specific command sets**: Customize the commands for each device using AI.
7. **Add timing for each connection**: Ask the AI to time how long each connection and command execution takes.
8. **Execute configuration changes**: Have the AI add a feature that allows configuration changes (e.g., modifying the hostname) to the devices.
9. **Use a progress bar**: Ask the AI to add a progress bar to show the progress of the script when working with multiple devices.
10. **Enable verbose logging**: Have the AI add a feature for verbose logging for debugging purposes.

Use the suggestions above to ask the AI to improve the script for you. Pick one or more features from the list, and task the `llm` tool with helping you implement them.

For example:

`student@bchd:~$` `cat netmiko_script.py | llm -s "add a feature that saves the ARP output to a file for each device"`
