#!/usr/bin/python3
"""Solution to trivia challenge!"""

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/") 
def start():
    return render_template("landing.html")

@app.route("/answer", methods = ["POST"])
def answer():
    keywords= ["african","european"]

    # if an answer was given       # if "african" and "european" are in that answer
    if request.form.get("ans") and any(x in request.form.get("ans").lower() for x in keywords):
        return redirect("/correct")

    else:
        return redirect("/wrong")

@app.route("/correct")
def success():
    return render_template("correct.html")

@app.route("/wrong")
def failure():
    return render_template("wrong.html")


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
