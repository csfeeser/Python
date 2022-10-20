<img src="https://github.com/csfeeser/Python/blob/master/trivia2.png?raw=true" alt="drawing" width="500"/>

## Earlier, you were challenged to write a Flask API that did the following:
  
- A landing page rendered an HTML form asking a trivia question.
- The submitted answer was POSTed to another page
- If the answer was correct, the user was redirected to the "/correct" route
- If the answer was incorrect, the user was returned to the form to try again.

<details>
<summary><b>Click here for an example solution!</b></summary>

```python
#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template

app = Flask(__name__)

html= """<style>
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
</html>"""

@app.route("/correct")
def success():
    return f"That is correct!"

@app.route("/")
def start():
    return html

@app.route("/login", methods = ["POST"])
def login():
        if request.form.get("nm") and request.form.get("nm") == "42":
                return redirect("/correct")
        else:
            return redirect("/")

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
```
</details>

## Here is part TWO of this challenge:
- Take the posted answer and save it to a **cookie** or a **session**.
    - The cookie must be read in order to check if the answer is correct.

- Adapt the HTML to do the following:
    - Add a Jinja2 **{% if %}** expression. If the answer contained in the cookie/session is wrong, have the conditional print something like "XYZ is not the correct answer!" before rendering the rest of the HTML form.
