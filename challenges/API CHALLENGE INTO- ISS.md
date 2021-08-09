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

    ### MEGA BONUS
    
0. You've got the location... but that's not very human readable, is it? What CITY is the ISS currently flying across? Take a look at the 3rd party library **reverse_geocoder**- there is [copy/pasteable code you can use here!](https://www.geeksforgeeks.org/python-reverse-geocoding-to-get-location-on-a-map-using-geographic-coordinates/)

    ```
    CURRENT LOCATION OF THE ISS:
    Timestamp: 2021-08-09 14:08:29
    Lon: -52.7658
    Lat: 37.1268
    City: Saint-Pierre
    ```

<details>
<summary>Need help getting started?</summary>
<br>
    
```python
#!/usr/bin/python3

import requests
  
URL= http://api.open-notify.org/astros.json
def main():
    # requests.get() sends GET request to the URL
    # .json() strips JSON off the response and translates into Python!
    resp= requests.get(URL).json()
    
main()

</details>

