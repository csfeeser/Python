# Making Multiple HTTP GET Requests to API

This warmup uses an unofficial Game of Thrones API- [An Api of Ice and Fire](https://www.anapioficeandfire.com)

<img src="https://cdn-media-1.freecodecamp.org/images/1*zWAQiGmSUNnBMl6D12xi7A.jpeg" alt="drawing" width="500"/>

Below is a script that will allow you to return information about one of the HUNDREDS (thousands?) of characters in the Game of Thrones literary universe! Run the script and enter a number (583 will return Jon Snow!)

```python
#!/usr/bin/python3
import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        pprint.pprint(got_dj)

if __name__ == "__main__":
        main()
```

Note that the output contains the following:

- `books` - books that the character appeared as a non-centric character
- `povBooks` - books that the character appeared as a narrator
- `allegiances` - groups or families that the character belongs to

ALTER THE SCRIPT ABOVE so that the output instead returns ONLY the following:

- The name of the character
- The name(s) of books the character appeared in
- The name(s) of allegiances the character has (if any)

BONUSES:
- If the character doesn't have a name, return their FIRST alias instead.
- Specify if each book the character was in was POV or not.
- Error handle for bad requests!
