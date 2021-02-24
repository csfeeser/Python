# Jinja2 Challenge:

Let the following be the data structure that you want to put inside of a hosts file:

    groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
              {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
              {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]

Your goal is to use Flask to create output like this:

    192.168.30.22 hostA.localdomain # hostA
    192.168.30.33 hostB.localdomain # hostB
    192.168.30.44 hostC.localdomain # hostB

### YOUR TASK:
- Create a Jinja2 template that would create the above output
- Create a flask server that populates that Jinja2

### BONUS:
- Create a form that lets you add more data to `groups`.

<!-- 
Solution

# Undercloud Host FQDNs
{% for item in groups %}
{{ item.ip }}    {{item.fqdn }} # {{ item.hostname }}
{% endfor %}



ROCKET SCIENCE!!!

Turn this into an API that accepts inputs from a form

#!/usr/bin/env python3

from flask import Flask
from flask import request
from flask import render_template, url_for, redirect


app = Flask(__name__)

groups = [{"hostname": "hostA", "ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]

@app.route("/", methods=["POST", "GET"])
@app.route("/add_ip", methods=["POST", "GET"])
def adder():
    if request.method == "POST":
        hostname = request.form.get("hostname")
        ip = request.form.get("ip")
        fqdn = request.form.get("fqdn")
        groups.append({"hostname": hostname, "ip": ip, "fqdn": fqdn})
        print(groups)
        return redirect(url_for('adder'))
    else:
        print("Groups again")
        print(groups)
        return render_template("hostsfile.html", groups=groups)


app.run(port=2224)



HERE IS THE hostsfile.html file:

<HTML>
<body>
<h1>
Here are the hosts</h1> <br>

{% for item in groups %}<ul>{{ item.ip }} {{ item.fqdn }} # {{ item.hostname }}</ul>{% endfor %}

<form action = "/add_ip" method="post">
    Hostname <input type="text" name="hostname"/><br>
    IP <input type="text" name="ip"/><br>
    FQDN <input type="text" name="fqdn"/><br>
    <input type="submit" value="Add Host"/>
</form>
</body>
</HTML>
-->

