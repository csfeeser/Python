#!/usr/bin/python3
"""Alta3 APIs and HTML"""

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request # allows us to read incoming POST data
from flask import render_template # opens HTML files and returns html to client

app = Flask(__name__)


html= """<form method="post" action= "/login">
     <p>Age:</p>
     <select name="age">
        <option value="1_sre">23</option>
        <option value="2_sam">24</option>
        <option value="5_john">25</option>
     </select>
     <input type="submit" name="submit"/>
</form>"""

@app.route("/")
def start():
    return html

@app.route("/login", methods = ["POST"])
def login():
    if request.method == "POST":
        # check and see if data was posted
        if request.form.get("age"):
            user= request.form.get("age")
        else:
            user= "defaultuser"
    return redirect(f"/success/{user}")

@app.route("/success/<name>")
def success(name):
    return f"Welcome {name}\n"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
