## Jinja2 Solution

### Here is the link to the [original challenge](https://github.com/csfeeser/Python/blob/master/flask/j2challenge.md)!

### templates/hosts.j2

```html
{% for host in groups %}
   <h4><span>{{ host.ip }}   {{ host.fqdn }} # {{ host.hostname }}</span></h4>
   {% endfor %}

<br>
<li><a href = '/form'></b>Click here to add more data</b></a></li>
<li><a href = '/logout'></b>Click here to log out</b></a></li>
```

### templates/formcollector.html.j2

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Enter new data</title>
    <form action = "/" method = "POST">
        <p>Enter Hostname:</p>
        <p><input type = "text" name = "hostname"></p>
        <p>Enter IP Address:</p>
        <p><input type = "text" name = "ip"></p>
        <p>Enter Fully Qualified Domain Name:</p>
        <p><input type = "text" name = "fqdn"></p>
        <p><input type = "submit" value = "submit"></p>
    </form>
</head>
<body>
</body>
</html>
```


### solution.py

```python
#!/usr/bin/python3

from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import render_template

app = Flask(__name__)

app.secret_key= "random random RANDOM!"

groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]

@app.route("/", methods= ["GET","POST"])
def hosts():
    # GET returns the rendered hosts
    # POST adds new hosts, then returns rendered hosts
    if "username" in session and session["username"] == "admin":
        if request.method == "POST":
            # pull all values from posted form
            hostname = request.form.get("hostname")
            ip = request.form.get("ip")
            fqdn = request.form.get("fqdn")
            # create a new dictionary with values, add to groups
            groups.append({"hostname": hostname, "ip": ip, "fqdn": fqdn})
    return render_template("hosts.j2", groups=groups)

@app.route("/form", methods=["GET","POST"])
def form():
    # HTML form that collects hostname, ip, and fqdn values
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
