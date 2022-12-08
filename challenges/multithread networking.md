## Multi-Threading Challenge

Here is a shortened version of the netmiko code at the end of lab 32:

```python
from datetime import datetime
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

def netcommand(**a_device):   # NEW-- this code is now inside a function!
    net_connect = ConnectHandler(**a_device)  # unpack the dictionary argument
    output = net_connect.send_command("show arp")
    
    # window dressing showing the results
    print(f"\n\n--------- Device {a_device['device_type']} ---------") 
    print(output) 
    print("--------- End ---------") 
```

Use the script we just used in lab 46 as a guide. Can you re-write the code below so that network calls are made instead of API calls?

```python
#!/usr/bin/python3
"""API requests with threads | rzfeeser@alta3.com"""

# standard library
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time

# python3 -m pip install requests
import requests


url_list = [
    "https://api.le-systeme-solaire.net/rest/bodies/lune",
    "https://api.le-systeme-solaire.net/rest/bodies/phobos",
]

def download_file(url):
    html = requests.get(url, stream=True)
    return html.status_code

start = time()

processes = []

# we want to be careful with the number of workers
# if you are making thousands of requests, does your target have limiting engaged?
# beware you don't overload internal or external services; 5 to 10 is fine for most scripts
with ThreadPoolExecutor(max_workers=5) as executor:
    for url in url_list:
        processes.append(executor.submit(download_file, url))   # add a new task to the threadpool and store in processes list

for task in as_completed(processes):    # yields the items in processes as they complete (it finished or was canceled)
    print(task.result())

# display the total run time
print(f'Time taken: {time() - start}')
```

<details>
<summary>CHAD'S SOLUTION</summary>

```python
#!/usr/bin/python3
"""API requests with threads | rzfeeser@alta3.com"""

from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time
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

def netcommand(**a_device):
    net_connect = ConnectHandler(**a_device)
    output = net_connect.send_command("show arp")
    print(f"\n\n--------- Device {a_device['device_type']} ---------")
    print(output)
    print("--------- End ---------")

start = time()

processes = []

with ThreadPoolExecutor(max_workers=5) as executor:
    for device in all_devices:
        processes.append(executor.submit(netcommand, **device))   # add a new task to the threadpool and store in processes list

for task in as_completed(processes):    # yields the items in processes as they complete (it finished or was canceled)
    print(task.result())

# display the total run time
print(f'Time taken: {time() - start}')
```
</details>
