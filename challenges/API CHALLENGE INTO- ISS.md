# Morning Challenge: INTERNATIONAL SPACE STATION (ISS) TRACKER!

![Image description](https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2020/11/international_space_station/22293527-2-eng-GB/International_Space_Station_pillars.gif)

SPACE... the final frontier! Click the following link to view an open API that, upon request, returns the latitude and longitude of the ISS as it flies over earth!

http://api.open-notify.org/iss-now.json

**Your challenge this morning is to do the following:**

1. Using the **requests** module, access the API from the link above and pull/translate the JSON!

0. This API changes EVERY SINGLE TIME a GET request is sent to it (it's moving 4.76 miles per second, after all!) Write a script that returns the collected data into something like this:
    
    ```
    CURRENT LOCATION OF THE ISS:
    Lon: -52.7658
    Lat: 37.1268
    ```

    ### SUPER BONUS

0. This API also returns the timestamp of when the response was generated in [Epoch time (click here to see how Epoch time works!)](https://www.epochconverter.com/). Return this value, but make it human readable so your output looks like so:

    ```
    CURRENT LOCATION OF THE ISS:
    Timestamp: 2021-08-09 14:08:29
    Lon: -52.7658
    Lat: 37.1268
    ```

    > Hint: Google "python convert epoch time to date time"
 
    ### MEGA BONUS
    
0. You've got the location... but that's not very human readable, is it? What CITY and COUNTRY is the ISS currently flying across? Take a look at the 3rd party library **reverse_geocoder**- there is [copy/pasteable code you can use here!](https://github.com/csfeeser/Python/blob/master/enrichment/geocoder.md)

    ```
    CURRENT LOCATION OF THE ISS:
    Timestamp: 2021-08-09 14:08:29
    Lon: 77.22445
    Lat: 28.63576
    City/Country: New Delhi, IN
    ```

```python
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
```
