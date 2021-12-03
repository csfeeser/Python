#!/usr/bin/env python3
""" Author: RZFeeser || Alta3 Research
Gather data returned by various APIs published on OMDB, and cache in a local SQLite DB
"""

import json
import sqlite3
import requests
from flask import Flask, jsonify

app = Flask(__name__)

# Define the base URL
OMDBURL = "http://www.omdbapi.com/?"

# helper function!
def movielookup(mykey, searchstring):
    """Interactions with OMDB API
       mykey = omdb api key
       searchstring = string to search for"""
    try:
        # begin constructing API
        api = f"{OMDBURL}apikey={mykey}&s={searchstring}"

        ## open URL to return 200 response
        resp = requests.get(api)
        ## read the file-like object decode JSON to Python data structure
        return resp.json()
    except:
        return False

def trackmeplease(datatotrack):
    conn = sqlite3.connect('mymovie.db')
    try:
        conn.execute('''CREATE TABLE IF NOT EXISTS MOVIES (TITLE TEXT PRIMARY KEY NOT NULL, YEAR INT  NOT NULL);''')

        # loop through the list of movies that was passed in
        for data in datatotrack:
            # in the line below, the ? are examples of "bind vars"
            # this is best practice, and prevents sql injection attacks
            # never ever use f-strings or concatenate (+) to build your executions
            conn.execute("INSERT INTO MOVIES (TITLE,YEAR) VALUES (?,?)",(data.get("Title"), data.get("Year")))
            conn.commit()

        print("Database operation done")
        conn.close()
        return True
    except:
        return False

# Read in API key for OMDB
def harvestkey():
    with open("/home/student/omdb.key") as apikeyfile:
        return apikeyfile.read().rstrip("\n") # grab the api key out of omdb.key

@app.route("/1/<searchstring>")
@app.route("/2/<searchstring>")
def search(searchstring):
    # translated JSON
    mykey= harvestkey()
    resp = movielookup(mykey, searchstring)
    if resp: # has a value
         resp = resp.get("Search")
         print(resp)
         # write the results into the database
         if trackmeplease(resp):
             return "Successfully added to database!"
         else:
             return "There was an error!"

    else:
         return "That search did not return any results."

@app.route("/5")
def display():
        """return the contents of the database in JSON format"""
        conn = sqlite3.connect('mymovie.db')
        cursor = conn.execute("SELECT title, year from MOVIES")

        jsondata= []

        for row in cursor:
            jsondata.append({"title":row[0], "year":row[1]})

        conn.close()
        # return as JSON
        return jsonify(jsondata)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) 
