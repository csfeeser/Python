# Returning and POSTing JSON with Flask

### Lab Objective

The objective of this lab is to return JSON from an endpoint in our Flask API. The client should be able to POST JSON to our API as well.

### Procedure

0. Move into (or create) a new directory to work in, `/home/student/mycode/flaskapi/`

    `student@bchd:~$` `mkdir -p /home/student/mycode/flaskapi/`
    
0. Move into the directory:

    `student@bchd:~$` `cd ~/mycode/flaskapi/`
    
0. Let's write a new Flask application that contains some data about everyone's favorite web-slinger.

    `student@bchd:~/mycode/flaskapi$` `vim spideyapi01.py`
    
    ```python
    #!/usr/bin/env python3
    """DEMO: receiving JSON"""

    from flask import Flask
    from flask import request
    from flask import redirect
    from flask import jsonify

    app= Flask(__name__)

    spiderdata= {
        "name": "Spider-Man",
        "realName": "Peter Parker",
        "since": 1962,
        "powers": [
            "wall crawling",
            "web shooters",
            "spider senses",
            "super human stregth & agility"
                  ]
                 }

    @app.route("/")
    def index():
        # jsonify returns legal JSON
        return jsonify(spiderdata)

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=2224)
    ```
0. Save and run your script.

    `student@bchd:~/mycode/flaskapi$` `python3 spideyapi01.py`

0. Open a second window. Create the following:

    `student@bchd:~/mycode/flaskapi$` `vim spideyrequest01.py`

    ```
    #!/usr/bin/env python3
    import requests

    URL= "127.0.0.1:2224/"

    resp= requests.get(URL).json()

    print(resp)
    ```

0. Save and run your script.

    `student@bchd:~/mycode/flaskapi$` `python3 spideyrequest01.py`

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
