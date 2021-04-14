#!/usr/bin/env python3
import requests
from pprint import pprint as pp # part of the standard libray
# import webbrowser


## define some constants
NASAAPI = 'https://api.nasa.gov/planetary/apod?' # this is our API to call
MYKEY = 'api_key=DEMO_KEY' ## this is our api key
DATE = '&date=' + input("Enter a date in this format: YYYY-MM-DD")


## pretty print json
def main():
    """run-time code"""
    nasaapiobj = requests.get(NASAAPI + MYKEY + DATE) # call the webservice
    nasaread = nasaapiobj.json() # parse the JSON blob returned

    print("Title:", nasaread['title'])
    print("Date:", nasaread['date'])
    print(nasaread['explanation']) # display the value for the key explanation

    choice= input("HD or SD? ").upper()

    if choice == "HD":
        print("Link to the APOD:", nasaread.get('hdurl',"No HD URL for today!"))
    else:
        print("Link to the APOD:", nasaread.get('url'))


    #input('\nPress ENTER to view this photo of the day') # pause for ENTER
    # webbrowser.open(nasaread['hdurl']) # open in the webbrowser

main()
