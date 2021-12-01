#!/usr/bin/python3

# standard library modules first
import time

# 3rd party modules second
import requests
import reverse_geocoder as rg

URL= "http://api.open-notify.org/iss-now.json"

def main():
    # return API response, turn JSON into a python dictionary
    resp= requests.get(URL).json()

    # pull appropriate values for use later
    lat= resp["iss_position"]["latitude"]
    lon= resp["iss_position"]["longitude"]
    ts= resp["timestamp"]

    # convert epoch time into a human readable format
    hr_ts= time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))

    # return an ordered dictionary using our lat/lon
    locator_resp= rg.search((lat, lon))

    # slice that object to return the city name only
    city= locator_resp[0]["name"]

    # slice the object again to return the country
    country= locator_resp[0]["cc"]

    print(f"""
CURRENT LOCATION OF THE ISS:
Timestamp: {hr_ts}
Lon: {lon}
Lat: {lat}
City/Country: {city}, {country}
""")

if __name__=="__main__":
    main()
