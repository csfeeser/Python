<img src="https://www.brightful.me/content/images/2020/08/shutterstock_686118184.jpg" alt="drawing" width="500"/>

## Write a Flask API that does the following:
  
1. **Make the landing page ("/") return an HTML form.**
   - The form should ask a trivia question of your choosing (feel free to re-use HTML from lab `Building APIs with Python`!)
   - The answer should be POSTed to another path.

2. **Depending on the answer POSTed from the form, do the following:**
   - If the answer is correct, redirect your user to the "/correct" route!
   - If the answer is wrong, return them to the form to try again.
   
3. **You will definitely need to import the following:**

    ```python
    from flask import Flask
    from flask import redirect
    from flask import request
    from flask import render_template
    ```


## SOLUTION
```html
<style>
body {
  background-color: black;
  text-align: center;
  color: white;
  font-family: Arial, Helvetica, sans-serif;
}
</style>
</head>
<body>

<h1>TRIVIA TIME</h1>
<p>What is the meaning of life, the universe, and everything?</p>
<img src="https://stevetobak.com/wp-content/uploads/2021/02/dont-panic.png" alt="Avatar" style="width:200px">

    <form action = "/login" method = "POST">
        <p><input type = "text" name = "nm"></p>
        <p><input type = "submit" value = "submit"></p>
    </form>

</body>
</html>
```


```python
#!/usr/bin/python3
"""Alta3 APIs and HTML"""

## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/correct")
def success():
    return f"That is correct!"

@app.route("/")
def start():
    return render_template("postmaker.html")

@app.route("/login", methods = ["POST"])
def login():
        if request.form.get("nm"):
            answer = request.form.get("nm")
            if answer == "42":
                return redirect("/correct")
            else:
                return redirect("/")
        else:
            return redirect("/")

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
```
