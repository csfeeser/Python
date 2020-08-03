## JSON Upgrade Challenge!

Previously you had been tasked with using a static dictionary to make output that looked like the following:

```
People in space:  3
Chris Cassidy is on the ISS.
Anatoly Ivanishin is on the ISS.
Ivan Vagner is on the ISS.
```

The code you wrote to accomplish this looked something like:

```
astros= {"number": 3, "people": [{"craft": "ISS", "name": "Chris Cassidy"}, {"craft": "ISS", "name": "Anatoly Ivanishin"}, {"craft": "ISS", "name": "Ivan Vagner"}], "message": "success"}

print("People in space: ", astros["number"])

for x in astros["people"]:
    print(f"{x['name']} is on the {x['craft']}")
```

**CHALLENGE**- Using your original script (or a copy of the one above) adapt your code so that it reads in the astronaut data *directly from the API*, not from a static dictionary (yuck).

If you need a starting point on how to access JSON data, look at how we accomplished it with *cat-facts* in **PyBasics Lab 37- Python, APIs and JSON** using the requests module!

http://api.open-notify.org/astros.json

```
# FIRST, gotta import requests!
import requests

# SECOND make a request object from the URL!
r = requests.get('http://api.open-notify.org/astros.json')

# THIRD, replace your static "astros" dictionary with the translated JSON!
astros= r.json()


print("People in space: ", astros["number"])

for x in astros["people"]:
    print(f"{x['name']} is on the {x['craft']}")                                                  
```
