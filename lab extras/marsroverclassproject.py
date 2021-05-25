#!/usr/bin/python3

import requests
import pprint
#NASAAPI = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=DEMO_KEY&earth_date=2015-05-30"

# this function grabs our credentials
def returncreds():
    ## first I want to grab my credentials
    with open("nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    
    return nasacreds

# this is our main function
def main():

    cameralist = {"curiosity":["fhaz","rhaz","mast","chemcam","mahli","mardi","navcam"],"opportunity":["fhaz","rhaz","navcam","pancam""minites"],"spirit":["fhaz","rhaz","navcam","pancam","minites"]}
    roverslist = []
    for list in cameralist:
        roverslist.append(list)

    print("Rovers List: \n")
    #for displayrovers in roverslist:
    print(*roverslist,"\n")
    roversname = input("Choose the rovers from the list")
   
    print("Camera List: \n")
    #for camlist in cameralist:
    print(*cameralist[roversname],"\n")         
    cameraname = input("Choose the camera name from the list")

    edate = input("Enter the earth date : ")

    ## first grab credentials
    nasacreds = returncreds()
    
    # https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=DEMO_KEY&earth_date=2015-05-30
    ## make a call to NASAAPI with our key
    NASAAPI = f'https://api.nasa.gov/mars-photos/api/v1/rovers/{roversname}/photos?camera={cameraname}&{nasacreds}&earth_date={edate}'



    apodresp = requests.get(NASAAPI)

    # Input 
    ## strip off json
    apod = apodresp.json()

    pprint.pprint(apod)

if __name__ == "__main__":
    main()
