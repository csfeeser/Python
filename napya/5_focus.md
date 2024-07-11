If you're looking for some solid, tried and true concepts to play with while building skill with Python and Ansible, here are some tools as well as recommendations on how you might use them!

### Python Modules:

1. **os**: Provides functions for interacting with the operating system.
   - **Try**: Use `os.listdir()` to list all files and directories in a specified path.
     ```python
     import os
     print(os.listdir('/path/to/directory'))
     ```

2. **random**: Implements pseudo-random number generators for various distributions.
   - **Try**: Use `random.randint()` to generate a random integer between specified limits.
     ```python
     import random
     print(random.randint(1, 100))
     ```

3. **json**: Provides methods to parse JSON (JavaScript Object Notation) strings or files.
   - **Try**: Use `json.dumps()` to convert a Python dictionary to a JSON string.
     ```python
     import json
     data = {'name': 'John', 'age': 30}
     json_string = json.dumps(data)
     print(json_string)
     ```

4. **requests**: Allows you to send HTTP requests easily.
   - **Try**: Use `requests.get()` to fetch data from a URL.
     ```python
     import requests
     response = requests.get('https://api.github.com')
     print(response.json())
     ```

5. **datetime**: Supplies classes for manipulating dates and times.
   - **Try**: Use `datetime.datetime.now()` to get the current date and time.
     ```python
     import datetime
     now = datetime.datetime.now()
     print(now)
     ```

### Ansible Modules:

1. **ping**: A simple module that just tests the connection from Ansible to the target machine.
   - **Try**: Use the `ping` module to check the connectivity to a host.
     ```yaml
     - name: Ping a host
       ansible.builtin.ping:
     ```

2. **copy**: Used to copy files to remote locations.
   - **Try**: Use the `copy` module to copy a file from the local machine to a remote machine.
     ```yaml
     - name: Copy a file
       ansible.builtin.copy:
         src: /path/to/local/file
         dest: /path/to/remote/destination
     ```

3. **user**: Manages user accounts on remote systems.
   - **Try**: Use the `user` module to create a new user on a remote machine.
     ```yaml
     - name: Create a user
       ansible.builtin.user:
         name: newuser
         state: present
     ```

4. **apt**: Manages packages on Debian-based systems.
   - **Try**: Use the `apt` module to install a package on a Debian-based system.
     ```yaml
     - name: Install a package
       ansible.builtin.apt:
         name: package_name
         state: present
     ```

5. **yum**: Manages packages on Red Hat-based systems.
   - **Try**: Use the `yum` module to install a package on a Red Hat-based system.
     ```yaml
     - name: Install a package
       ansible.builtin.yum:
         name: package_name
         state: present
     ```

### Ansible Magic Variables:

1. **hostvars**: Access variables of other hosts in the inventory.
   - **Try**: Use `hostvars` to get a variable from another host in your playbook.
     ```yaml
     - name: Access variable from another host
       debug:
         msg: "{{ hostvars['other_host']['variable_name'] }}"
     ```

2. **inventory_hostname**: The name of the current host as it is known in the inventory.
   - **Try**: Use `inventory_hostname` to display the current host's name in a task.
     ```yaml
     - name: Show inventory hostname
       debug:
         msg: "This is {{ inventory_hostname }}"
     ```

3. **group_names**: List of groups the current host is part of.
   - **Try**: Use `group_names` to display the groups the current host belongs to.
     ```yaml
     - name: Show group names
       debug:
         msg: "This host is part of the following groups: {{ group_names }}"
     ```

4. **ansible_playbook_dir**: The directory where the playbook is located.
   - **Try**: Use `ansible_playbook_dir` to include a local script relative to the playbook directory.
     ```yaml
     - name: Include a local script
       script: "{{ ansible_playbook_dir }}/scripts/myscript.sh"
     ```

5. **ansible_facts**: Contains various facts gathered about the host during execution.
   - **Try**: Use `ansible_facts` to display all gathered facts about the current host.
     ```yaml
     - name: Show all facts
       debug:
         var: ansible_facts
     ```

### Python Functions:

1. **print()**: Prints the specified message to the screen or other standard output device.
   - **Try**: Use `print()` to output a formatted string.
     ```python
     name = "John"
     print(f"Hello, {name}!")
     ```

2. **len()**: Returns the number of items in an object.
   - **Try**: Use `len()` to find the length of a list.
     ```python
     my_list = [1, 2, 3, 4]
     print(len(my_list))
     ```

3. **range()**: Generates a sequence of numbers.
   - **Try**: Use `range()` in a for loop to iterate over a sequence of numbers.
     ```python
     for i in range(5):
         print(i)
     ```

4. **open()**: Opens a file and returns a corresponding file object.
   - **Try**: Use `open()` to read the contents of a file.
     ```python
     with open('example.txt', 'r') as file:
         contents = file.read()
         print(contents)
     ```

5. **type()**: Returns the type of the specified object.
   - **Try**: Use `type()` to check the type of a variable.
     ```python
     my_var = 10
     print(type(my_var))
     ```
