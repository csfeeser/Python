#!/usr/bin/python3
"""Solution to the GOT Customization for Lab 19. requests library - Open APIs"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"
KEYS= ["allegiances", "books", "povBooks"]

def main():
    choice= input("Choose between 1 and 2000 to select a GoT character!\n>" )
 
    resp = requests.get(AOIF_CHAR + choice).json()
   
    # Let's print the name of the character so we know who we're looking at.
    # HOWEVER, some characters don't have names, only "aliases."
    # The ternary operator below returns the character's name if it exists, OR
    # the first "alias" of the character if not.
    # example, https://anapioficeandfire.com/api/characters/1
    print("CHARACTER:", end= " ")
    print(f"{resp['name']}\n" if resp['name'] else f"{resp['aliases'][0]}\n")

    # Next we'll loop across the dict keys specified at the top of the script
    # for each key we'll search in the API dict (books, povBooks, houses)--
    for key in KEYS:
        # print that key
        print(f"{key.upper()}:")
        # then test if there are any links in that key's list
        if len(resp[key]) != 0:
            # if so, loop those links and send GET requests to each
            for element in resp[key]:
                # print out the name of the book/house from the response
                print(requests.get(element).json()["name"])
        else:
            # if the list is empty, print "none" and move to the next key
            print("None.")
        print()

if __name__ == "__main__":
    main()
