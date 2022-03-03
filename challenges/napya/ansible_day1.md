## Busted Playbook Challenge!

<img src="https://i.redd.it/i4v9op0chrc51.jpg" width="500"/>



Good morning! To get the blood moving today we'll start with a familiar looking playbook-- however, it's broken! Your job is to get it working (no need to improve it).

1. Please start by getting your environment prepared:

    `student@bchd:~$` `cd && wget https://labs.alta3.com/projects/napya/deploy/napyasetup.sh -qO setup.sh && bash setup.sh`

0. Use vim to create a playbook file of your choosing and enter the following. Then test, fix, repeat!

    `student@bchd:~$` `vim bustedplaybook.yml`
    
```yaml
---
- name: Tuesday Challenge
  hosts: planet express
  connection: network_cli
  gather_facts: yes

  tasks:
   - name: print out the variable named "result"
     debug:
       var: result
       
   -apt:
        name: sl
       state: present
   name: using apt to install sl
   register: result
```

<!--
### SOLUTION

```yaml
---
- name: Tuesday Challenge
  hosts: planetexpress
  connection: ssh
  gather_facts: yes

  tasks:
   - apt:
       name: sl
       state: present
     name: using apt to install sl
     register: result

   - name: print out result
     debug:
       var: result.cache_update_time
```
-->
