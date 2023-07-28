# WARMUP: Busted Flask Code!

<img src="https://pbs.twimg.com/profile_images/521380344625246209/1R7RQnZh_400x400.jpeg" alt="drawing" width="200"/>

### Below is code that renders HTML containing a form to POST an answer to a trivia question.
### HOWEVER, it is broken! VERY BROKEN! Fix it (no need to improve it)!

You can test the functionality by either opening the page in `aux1` and filling out the form, OR you can use curl:  
`curl localhost:2224/login -d nm=42 -L`

<details>
<summary>Click here for a list of what's wrong with the code WITHOUT including the solution</summary>

- NOTHING is wrong with the HTML!
- THREE flask functions were not imported
- decorators are missing from the functions
- one of the routes must specify that it will accept a POST method
- common syntax errors: missing ) and missing "quotation marks"
- app.run() must specify host IP and port to display correctly in aux1 (see lab 33)

</details>

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

## SOLUTION

<details>
<summary>Click here to see the solution!</summary>
    
```python
#!/usr/bin/python3

from flask import Flask
from flask import request, redirect, url_for # missing imports

app = Flask(__name__)

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

@app.route("/correct") # missing decorator
def success():
    return f"That is correct!"

@app.route("/") # missing decorator
def start():
    return html

@app.route("/login", methods= ["POST"]) # missing decorator, 
                                        #ALSO must specify that POST method allowed
def login():
        if request.form.get("nm"):
            answer = request.form.get("nm")
            if answer == "42":
                return redirect(url_for("success")) # missing ending )
            else:
                return redirect("/")  # missing "" around /
        else:
            return redirect("/")      # missing "" around /

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)  # specify host and port so we can see in aux1
```

</details>
