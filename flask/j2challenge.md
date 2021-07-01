# Jinja2 Challenge:

Let the following be the data structure that you want to put inside of a hosts file:

    groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
              {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
              {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]

Your goal is to use Flask to create output like this:

    192.168.30.22 hostA.localdomain # hostA
    192.168.30.33 hostB.localdomain # hostB
    192.168.30.44 hostC.localdomain # hostB

### TASK 1:
- Create a Jinja2 template that would create the above output
- Create a flask server that populates that Jinja2

### TASK 2:
- Create a form that lets you add more data to `groups`.

### TASK 3:
- Make an addition to your Flask server. Create a **session** that is made to include a **specific variable** (your choice). A user is ONLY able to add info to `groups` if that session variable is present.

