# Morning Exercise: ISS TRACKER!

![Image description](https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2020/11/international_space_station/22293527-2-eng-GB/International_Space_Station_pillars.gif)

SPACE... the final frontier! Click the following link to view an open API that, upon request, returns the latitude and longitude of the ISS as it flies over earth!

http://api.open-notify.org/iss-now.json

## Your challenge this morning is to do the following:

#### Part 1: 
- Using the **requests** module, access the API from the link above and pull/translate the JSON!

<details>
<summary>Chad, I haven't had my dang coffee yet. How about a lil' code to get me started?</summary>

```python
#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
    
URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()

if __name__ == "__main__":
    main()
```
    
</details>

#### Part 2: 
- This API changes EVERY SINGLE TIME a GET request is sent to it (it's moving 4.76 miles per second, after all!) Make your script return the collected data into something like this:
    
    ```
    CURRENT LOCATION OF THE ISS:
    Lon: -52.7658
    Lat: 37.1268
    ```

<details>
<summary>Solution to returning longitude and latitude</summary>

```python
#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
    
URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()
    
    # SOLUTION TO PART 2
    lon= resp["iss_position"]["longitude"]
    lat= resp["iss_position"]["latitude"]
    
    print(f"""
    CURRENT LOCATION OF THE ISS:
    Lon: {lon}
    Lat: {lat}
    """)

if __name__ == "__main__":
    main()
```
    
</details>

#### Part 3: SUPER BONUS!
- This API also returns the timestamp of when the response was generated in [Epoch time (click here to see how Epoch time works!)](https://www.epochconverter.com/). Return this value, but make it human readable so your output looks like so:

    ```
    CURRENT LOCATION OF THE ISS:
    Timestamp: 2021-08-09 14:08:29
    Lon: -52.7658
    Lat: 37.1268
    ```

    > Hint: Google "python convert epoch time to date time"

<details>
<summary>Solution to converting timestamp</summary>

```python
#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime

URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()
    

    lon= resp["iss_position"]["longitude"]
    lat= resp["iss_position"]["latitude"]

    # SOLUTION TO PART 3
    # import datetime added above
    ts= resp["timestamp"]
    ts = datetime.datetime.fromtimestamp(ts)
    
    print(f"""
    CURRENT LOCATION OF THE ISS:
    Timestamp: {ts}
    Lon: {lon}
    Lat: {lat}
    """)

if __name__ == "__main__":
    main()
```
    
</details>

#### Part 4: MEGA BONUS
- You've got the location... but that's not very human readable, is it? What CITY and COUNTRY is the ISS currently flying across? Take a look at the 3rd party library **reverse_geocoder**- there is [copy/pasteable code you can use here!](https://github.com/csfeeser/Python/blob/master/enrichment/geocoder.md)

    ```
    CURRENT LOCATION OF THE ISS:
    Timestamp: 2021-08-09 14:08:29
    Lon: 77.22445
    Lat: 28.63576
    City/Country: New Delhi, IN
    ```

<details>
<summary>Solution to all the above:</summary>

```python
#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime
import reverse_geocoder as rg ## PART 4 SOLUTION
    
URL= "http://api.open-notify.org/iss-now.json"
    
def main():
    resp= requests.get(URL).json()
    

    lon= resp["iss_position"]["longitude"]
    lat= resp["iss_position"]["latitude"]
    ts= resp["timestamp"]
    ts = datetime.datetime.fromtimestamp(ts)

    # return an ordered dictionary using our lat/lon vars
    locator_resp= rg.search((lat, lon))
                                    # add verbose=False argument to remove the
                                    # "Loading formatted geocoded file..." output

    # slice that object to return the city name only
    city= locator_resp[0]["name"]

    # slice the object again to return the country
    country= locator_resp[0]["cc"]

    print(f"""
    CURRENT LOCATION OF THE ISS:
    Timestamp: {ts}
    Lon: {lon}
    Lat: {lat}
    City/Country: {city}, {country}
    """)

if __name__ == "__main__":
    main()
```
</details>
