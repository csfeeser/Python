### hosts.j2
```html
{% for host in groups %}
<h4><span>{{ host[0] }}   {{ host[1] }} # {{ host[2] }}</span></h4>
   {% endfor %}

<br>
<li><a href = '/form'></b>Click here to add more data</b></a></li>
<li><a href = '/logout'></b>Click here to log out</b></a></li>
```

### databasemaker.py
```python
import sqlite3
import os.path

groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]

# if challenge.db doesn't exist, create and populate it
if not os.path.exists('challenge.db'):
    conn = sqlite3.connect('challenge.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS HOSTS
     (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
     HOSTNAME     TEXT    NOT NULL,
     IP           TEXT     NOT NULL,
     FQDN         TEXT    NOT NULL);''')

    for group in groups:
        #conn.execute(f"INSERT INTO HOSTS (ID,HOSTNAME,IP,FQDN) VALUES ('{x}','hosty','1.1.1.1','fqdngoeshere')")
        conn.execute(f"INSERT INTO HOSTS (HOSTNAME,IP,FQDN) VALUES ('{group.get('hostname')}','{group.get('ip')}','{group.get('fqdn')}');")
        conn.commit()

    # last line
    conn.close()
```    

### classsolution.py
```python
#!/usr/bin/python3

import sqlite3
import databasemaker

from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import render_template

app = Flask(__name__)

app.secret_key= "random random RANDOM!"

def insertgroup(ip, fqdn, hostname):
    conn = sqlite3.connect('challenge.db')
    conn.execute(f"INSERT INTO HOSTS (HOSTNAME,IP,FQDN) VALUES ('{hostname}','{ip}','{fqdn}');")
    conn.commit()
    conn.close()

def selectdata():
    conn = sqlite3.connect('challenge.db')
    cursor = conn.execute("SELECT HOSTNAME,IP,FQDN from HOSTS")
    
    # list comprehension
    groups= [x for x in cursor]
    return groups


@app.route("/", methods= ["GET","POST"])
def hosts():
    if "username" in session and session["username"] == "admin":
        if request.method == "POST":
            # pull values
            hostname = request.form.get("hostname")
            ip = request.form.get("ip")
            fqdn = request.form.get("fqdn")
            print(hostname, ip, fqdn)
            insertgroup(hostname, ip, fqdn)
            #groups= selectdata()

                        # display current hosts
    groups= selectdata() 
    return render_template("hosts.j2", groups=groups)


@app.route("/form", methods=["GET","POST"])
def form():
    if request.method == "POST":
        session["username"] = request.form.get("username")

    if "username" in session and session["username"] == "admin":
        return render_template("formcollector.html.j2")

    else:
        return """
   <form action = "" method = "post">
      <p>Invalid Login.</p>
      <p><input type = text name = username></p>
      <p><input type = submit value = Login></p>
   </form>
  """

@app.route("/logout")
def logout():
    # accessing this page pops the value of username of the session
    session.pop("username", None)
    return redirect("/")

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
```
