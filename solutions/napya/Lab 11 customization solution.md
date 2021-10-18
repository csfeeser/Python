```
#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"


def data_lookup(data):
   """This function will take a list of links (be they books or houses) and returns the name value from each link"""

   content = []

   for x in data:
       resp= requests.get(x).json()
       content.append(resp["name"])

   return content

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        got = requests.get(AOIF_CHAR + got_charToLookup).json()

        print(f"""
        Name: {got['name']}
        Allegiances: {data_lookup(got['allegiances'])}
        Books: {data_lookup(got['books'])}
        POV Books: {data_lookup(got['povBooks'])}
        """)

if __name__ == "__main__":
        main()
```
