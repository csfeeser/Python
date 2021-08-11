# Jinja2 Challenge:

Below is your "starter data" for this challenge. You'll put this inside your Flask API script as a normal list.

    groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
              {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
              {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]

Your goal is to use Flask to create output like this (if possible, return this in HTML!):

    192.168.30.22 hostA.localdomain # hostA
    192.168.30.33 hostB.localdomain # hostB
    192.168.30.44 hostC.localdomain # hostB

### TASK 1:
- Create a Jinja2 template that would create the above output
- Create a flask server that populates that Jinja2

    <details>
    <summary><b>I can't figure out the Jinja2 template and I gave it my best shot!</b></summary>

    ```
    {% for host in groups %}
       <h4><span>{{ host.ip }}   {{ host.fqdn }} # {{ host.hostname }}</span></h4>
       {% endfor %}

    <br>
    <li><a href = '/form'></b>Click here to add more data</b></a></li>
    <li><a href = '/logout'></b>Click here to log out</b></a></li>
    ```
    </details>



### TASK 2:
- Create a form that lets you add more data to `groups`.

    <details>
    <summary><b>I can't figure out the HTML for a form like this and I gave it my best shot!</b></summary>

    ```
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
    </details>
    
### TASK 3:
- Make an addition to your Flask server. Create a **session** that is made to include a **specific variable** (your choice). A user is ONLY able to add info to `groups` if that session variable is present.

    <details>
    <summary><b>I want to see the full solution.</b></summary>
        Perhaps. Did you give it your best shot?
        <details>
        <summary><b>Yes.</b></summary>
            Truly?
            <details>
            <summary><b>Yes!</b></summary>
                For reals?
                <details>
                <summary><b>YES!</b></summary>
                    Click here, then. --> https://github.com/csfeeser/Python/blob/master/flask/j2solution.md
                </details>
            </details>
        </details>
    </details>
