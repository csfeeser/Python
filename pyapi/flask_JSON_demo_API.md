# Returning and POSTing JSON with Flask

### Lab Objective

The objective of this lab is to return JSON from an endpoint in our Flask API. The client should be able to POST JSON to our API as well.

### Procedure

1. Move into (or create) a new directory to work in, `/home/student/mycode/flaskapi/`

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

    herodata= [{
        "name": "Spider-Man",
        "realName": "Peter Parker",
        "since": 1962,
        "powers": [
            "wall crawling",
            "web shooters",
            "spider senses",
            "super human strength & agility"
                  ]
                 }]

    @app.route("/")
    def index():
        # jsonify returns legal JSON
        return jsonify(herodata)

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
    from pprint import pprint
    
    URL= "http://127.0.0.1:2224/"

    resp= requests.get(URL).json()

    pprint(resp)
    ```

0. Save and run your script.

    `student@bchd:~/mycode/flaskapi$` `python3 spideyrequest01.py`

    ```
    [{'name': 'Spider-Man',
     'powers': ['wall crawling',
                'web shooters',
                'spider senses',
                'super human strength & agility'],
     'realName': 'Peter Parker',
     'since': 1962}]
    ```

0. Cool! Your API returned JSON and your requests script converted it to a Pythonic dictionary!

0. Let's update our Flask application to allow POSTing JSON.

    `student@bchd:~/mycode/flaskapi$` `vim spideyapi02.py`
    
    ```python
    #!/usr/bin/env python3
    """DEMO: receiving JSON"""

    from flask import Flask
    from flask import request
    from flask import redirect
    from flask import jsonify

    import json

    app= Flask(__name__)

    herodata= [{
        "name": "Spider-Man",
        "realName": "Peter Parker",
        "since": 1962,
        "powers": [
            "wall crawling",
            "web shooters",
            "spider senses",
            "super human strength & agility"
                  ]
                 }]

    @app.route("/", methods=["GET","POST"])
    def index():
        if request.method == 'POST':
            data = request.json
            if data:
               data= json.loads(data)
               name = data["name"]
               realName = data["realName"]
               since = data["since"]
               powers = data["powers"]
               herodata.append({"name":name,"realName":realName,"since":since,"powers":powers})

        return jsonify(herodata)

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=2224)
    ```

0. Save and run your script.

    `student@bchd:~/mycode/flaskapi$` `python3 spideyapi02.py`

0. In your second window, create the following. Let's post some *Wolverine* info to our herodata object in our API:

    `student@bchd:~/mycode/flaskapi$` `vim spideyrequest02.py`

    ```python
    #!/usr/bin/env python3
    import requests
    import json
    from pprint import pprint

    URL= "http://127.0.0.1:2224/"

    new_hero= {
               "name": "Wolverine",
               "realName": "James Howlett",
               "since": 1974,
               "powers": ["adamantium skeleton","claws","regeneration"]
              }

    # json.dumps takes a python object and returns it as a JSON string
    new_hero= json.dumps(new_hero)

    # requests.post requires two arguments at the minimum;
    # a url to send the request 
    # and a json string to attach to the request
    resp= requests.post(URL, json=new_hero)

    # pretty-print the response back from our POST request
    pprint(resp.json())
    ```

0. Save and run your script.

    `student@bchd:~/mycode/flaskapi$` `python3 spideyrequest02.py`
    
    ```
    [{'name': 'Spider-Man',
      'powers': ['wall crawling',
                 'web shooters',
                 'spider senses',
                 'super human strength & agility'],
      'realName': 'Peter Parker',
      'since': 1962},
     {'name': 'Wolverine',
      'powers': ['adamantium skeleton', 'claws', 'regeneration'],
      'realName': 'James Howlett',
      'since': 1974}]
    ```
    
 0. Success! Your POST request worked and your API returned the updated `herodata` list as JSON!
