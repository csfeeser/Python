## Looping Exercise


Grab the following playbook:

```yaml
- name: showing off loops in ansible
  hosts: localhost
  connection: local

  vars:
    books:
    - Title: Watchmen
      Author: Alan Moore
    - Title: Eragon
      Author: Christopher Paolini
    - Title: The Hobbit
      Author: J.R.R. Tolkien
    - Title: Ender's Game
      Author: Orson Scott Card

        # for item in books:
        #   print(item)
  tasks:
   - name: print out a bunch o' books
     debug:
       msg: "{{ item }}"
     loop: "{{ books }}"
```

Edit the playbook so that you get the following output instead:

```
TASK [print out a bunch o' books] **********************************************
ok: [localhost] => (item={'Title': 'Watchmen', 'Author': 'Alan Moore'}) => {
    "msg": "Watchmen by Alan Moore is my favorite book!"}
ok: [localhost] => (item={'Title': 'Eragon', 'Author': 'Christopher Paolini'}) => {
    "msg": "Eragon by Christopher Paolini is my favorite book!"}
ok: [localhost] => (item={'Title': 'The Hobbit', 'Author': 'J.R.R. Tolkien'}) => {
    "msg": "The Hobbit by J.R.R. Tolkien is my favorite book!"}
ok: [localhost] => (item={'Title': "Ender's Game", 'Author': 'Orson Scott Card'}) => {
    "msg": "Ender's Game by Orson Scott Card is my favorite book!"}
```

**HINT:** The following is the only line you have to edit!

```
msg: "{{ item }}"
```
