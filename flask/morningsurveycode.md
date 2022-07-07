## Morning Survey Code!

If you prefer, you can test and see what response codes come back to help answer your survey questions this morning! Here is a reminder of how you can use `curl` to test:

**send GET request-**  `curl localhost:2224/<path>`  
*Example-* `curl localhost:2224/one`  

**send POST request-**  `curl localhost:2224/<path> -d <whatever you're posting>`  
*Example-* `curl localhost:2224/four -d nm=testvalue`  

Get the code running below. Use TMUX to open a new terminal so you can use curl to test!

**SPLIT SCREEN HORIZONTALLY:**  
`ctrl` `b` (hands off keyboard) `shift` `"`

### Figure 1

```python
#!/usr/bin/python3
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/one")
def first():
    return "Hello Admin"

@app.route("/two/<adj>")
def second(adj):
    return f"Python is {adj}!"

@app.route("/three", methods= ["GET"])
def third():
    return redirect(url_for("third"))

@app.route("/four", methods= ["GET", "POST"])
def fourth():
    return redirect(url_for("eightyninebajillionth"))

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
