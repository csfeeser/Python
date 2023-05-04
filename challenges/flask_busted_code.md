# WARMUP: Busted Flask Code!

<img src="https://pbs.twimg.com/profile_images/521380344625246209/1R7RQnZh_400x400.jpeg" alt="drawing" width="200"/>

### Below is code that renders HTML containing a form to POST an answer to a trivia question.
### HOWEVER, it is broken! VERY BROKEN! Fix it (no need to improve it)!

You can test the functionality by either opening the page in `aux1` and filling out the form, OR you can use curl:  
`curl localhost:2224/login -d nm=42 -L`

1. `student@bchd:~$` `vim ~/mycode/flaskapi/bustedflask.py`

    ```python
    #!/usr/bin/python3

    from flask import Flask

    app = Flask(__name__)

    ### NOTE FROM CHAD: There is nothing wrong with the HTML
    html= '''<style>
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
    </html>'''

    def success():
        return f"That is correct!"

    def start():
        return html

    def login():
            if request.form.get("nm"):
                answer = request.form.get("nm")
                if answer == "42":
                    return redirect(url_for("success")
                else:
                    return redirect(/)
            else:
                return redirect(/)

    if __name__ == "__main__":
       app.run()
    ```

<!--
## SOLUTION

```python
#!/usr/bin/python3

from flask import Flask
from flask import request
from flask import url_for
from flask import redirect

app = Flask(__name__)

### NOTE FROM CHAD: There is nothing wrong with the HTML
html= '''<style>
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
</html>'''

@app.route("/success")
def success():
    return f"That is correct!"

@app.route("/")
def start():
    return html

@app.route("/login", methods= ["POST"])
def login():
        if request.form.get("nm"):
            answer = request.form.get("nm")
            if answer == "42":
                return redirect(url_for("success"))
            else:
                return redirect("/")
        else:
            return redirect("/")

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
```
