### Accepting JSON as POST and returning JSON as response
```python
#!/usr/bin/env python3

from flask import Flask, render_template, request, jsonify, redirect

app = Flask(__name__)

jsondata= []

@app.route("/post",methods=["POST"])
def post():
    if request.method == 'POST':
        data = request.json
        if data:
            nm = data["nm"]
            addr = data["addr"]
            city = data["city"]
            pin = data["pin"]
            jsondata.append({"nm":nm,"addr":addr,"city":city,"pin":pin})
    return redirect("/")

@app.route("/")
def index():
    return jsonify(jsondata)

if __name__ == '__main__':
        app.run(host="0.0.0.0", port=2224, debug = True)
```

### Making a POST request with JSON

```python
import requests
import json

data = {
    "nm": "Chad",
    "addr": "Hersheypark Drive",
    "city": "Hershey",
    "pin": "1234",
}

requests.post("http://10.13.43.121:2224/post", json=data)
```
