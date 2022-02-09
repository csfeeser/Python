## Busted Playbook Challenge!

<img src="https://i.redd.it/i4v9op0chrc51.jpg" width="500"/>



Good morning! To get the blood moving today we'll start with a familiar looking playbook-- however, it's broken! Your job is to get it working (no need to improve it).

Please start by getting your environment prepared:

`student@bchd:~$` `cd && wget https://labs.alta3.com/projects/ansible/deploy/setup.sh && bash setup.sh`

You now have an inventory file. Check it out with the following command:

`student@bchd:~$` `less ~/mycode/inv/dev/hosts`

> You can scroll up and down the document with your arrow keys. Press q when you're ready to return to the command line.
We will use the group `planetexpress` for the following playbook.

Use vim to create a playbook file of your choosing and enter the following. Then test, fix, repeat!

```yaml
---
- name: Wednesday Challenge
  hosts: planet express
  connection: network_cli
  gather_facts: yes

  vars:
     trivia_api: https://opentdb.com/api.php?amount=1&category=18&difficulty=easy&type=multiple
     
  tasks:
   - name: print out the variable named "result"
     debug:
       var: result
       
   -uri:
        method: POST
       url: trivia_api
   name: using apt to install sl
   register: result
```

<!--
### SOLUTION

```yaml
---
- name: Wednesday Challenge
  hosts: planetexpress
  connection: ssh
  gather_facts: yes
 
  vars:
    trivia_api: https://opentdb.com/api.php?amount=1&category=18&difficulty=easy&type=multiple

  tasks:
   - name: sending a GET request to the API
     uri:
       method: GET
       url: "{{ trivia_api }}"
     register: result

   - name: print out result
     debug:
       var: result
```
-->
