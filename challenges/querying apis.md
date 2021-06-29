# Querying APIs!

## Choose to continue Lab 20 (NASA APIs) or Lab 21 (Marvel Comic API)

### Lab 20. NASA APIs

The NeoWS (Near Earth Object Web Service) script is incomplete! Implement the following:

- query the user for a start and end date.
- return how many asteroids were present in that range
- return how many asteroids were **potentially hazardous** in that range.
- **Stretch Goal**: In terms of kilometers, what was the biggest asteroid in that range? The fastest? The closest?

<!--
#!/usr/bin/env python3

import requests ## 3rd party URL lookup

## define the main function
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API URL

    startdate= "start_date=" + input("Choose a start date (YYYY-MM-DD) ")
    enddate= "&end_date=" + input("Choose an end date (YYYY-MM-DD) ")
    mykey = '&api_key=g2dpPgvaIy7V4gdXO8cTKmMMJP2EEwR3RNYb6aQ0' ## replace this with our API key

    neourl = neourl + startdate + enddate + mykey
    print(neourl)

    neodata = (requests.get(neourl)).json()

    size= 0
    asteroid_distance= 0
    asteroid_names= []
    danger_count= 0

    print(f"Total Asteroids in Range: {neodata['element_count']}")
    for date in neodata["near_earth_objects"].keys():
        for aster in neodata["near_earth_objects"][date]:
            asteroid_names.append(aster["name"])
            if aster["estimated_diameter"]["kilometers"]["estimated_diameter_max"] > size:
                size= aster["estimated_diameter"]["kilometers"]["estimated_diameter_max"]
            if float(aster["close_approach_data"][0]["miss_distance"]["lunar"]) > asteroid_distance:
                asteroid_distance = float(aster["close_approach_data"][0]["miss_distance"]["lunar"])
            if aster["is_potentially_hazardous_asteroid"]:
                danger_count += 1

    print(f"Largest Asteroid (kilometers): {size}")
    print(f"Closest Asteroid (lunar): {asteroid_distance}")
    print(f"Number of potentially hazardous asteroids: {danger_count}")
    input("Press ENTER to see a list of all asteroids.")
    for a,b,c in zip(asteroid_names[::3],asteroid_names[1::3],asteroid_names[2::3]):
        print('{:<30}{:<30}{:<}'.format(a,b,c))

if __name__ == "__main__":
    main()
-->

### Lab 21. Marvel Comic API

For a given Marvel character, return the following:

- How many comics did they appear in?
  - What are the titles of the last 5 they appeared in?
- Return another piece of information of your choice!
- What is their backstory (if provided)?
- Download a picture of the character to your /home/student/static directory

<!--
#!/usr/bin/env python3
"""Marvel Python Client
RZFeeser@alta3.com | Alta3 Research"""

# standard library imports
import argparse   # pull in arguments from CLI
import time       # create time stamps (for our RAND)
import hashlib    # create our md5 hash to pass to dev.marvel.com
from pprint import pprint # we only want pprint() from the package pprint

# 3rd party imports
import requests   # python3 -m pip install requests
import wget

## Define the API here
API = 'http://gateway.marvel.com/v1/public/characters'

## Calculate a hash to pass through to our MARVEL API call
## Marvel API wants md5 calc md5(ts+privateKey+publicKey)
def hashbuilder(rand, privkey, pubkey):
    return hashlib.md5((f"{rand}{privkey}{pubkey}").encode('utf-8')).hexdigest()  # create an MD5 hash of our identifers

## Perform a call to MARVEL Character API
## http://gateway.marvel.com/v1/public/characters
## ?name=Spider-Man&ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150
def marvelcharcall(rand, keyhash, pubkey, lookmeup):
    r = requests.get(f"{API}?name={lookmeup}&ts={rand}&apikey={pubkey}&hash={keyhash}")  # send an HTTP GET to this location

    # the marvel APIs are "flakey" at best, so check for a 200 response
    if r.status_code != 200:
        response = None     #
    else:
        response = r.json()

    # return the HTTP response with the JSON removed
    return response


def main():

    ## harvest private key
    with open(args.dev) as pkey:
        privkey = pkey.read().rstrip('\n')

    ## harvest public key
    with open(args.pub) as pkey:
        pubkey = pkey.read().rstrip('\n')

    ## create an integer from a float timestamp (for our RAND)
    rand = str(time.time()).rstrip('.')

    ## build hash with hashbuilder(timestamp, privatekey, publickey)
    keyhash = hashbuilder(rand, privkey, pubkey)

    ## call the API with marvelcharcall(timestamp, hash, publickey, character)
    result = marvelcharcall(rand, keyhash, pubkey, args.hero)

    name= result["data"]["results"][0]["name"]

    print("Name:",name,"\n")

    desc= result["data"]["results"][0]["description"]
    print("Description:")
    if len(desc) > 0:
        print(desc)
    else:
        print("None Provided")

    # thumbnail
    path= result["data"]["results"][0]["thumbnail"]["path"]
    extension= result["data"]["results"][0]["thumbnail"]["extension"]
    final= path + "/portrait_small." + extension

    r= requests.get(path + "/portrait_small." + extension) # create HTTP response object
      
    with open(f"/home/student/static/{name}.{extension}",'wb') as f:
        f.write(r.content)

    print(f'\nComic Count: {result["data"]["results"][0]["comics"]["available"]}')

    print(f"\nFive Comics featuring {name}:")
    totalcomics= 5
    for comicdict in result["data"]["results"][0]["comics"]["items"]:
        if totalcomics == 0:
            break
        else:
            print("-",comicdict["name"])
            totalcomics -= 1
        

## Define arguments to collect
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # This allows us to pass in public and private keys
    parser.add_argument('--dev', help='Provide the /path/to/file.priv containing Marvel private developer key')
    parser.add_argument('--pub', help='Provide the /path/to/file.pub containing Marvel public developer key')
    parser.add_argument('--hero', help='Character to search for within the Marvel universe')
    args = parser.parse_args()
    main()
-->
