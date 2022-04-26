# Morning Challenge: ASTRONAUT TRACKER!

![Image description](https://media1.tenor.com/images/c2e16afc6bff5a5ec0f027f1cc209649/tenor.gif?itemid=15935992)

SPACE- the final frontier! Though we won't really be FOCUSING on APIs in this course, it will be good to experience how to access them with Python. The API we'll take a look at is a public API that records all current people in space and what vessel they are on. Check it out at http://api.open-notify.org/astros.json

**Try the following:**

1. The code below uses the **requests** module. It is ALREADY WRITTEN to access the API, grab the data, and translate it into a Python dictionary!

    ```python
    #!/usr/bin/python3

    import requests

    URL= "http://api.open-notify.org/astros.json"
    
    def main():
        # requests.get() requests info from the URL
        # .json() method transforms that data into a Pythonic dictionary!
        sliceme= requests.get(URL).json()

        print(sliceme)
        print(type(sliceme))

    main()
    ```

1. APIs are cool in that they provide highly accessible data (they're usually found online) for your programs to use. ***They are also one of the best ways to build your slicing and for loop skills.*** The data is also dynamic- for instance, this API changes EVERY SINGLE TIME astronauts leave/arrive in space! 
 
2. Edit the script above. Add a *for loop* that returns each astronaut and the craft that they are on. Your output should look like this:
    
    ```
    People in Space:  7
    Raja Chari is on the ISS
    Tom Marshburn is on the ISS
    Kayla Barron is on the ISS
    Matthias Maurer is on the ISS
    Oleg Artemyev is on the ISS
    Denis Matveev is on the ISS
    Sergey Korsakov is on the ISS
    ```

### Chad I am a BOSS and I finished that! What's next!

Nice work!!! Here's another URL for a similar API:

`http://api.open-notify.org/iss-now.json`

That link leads to a different API that returns the latitude and longitude of the ISS over Earth!  

- Copy the `requests.get()` line of code and paste it into a new line.
- Change that second `requests.get()` so that it uses the new URL above.
- Slice the data that gets returned so it looks something like this instead:

```
CURRENT LOCATION OF THE ISS:
Lon: -52.7658
Lat: 37.1268
```

Your final output should look like this:

    People in Space:  7
    Raja Chari is on the ISS
    Tom Marshburn is on the ISS
    Kayla Barron is on the ISS
    Matthias Maurer is on the ISS
    Oleg Artemyev is on the ISS
    Denis Matveev is on the ISS
    Sergey Korsakov is on the ISS

    CURRENT LOCATION OF THE ISS:
    Lon: -52.7658
    Lat: 37.1268
