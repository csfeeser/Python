# Ansible Content Challenge!

To test what you've learned about Ansible so far, please do the following:

1. Run this command and see what containers you are currently running.

    `student@bchd:~$` `sudo docker ps`

0. If you do **NOT** see bender, fry, zoidberg, and farnsworth, run the following commands:

    `student@bchd:~$` `cd`

    `student@bchd:~$` `vim setup.sh`

       wget https://labs.alta3.com/projects/ansible/deploy/max-teardown.sh
       bash max-teardown.sh
       wget https://labs.alta3.com/projects/ansible/deploy/pexpress-setup.sh
       bash pexpress-setup.sh
       ssh-copy-id bender@10.10.2.3 -f
       ssh-copy-id fry@10.10.2.4 -f
       ssh-copy-id zoidberg@10.10.2.5 -f

    `student@bchd:~$` `bash setup.sh`

    When prompted, type `alta3` as the password for bender, fry, and zoidberg.
    
0. Edit your inventory file (`/home/student/ans/inv/dev/hosts`) and add the following to it:

    ```
    [renamed]
    bugs      ansible_host=10.10.2.3 ansible_user=bender ansible_python_interpreter=/usr/bin/python3
    daffy         ansible_host=10.10.2.4 ansible_user=fry ansible_python_interpreter=/usr/bin/python3
    elmer    ansible_host=10.10.2.5 ansible_user=zoidberg ansible_python_interpreter=/usr/bin/python3
    taz  ansible_host=10.10.2.6 ansible_user=farnsworth ansible_ssh_pass=alta3
    ```

0. Write a playbook that does the following:
    - explicitly states there will be an **ssh** connection to the hosts
    - writes to all hosts in `renamed` EXCEPT for *taz*.
    - DO NOT gather facts about your hosts
    - Create a new user with *your name* in each machine. Assign it to the group *funkytown*
    - **BONUS**- the name of the user is passed with a {{ variable }} outside of the tasks section.

<!--
<details>
<summary>SOLUTION:</summary>
<br>

Here's a link to an awesome [Stack Overflow Solution!](https://stackoverflow.com/questions/63717959/create-user-group-if-it-does-not-exist-using-ansible)

```yaml
- name: "day 1 challenge solution"
  hosts: renamed,!taz
  gather_facts: no
  connection: ssh
  become: true

  vars_prompt:
    - name: "username"
      prompt: "What is the name of the new user?"
      private: no

    - name: "password"
      prompt: "What is the password of the user?"
      private: yes
      confirm: yes
      encrypt: "sha512_crypt"

  tasks:
    - name: Ensure group "somegroup" exists
      group:
        name: funkytown
        state: present

    - name: "Add the user {{ username }}"
      user:
        name: "{{ username }}"
        password: "{{ password }}"
        group: funkytown
```

</details>
-->
