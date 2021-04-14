#!/usr/bin/python3
"""Alta3 || Tracking ISS"""

import urllib.request
import json

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():

    ## Call the webservice
    groundctrl = urllib.request.urlopen(MAJORTOM)

    ## put fileobject into helmet
    helmet = groundctrl.read()

    ## decode JSON to Python data structure
    helmetson = json.loads(helmet.decode('utf-8'))

    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(helmetson)

    print('\n\nPeople in Space: ', helmetson['number'])
    for x in helmetson["people"]:
        print(f"{x['name']} is on the {x['craft']}.")
main()
