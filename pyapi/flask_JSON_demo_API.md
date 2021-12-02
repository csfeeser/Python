In this morning's demo, I created a Flask API that both accepted JSON as a POST and returned JSON as a request.

```python
#!/usr/bin/env python3
"""DEMO: posting JSON, receiving JSON"""

from flask import Flask, request, jsonify, redirect

app= Flask(__name__)

jsondata= []

# ONLY posts to /post
@app.route("/post", methods=["POST"])
def post():
    #request.form   # accessing form data from the post (submitted via HTML)
    #request.args   # accessing data from query params (?name=Chad)
    #request.method # accessing what type of request method was used (GET, POST)
    #request.json   # accessing json attached to the post
    data= request.json
    # data now contains the JSON submitted by the client

    # if JSON was actually sent:
    if data:
        # treat "data" like a dictionary!
        nm= data["name"]
        ic= data["ice cream"]
        color= data["color"]
        jsondata.append({"nm":nm, "ic":ic, "color":color})
    return redirect("/")

@app.route("/")
def index():
    # how to have a Flask API return object as JSON
    return jsonify(jsondata)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
```

The second script used the requests library to send a POST with JSON to the API.

```python
#!/usr/bin/env python3
"""how to use the requests module to send a POST"""

import requests

url= "http://10.2.120.155:2224/post"

chadfavs= {
          "name": "Chad",
          "ice cream": "coffee",
          "color" : "red"
          }

benfavs= {
          "name": "Ben",
          "ice cream": "chocolate",
          "color" : "blue"
          }

devonfavs= {
          "name": "DeVon",
          "ice cream": "reeses",
          "color" : "green"
          }

requests.post(url, json=chadfavs)
requests.post(url, json=benfavs)
requests.post(url, json=devonfavs)
```
